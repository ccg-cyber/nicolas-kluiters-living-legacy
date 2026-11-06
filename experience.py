"""Experience layer: new pages (prayer sanctuary, Maronite heritage, play), redesigned home,
app-like navigation, pilgrim passport, themes and personalised retention features."""
import json
from html import escape
from experience_data import *

IDX = {"ar": 0, "en": 1, "fr": 2}
ORDER = ["index", "pray", "heritage", "play", "discover", "life", "barqa", "timeline", "cause", "places", "archive", "media", "prayer", "sources"]
STAMP_PAGES = ["life", "barqa", "timeline", "cause", "places", "archive", "sources", "discover", "prayer", "media", "pray", "heritage", "play"]
ICON = {"index": "⌂", "pray": "✝", "heritage": "☘", "play": "◈", "discover": "⛰", "life": "☉", "barqa": "❖", "timeline": "⇥", "cause": "✧", "places": "⌖", "archive": "▣", "media": "▶", "prayer": "◌", "sources": "☰"}
GROUP = {"pray": "faith", "heritage": "faith", "prayer": "faith", "cause": "faith", "play": "play", "media": "play", "archive": "play", "discover": "story", "life": "story", "barqa": "story", "timeline": "story", "places": "story", "sources": "story"}

def t(k, lang): return T[k][IDX[lang]]

def tiles(lang, hrefs):
    items = [("pray", "tile_candle", "p-candle", "🕯", "#candle"), ("pray", "tile_rosary", "p-rosary", "◯", "#rosary"),
             ("heritage", "tile_saints", "", "✝", "#saints"), ("heritage", "tile_feasts", "", "◷", "#feasts"),
             ("play", "tile_play", "", "◈", "#memory"), ("play", "tile_quiz", "", "?", "#quiz")]
    out = []
    for i, (page, key, _, ic, anchor) in enumerate(items):
        out.append(f"<a class='tile tile-{i+1}' href='{hrefs[page]}{anchor}'><span class='tile-ic' aria-hidden='true'>{ic}</span><h3>{t(key, lang)}</h3><p>{t(key + '_d', lang)}</p><span class='tile-go' aria-hidden='true'>→</span></a>")
    return "".join(out)

def home_body(lang, hrefs):
    return f"""<section class='today-panel' data-today aria-label='{t('today', lang)}'></section>
<section class='home-do'><h2>{t('h_do', lang)}</h2><div class='tile-grid'>{tiles(lang, hrefs)}</div></section>
<section class='home-story'><div><p class='eyebrow'>{t('h_story_k', lang)}</p><h2>{t('h_story_h', lang)}</h2><p>{t('h_story_p', lang)}</p>
<div class='cta-row'><a class='button-link' href='{hrefs['life']}'>{t('h_story_a', lang)}</a><a class='ghost-link' href='{hrefs['timeline']}'>{t('h_story_b', lang)} →</a></div></div>
<figure class='story-photo'><img src='ASSET_PREFIXportrait-restored-1536.webp' alt='{t('h_alt', lang)}' loading='lazy'></figure></section>
<section class='continue-panel' data-continue hidden></section>
<section class='journey-bar' data-journey aria-live='polite'></section>"""

def candle_html(lang):
    return f"""<section id='candle' class='sanct-block candle-block'>
<div class='sanct-head'><p class='eyebrow'>01</p><h2>{t('p_candle_h', lang)}</h2><p>{t('p_candle_p', lang)}</p></div>
<div class='candle-stage'><div class='hero-candle' aria-hidden='true'><i class='halo'></i><i class='flame'></i><b class='wick'></b><span class='wax'></span></div>
<div class='candle-form'><label for='candle-note'>{t('p_intention', lang)}</label><textarea id='candle-note' maxlength='140' rows='2'></textarea>
<div class='cta-row'><button id='candle-light' class='button-link' type='button'>{t('p_light', lang)}</button><button id='candle-out' class='ghost-btn' type='button'>{t('p_extinguish', lang)}</button></div>
<p id='candle-count' class='soft' aria-live='polite'></p></div></div>
<ul id='candle-row' class='candle-row' aria-label='{t('p_candle_h', lang)}'></ul></section>"""

