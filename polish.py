"""Production polish layer: security, SEO, PWA, performance and UX hooks.

Wraps the page renderer after premium.install() and writes site-level files.
"""
import json, re
from html import escape
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent
SITE_NAME = {"ar": "الأب نيكولا كلويترز — إرث حيّ", "en": "Father Nicolas Kluiters — A Living Legacy", "fr": "Père Nicolas Kluiters — Un héritage vivant"}
LOCALE = {"ar": "ar_AR", "en": "en_US", "fr": "fr_FR"}
UI = {
    "ar": {"offline": "أنت غير متصل — تُعرض الصفحات المحفوظة.", "top": "العودة إلى أعلى الصفحة", "toc": "في هذه الصفحة", "prev": "السابق", "next": "التالي"},
    "en": {"offline": "You are offline — showing saved pages.", "top": "Back to top", "toc": "On this page", "prev": "Previous", "next": "Next"},
    "fr": {"offline": "Vous êtes hors ligne — pages enregistrées affichées.", "top": "Haut de page", "toc": "Sur cette page", "prev": "Précédent", "next": "Suivant"},
}
HINTS = {"ar": "هذا الموقع متوفر بالعربية — افتح النسخة العربية", "en": "This site is available in English — open the English version", "fr": "Ce site est disponible en français — ouvrir la version française"}
CSP = ("default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' https: data:; font-src 'self'; "
       "connect-src 'self'; worker-src 'self'; manifest-src 'self'; base-uri 'self'; form-action 'none'; object-src 'none'")
_dims = {}

def dims(rel):
    if rel not in _dims:
        try:
            with Image.open(ROOT / rel) as im: _dims[rel] = im.size
        except Exception: _dims[rel] = None
    return _dims[rel]

def install(g):
    original = g["render"]
    BASE, PAGES = g["BASE"], g["PAGES"]

    def render(lang, slug):
        html = original(lang, slug)
        pre = "assets/" if lang == "ar" else "../assets/"
        up = "" if lang == "ar" else "../"
        data, T = g["CONTENT"][lang][slug], g["TEXT"][lang]
        url = BASE + g["locale_path"](lang, slug)
        # --- head: drop third-party fonts, add self-hosted fonts, icons, manifest, security, social
        html = re.sub(r"<link rel='preconnect'[^>]*>\n?", "", html)
        html = re.sub(r"<link href='https://fonts\.googleapis\.com[^>]*>\n?", "", html)
        face = "NotoNaskhArabic-400" if lang == "ar" else "DMSans-400"
        face2 = "NotoNaskhArabic-700" if lang == "ar" else "DMSans-500"
        og_alt = escape(T["site"], quote=True)
        title = escape(data["title"], quote=True)
        desc = escape(data["summary"], quote=True)
        head_extra = f"""<meta http-equiv='Content-Security-Policy' content="{CSP}">
<meta name='referrer' content='strict-origin-when-cross-origin'>
<meta name='color-scheme' content='light'>
<meta property='og:url' content='{url}'>
<meta property='og:site_name' content='{escape(SITE_NAME[lang], quote=True)}'>
<meta property='og:locale' content='{LOCALE[lang]}'>
<meta property='og:image:width' content='1200'>
<meta property='og:image:height' content='630'>
<meta property='og:image:alt' content='{og_alt}'>
<meta name='twitter:card' content='summary_large_image'>
<meta name='twitter:title' content='{title}'>
<meta name='twitter:description' content='{desc}'>
<meta name='twitter:image' content='{BASE}/assets/og-image.jpg'>
<link rel='icon' href='{pre}favicon.svg' type='image/svg+xml'>
<link rel='apple-touch-icon' href='{pre}apple-touch-icon.png'>
<link rel='manifest' href='{up}manifest.webmanifest'>
<link rel='preload' href='{pre}fonts/{face}.woff2' as='font' type='font/woff2' crossorigin>
<link rel='preload' href='{pre}fonts/{face2}.woff2' as='font' type='font/woff2' crossorigin>
<link rel='stylesheet' href='{pre}polish.css'>
"""
        html = html.replace(f"{BASE}/assets/portrait-archive.jpg", f"{BASE}/assets/og-image.jpg")
        html = html.replace("<title>", head_extra + "<title>", 1)
        # --- structured data
        crumbs = [{"@type": "ListItem", "position": 1, "name": T["site"], "item": BASE + g["locale_path"](lang, "index")}]
        if slug != "index":
            crumbs.append({"@type": "ListItem", "position": 2, "name": data["title"], "item": url})
        graph = [{"@type": "WebPage", "@id": url, "url": url, "name": data["title"], "description": data["summary"], "inLanguage": lang,
                  "isPartOf": {"@id": BASE + "/#website"}, "primaryImageOfPage": BASE + "/assets/og-image.jpg"},
                 {"@type": "BreadcrumbList", "itemListElement": crumbs}]
        if slug == "index":
            graph.append({"@type": "WebSite", "@id": BASE + "/#website", "url": BASE + "/", "name": SITE_NAME[lang], "inLanguage": ["ar", "en", "fr"]})
        if slug in ("index", "life"):
            graph.append({"@type": "Person", "name": "Nicolas Kluiters", "alternateName": ["نيكولا كلويترز", "Nicolaas Kluiters"], "jobTitle": "Jesuit priest",
                          "birthDate": "1940", "deathDate": "1985", "nationality": "Dutch", "workLocation": {"@type": "Place", "name": "Barqa, Bekaa, Lebanon"}})
        ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False).replace("<", "\\u003c")
        html = html.replace("</head>", f"<script type='application/ld+json'>{ld}</script>\n</head>", 1)
        # --- images: intrinsic size for local assets (no layout shift) + async decode
        def img(m):
            tag, rel = m.group(0), m.group(2)
            d = dims("assets/" + rel)
            if d and "width=" not in tag:
                tag = tag.replace("<img ", f"<img width='{d[0]}' height='{d[1]}' decoding='async' ", 1)
            return tag
        html = re.sub(r"<img [^>]*src='((?:\.\./)?assets/)([^']+)'[^>]*>", img, html)
        # --- previous / next page navigation
        i = PAGES.index(slug) if slug in PAGES else None
        if i is not None:
            u = UI[lang]; names = g["NAV"][lang]; parts = []
            if i > 0:
                parts.append(f"<a class='prev' rel='prev' href='{g['nav_href'](lang, PAGES[i-1], lang)}'><small>{u['prev']}</small>{escape(names[i-1])}</a>")
            if i < len(PAGES) - 1:
                parts.append(f"<a class='next' rel='next' href='{g['nav_href'](lang, PAGES[i+1], lang)}'><small>{u['next']}</small>{escape(names[i+1])}</a>")
            html = html.replace("</article>", f"<nav class='page-nav' aria-label='{escape(T['menu'], quote=True)}'>{''.join(parts)}</nav></article>", 1)
        # --- on-this-page list generated at build time (no layout shift)
        m = re.search(r"<div class='prose'>", html)
        if m:
            start = m.end(); end = html.find("</article>", start)
            seg = html[start:end]; heads = []
            def tag(mm):
                n = len(heads) + 1; heads.append((f"s{n}", re.sub(r"<[^>]+>", "", mm.group(1))))
                return f"<h2 id='s{n}'>{mm.group(1)}</h2>"
            seg = re.sub(r"<h2>(.*?)</h2>", tag, seg, flags=re.S)
            if len(heads) >= 4:
                toc = (f"<nav class='toc' aria-label='{UI[lang]['toc']}'><h2>{UI[lang]['toc']}</h2><ol>"
                       + "".join(f"<li><a href='#{i}'>{t}</a></li>" for i, t in heads) + "</ol></nav>")
                html = html[:m.start()] + toc + "<div class='prose'>" + seg + html[end:]
        # --- polish script
        links = {l: (("../" if lang != "ar" else "") + g["locale_path"](l, slug).lstrip("/")) for l in ("ar", "en", "fr")}
        pdata = json.dumps({"t": UI[lang], "sw": up + "sw.js", "hints": HINTS, "links": links}, ensure_ascii=False).replace("<", "\\u003c")
        html = html.replace("</body>", f"<script id='polish-data' type='application/json'>{pdata}</script><script src='{pre}polish.js' defer></script></body>", 1)
        return html
    g["render"] = render