def rosary_html(lang):
    return f"""<section id='rosary' class='sanct-block'>
<div class='sanct-head'><p class='eyebrow'>02</p><h2>{t('p_rosary_h', lang)}</h2><p>{t('p_rosary_p', lang)}</p></div>
<div class='rosary-card' data-rosary><div class='mys-tabs' role='tablist' aria-label='{t('p_mys_today', lang)}'></div>
<div class='rosary-main'><p class='rosary-decade' aria-live='polite'></p><h3 class='rosary-mystery'></h3>
<ol class='beads' aria-hidden='true'></ol><p class='rosary-bead soft'></p>
<div class='cta-row center'><button class='button-link big' data-hail type='button'>{t('p_hail', lang)}</button><button class='ghost-btn' data-undo type='button'>{t('p_undo', lang)}</button><button class='ghost-btn' data-restart type='button'>{t('p_restart', lang)}</button></div>
<p class='rosary-done' role='status'></p></div></div></section>"""

def library_html(lang):
    ids = [("cross", "p_cross", "cross_t"), ("our", "p_our", "our_t"), ("hail", "p_hailmary", "hail_t"), ("glory", "p_glory", "glory_t")]
    det = "".join(f"<details class='prayer-item'{' open' if i == 1 else ''}><summary>{t(h, lang)}</summary><p class='prayer-text'>{t(tx, lang)}</p>{syr(lang) if i == 1 else ''}</details>" for i, (_, h, tx) in enumerate(ids))
    return f"""<section id='library' class='sanct-block'><div class='sanct-head'><p class='eyebrow'>03</p><h2>{t('p_lib_h', lang)}</h2><p>{t('p_lib_p', lang)}</p></div>
<div class='prayer-list'>{det}</div>
<div class='ambient-card'><div><h3>{t('p_ambient', lang)}</h3><p class='soft'>{t('p_ambient_p', lang)}</p></div><button id='ambient' class='button-link' type='button' aria-pressed='false' data-on='{t('p_ambient_on', lang)}' data-off='{t('p_ambient_off', lang)}'>{t('p_ambient_off', lang)}</button></div>
<button class='ghost-btn' data-print type='button'>{t('p_print', lang)}</button></section>"""

def syr(lang):
    return f"<div class='syriac-note'><p>{t('p_syr_note', lang)}</p><p class='syriac' lang='syr' dir='rtl'>ܐܒܘܢ ܕܒܫܡܝܐ ܢܬܩܕܫ ܫܡܟ</p><p class='soft'>{t('p_syr_tr', lang)}</p></div>"

def pray_body(lang):
    return f"<div data-today class='today-panel compact'></div>" + candle_html(lang) + rosary_html(lang) + library_html(lang)

def heritage_body(lang):
    facts = "".join(f"<div><dt>{t(a, lang)}</dt><dd>{t(b, lang)}</dd></div>" for a, b in [("he_f1", "he_f1v"), ("he_f2", "he_f2v"), ("he_f3", "he_f3v"), ("he_f4", "he_f4v"), ("he_f5", "he_f5v")])
    i = IDX[lang]
    saints = "".join(f"<button class='saint-card' type='button' data-saint='{s[0]}'><span class='saint-years'>{s[1]}</span><strong>{s[2][i]}</strong><span class='text-link'>{t('he_read', lang)} →</span></button>" for s in SAINTS)
    chips = "".join(f"<button type='button' data-filter='{k}' aria-pressed='{'true' if k == 'all' else 'false'}'>{t(l, lang)}</button>" for k, l in [("all", "he_all"), ("saint", "he_saintsf"), ("marian", "he_marian"), ("lord", "he_lord"), ("nk", "he_nk")])
    return f"""<section class='sanct-block'><div class='sanct-head'><p class='eyebrow'>01</p><h2>{t('he_intro_h', lang)}</h2><p>{t('he_intro_p', lang)}</p></div>
<dl class='fact-strip'>{facts}</dl><p class='editorial-note'>{t('he_nk_p', lang)}</p></section>
<section id='saints' class='sanct-block'><div class='sanct-head'><p class='eyebrow'>02</p><h2>{t('he_saints_h', lang)}</h2><p>{t('he_saints_p', lang)}</p></div><div class='saint-grid'>{saints}</div>
<dialog id='saint-dialog'><div class='dialog-top'><strong id='saint-name'></strong><button type='button' data-close-saint>×</button></div><p id='saint-years' class='eyebrow'></p><p id='saint-text'></p></dialog></section>
<section id='feasts' class='sanct-block'><div class='sanct-head'><p class='eyebrow'>03</p><h2>{t('he_feasts_h', lang)}</h2><p>{t('he_feasts_p', lang)}</p></div>
<div class='next-feast' data-next-feast aria-live='polite'></div>
<div class='chip-row' role='group'>{chips}</div><ol class='feast-list' data-feasts></ol>
<button id='ics' class='button-link' type='button'>{t('he_ics', lang)}</button></section>"""

def play_body(lang):
    return f"""<section id='memory' class='sanct-block'><div class='sanct-head'><p class='eyebrow'>01</p><h2>{t('pl_mem_h', lang)}</h2><p>{t('pl_mem_p', lang)}</p></div>
<div class='game-bar'><span>{t('pl_moves', lang)}: <b id='mem-moves'>0</b></span><span>{t('pl_time', lang)}: <b id='mem-time'>0</b>s</span><span>{t('pl_best', lang)}: <b id='mem-best'>–</b></span><button id='mem-new' class='ghost-btn' type='button'>{t('pl_new', lang)}</button></div>
<div id='mem-grid' class='mem-grid'></div><p id='mem-msg' class='win-msg' role='status'></p></section>
<section id='quiz' class='sanct-block'><div class='sanct-head'><p class='eyebrow'>02</p><h2>{t('pl_quiz_h', lang)}</h2><p>{t('pl_quiz_p', lang)}</p></div>
<div id='quiz2' class='quiz2'><button id='quiz2-start' class='button-link' type='button'>{t('pl_start', lang)}</button></div></section>
<section id='cards' class='sanct-block'><div class='sanct-head'><p class='eyebrow'>03</p><h2>{t('pl_card_h', lang)}</h2><p>{t('pl_card_p', lang)}</p></div>
<div class='studio'><div class='studio-preview'><canvas id='card-canvas' width='1080' height='1350' role='img' aria-label='{t('pl_preview', lang)}'></canvas></div>
<div class='studio-controls'><label for='card-verse'>{t('pl_verse', lang)}</label><select id='card-verse'></select>
<fieldset><legend>{t('pl_bg', lang)}</legend><div class='chip-row'><button type='button' data-bg='0' aria-pressed='true'>{t('pl_bg1', lang)}</button><button type='button' data-bg='1' aria-pressed='false'>{t('pl_bg2', lang)}</button><button type='button' data-bg='2' aria-pressed='false'>{t('pl_bg3', lang)}</button></div></fieldset>
<fieldset><legend>{t('pl_res', lang)}</legend><div class='chip-row'><button type='button' data-res='1' aria-pressed='true'>{t('pl_hd', lang)}</button><button type='button' data-res='2' aria-pressed='false'>{t('pl_uhd', lang)}</button></div></fieldset>
<div class='cta-row'><button id='card-dl' class='button-link' type='button'>{t('pl_dl', lang)}</button><button id='card-share' class='ghost-btn' type='button'>{t('pl_share', lang)}</button></div></div></div></section>"""