def page(title, body, lang="en", rtl=False):
    return f"""<!doctype html>
<html lang='{lang}' dir='{'rtl' if rtl else 'ltr'}'>
<head><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1'>
<meta name='robots' content='noindex'><meta http-equiv='Content-Security-Policy' content="{CSP}">
<meta name='theme-color' content='#17241f'><link rel='icon' href='/assets/favicon.svg' type='image/svg+xml'>
<link rel='stylesheet' href='/assets/site.css'><link rel='stylesheet' href='/assets/polish.css'><title>{title}</title></head>
<body><main id='main' class='status-page'>{body}</main></body></html>
"""

def finish(g):
    BASE = g["BASE"]
    status = ("<section class='page-hero'><div class='page-hero-copy'><p class='eyebrow'>{e}</p><h1>{h}</h1><p class='page-summary'>{p}</p>"
              "<p><a class='button-link' href='{href}'>{b}</a></p></div></section>")
    langs = "<p class='language-switch'><a href='/index.html' lang='ar'>العربية</a><a href='/en/index.html' lang='en'>English</a><a href='/fr/index.html' lang='fr'>Français</a></p>"
    (ROOT / "404.html").write_text(page("404 · Nicolas Kluiters",
        status.format(e="404", h="Page not found · الصفحة غير موجودة · Page introuvable", p="The page may have moved. Return to the archive.", href="/en/index.html", b="Home · الرئيسية · Accueil") + langs), encoding="utf-8")
    (ROOT / "offline.html").write_text(page("Offline · Nicolas Kluiters",
        status.format(e="OFFLINE", h="You are offline · أنت غير متصل · Hors ligne", p="Pages you have already opened remain available. Reconnect to explore the rest of the archive.", href="/en/index.html", b="Home · الرئيسية · Accueil") + langs), encoding="utf-8")
    manifest = {"name": SITE_NAME["ar"] + " | " + SITE_NAME["en"], "short_name": "Nicolas Kluiters", "description": "A trilingual historical archive on Father Nicolas Kluiters and Barqa.",
                "lang": "ar", "dir": "rtl", "start_url": "./index.html", "scope": "./", "display": "standalone", "background_color": "#f5f2ea", "theme_color": "#17241f",
                "icons": [{"src": "assets/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "assets/icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable"},
                          {"src": "assets/favicon.svg", "sizes": "any", "type": "image/svg+xml"}]}
    (ROOT / "manifest.webmanifest").write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")
    (ROOT / "CNAME").write_text(BASE.split("//")[1] + "\n", encoding="utf-8")
    sec = ".well-known"; (ROOT / sec).mkdir(exist_ok=True)
    (ROOT / sec / "security.txt").write_text(f"Contact: https://github.com/ccg-cyber/nicolas-kluiters-living-legacy/issues\nExpires: 2027-11-06T00:00:00.000Z\nPreferred-Languages: en, fr, ar\nCanonical: {BASE}/.well-known/security.txt\n", encoding="utf-8")