def hero_html(lang, hrefs, data):
    return f"""<section class='xhero' data-xhero><div class='xhero-bg' aria-hidden='true'></div><div class='xhero-shade' aria-hidden='true'></div>
<div class='xhero-inner'><p class='xhero-kicker'>{t('h_kicker', lang)}</p><h1>{escape(data['title'])}</h1><p class='xhero-sub'>{escape(data['summary'])}</p>
<div class='cta-row'><a class='button-link gold' href='{hrefs['pray']}#candle'>🕯 {t('h_cta1', lang)}</a><a class='hero-ghost' href='{hrefs['life']}'>{t('h_cta2', lang)}</a><a class='hero-ghost' href='{hrefs['play']}'>{t('h_cta3', lang)}</a></div></div>
<a class='xhero-scroll' href='#main-after' aria-label='{t('h_scroll', lang)}'><span>{t('h_scroll', lang)}</span><i></i></a></section><span id='main-after'></span>"""

def install(g):
    LOC = g["LOCALES"]
    for lang in LOC:
        i = IDX[lang]
        labels = dict(zip(g["PAGES"], g["NAV"][lang]))
        labels.update({"pray": T["pray"][i], "heritage": T["heritage"][i], "play": T["play"][i]})
        c = g["CONTENT"][lang]
        c["pray"] = {"eyebrow": T["eyebrow_pray"][i], "title": T["pray"][i], "summary": T["pray_sum"][i], "body": pray_body(lang)}
        c["heritage"] = {"eyebrow": T["eyebrow_heritage"][i], "title": T["heritage"][i], "summary": T["heritage_sum"][i], "body": heritage_body(lang)}
        c["play"] = {"eyebrow": T["eyebrow_play"][i], "title": T["play"][i], "summary": T["play_sum"][i], "body": play_body(lang)}
        hrefs = {s: ("index.html" if s == "index" else s + ".html") for s in ORDER}
        c["index"]["body"] = home_body(lang, hrefs)
        g["NAV"][lang][:] = [labels[s] for s in ORDER]
    g["PAGES"] = tuple(ORDER)
    original = g["render"]

    def render(lang, slug):
        html = original(lang, slug)
        i = IDX[lang]; up = "" if lang == "ar" else "../"; pre = "assets/" if lang == "ar" else "../assets/"
        hrefs = {s: ("index.html" if s == "index" else s + ".html") for s in ORDER}
        c = g["CONTENT"][lang]
        html = html.replace("ASSET_PREFIX", pre)
        # head: theme before paint + new stylesheet
        html = html.replace("<link rel='stylesheet' href='%spolish.css'>" % pre, "<link rel='stylesheet' href='%spolish.css'><link rel='stylesheet' href='%sexperience.css'><script src='%stheme.js'></script>" % (pre, pre, pre), 1)
        html = html.replace("<meta name='color-scheme' content='light'>", "<meta name='color-scheme' content='light dark'>")
        # header actions
        actions = (f"<div class='header-actions'><button type='button' class='icon-btn' data-theme-toggle aria-pressed='false' data-night='{t('theme_dark', lang)}' data-day='{t('theme_light', lang)}'><span aria-hidden='true'>☾</span><span class='sr'>{t('theme_dark', lang)}</span></button>"
                   f"<button type='button' class='icon-btn passport-chip' data-open-passport><span aria-hidden='true'>✦</span><b data-passport-count>0</b><span class='sr'>{t('passport', lang)}</span></button></div>")
        html = html.replace("<div class='language-switch'", actions + "<div class='language-switch'", 1)
        # home hero
        if slug == "index":
            import re
            hero = hero_html(lang, hrefs, c["index"])
            html = re.sub(r"<section class='page-hero home-hero'>.*?</section>", lambda m: hero, html, count=1, flags=re.S)
            html = re.sub(r"<section class='discovery-game'>.*?</section>", "", html, count=1, flags=re.S)
            html = html.replace("<div class='page-tools'>", "<div class='page-tools in-home'>", 1)
        # tab bar + dialogs + keep exploring
        tabs = [("index", "tab_home", "⌂"), ("pray", "tab_pray", "✝"), ("play", "tab_play", "◈"), ("heritage", "tab_heritage", "☘")]
        tab = "".join(f"<a href='{hrefs[s]}'{' aria-current=page' if s == slug else ''}><span aria-hidden='true'>{ic}</span>{t(k, lang)}</a>" for s, k, ic in tabs)
        tab += f"<button type='button' data-open-menu><span aria-hidden='true'>☰</span>{t('tab_more', lang)}</button>"
        menu_items = "".join(f"<a class='menu-item g-{GROUP.get(s, 'story')}' href='{hrefs[s]}'><span class='mi-ic' aria-hidden='true'>{ICON[s]}</span><span><strong>{escape(c[s]['title'])}</strong><small>{escape(c[s]['summary'])}</small></span></a>" for s in ORDER)
        dialogs = (f"<nav class='tabbar' aria-label='{t('tab_more', lang)}'>{tab}</nav>"
                   f"<dialog id='menu-dialog'><div class='dialog-top'><strong>{t('explore_all', lang)}</strong><button type='button' data-close-menu aria-label='{g['TEXT'][lang]['menu']}'>×</button></div><div class='menu-grid'>{menu_items}</div></dialog>"
                   f"<dialog id='passport-dialog'><div class='dialog-top'><strong>✦ {t('passport', lang)}</strong><button type='button' data-close-passport aria-label='×'>×</button></div><p class='soft'>{t('passport_d', lang)}</p><div class='stamp-meter'><i data-meter></i></div><ul class='stamp-grid' data-stamps></ul><button type='button' class='ghost-btn' data-reset-passport>{t('passport_reset', lang)}</button></dialog>"
                   f"<div class='toast' role='status' aria-live='polite' hidden></div>")
        html = html.replace("</main>", f"<section class='keep' data-keep aria-label='{t('keep', lang)}' hidden></section></main>", 1)
        # data for JS
        stamp_names = {s: c[s]["title"] for s in STAMP_PAGES}
        for k in ("candle", "rosary", "memory", "quiz", "card", "ics"):
            stamp_names["act_" + k] = T["s_" + k][i]
        pages = [{"slug": s, "href": hrefs[s], "title": c[s]["title"], "summary": c[s]["summary"], "ic": ICON[s], "group": GROUP.get(s, "story")} for s in ORDER]
        d = {"lang": lang, "slug": slug, "t": {k: v[i] for k, v in T.items()}, "stamps": stamp_names, "stampOrder": STAMP_PAGES + ["act_" + k for k in ("candle", "rosary", "memory", "quiz", "card", "ics")],
             "pages": pages, "verses": [{"ref": v[0], "text": v[1 + i]} for v in VERSES],
             "feasts": [{"id": f[0], "m": f[1], "d": f[2], "kind": f[3], "name": f[4][i]} for f in FEASTS],
             "moving": [{"id": f[0], "off": f[1], "kind": f[2], "name": f[3][i]} for f in MOVING],
             "saints": {s[0]: {"name": s[2][i], "years": s[1], "text": s[3][i]} for s in SAINTS},
             "quiz": [{"q": q[0][i], "a": q[1][i], "c": q[2], "e": q[3][i]} for q in QUIZ],
             "mys": {k: {"name": v[0][i], "items": [m[i] for m in v[1]]} for k, v in MYSTERIES.items()},
             "memory": [{"img": m[0], "name": m[1 + i]} for m in MEMORY], "assets": pre, "root": up}
        blob = json.dumps(d, ensure_ascii=False).replace("<", "\\u003c")
        html = html.replace("</body>", f"{dialogs}<script id='exp-data' type='application/json'>{blob}</script><script src='{pre}experience.js' defer></script></body>", 1)
        return html
    g["render"] = render
