"""Experience layer: new pages (prayer sanctuary, Maronite heritage, play), redesigned home,
app-like navigation, pilgrim passport, themes and personalised retention features."""
import json
from html import escape
from experience_data import *

IDX = {"ar": 0, "en": 1, "fr": 2}
ICON = {"index": "house", "pray": "flame", "heritage": "church", "play": "gamepad-2", "discover": "map-pin", "life": "book-open", "barqa": "mountain", "timeline": "clock", "cause": "award", "places": "landmark", "archive": "images", "media": "tv", "prayer": "sparkles", "sources": "scroll-text"}
GROUP = {"pray": "faith", "heritage": "faith", "prayer": "faith", "cause": "faith", "play": "play", "media": "play", "archive": "play", "discover": "story", "life": "story", "barqa": "story", "timeline": "story", "places": "story", "sources": "story"}
SECTION = {"life": "life", "barqa": "life", "timeline": "life", "cause": "life", "places": "life", "archive": "life", "sources": "life", "discover": "life", "prayer": "pray"}
ORDER = ["index", "life", "pray", "heritage", "media", "play", "discover", "barqa", "timeline", "cause", "places", "archive", "prayer", "sources"]
STAMP_PAGES = ["life", "barqa", "timeline", "cause", "places", "archive", "sources", "discover", "prayer", "media", "pray", "heritage", "play"]
ACTS = ("candle", "rosary", "memory", "quiz", "card", "ics", "watch")

def t(k, lang): return T[k][IDX[lang]]


def I(n): return f"[[i:{n}]]"

def tiles(lang, hrefs):
    items = [("pray", "tile_candle", "flame", "#candle"), ("pray", "tile_rosary", "heart", "#rosary"),
             ("heritage", "tile_saints", "church", "#saints"), ("heritage", "tile_feasts", "calendar-days", "#feasts"),
             ("play", "tile_play", "layers", "#memory"), ("play", "tile_quiz", "brain", "#quiz")]
    return "".join(f"<a class='qa' href='{hrefs[p]}{a}'><span class='qa-ic'>{I(ic)}</span><span class='qa-t'><strong>{t(k, lang)}</strong><small>{t(k + '_d', lang)}</small></span></a>" for p, k, ic, a in items)

def home_body(lang, hrefs):
    v = VIDEOS[0]
    return f"""<section class='qa-row' aria-label='{t('h_q', lang)}'>{tiles(lang, hrefs)}</section>
<section class='today-panel' data-today aria-label='{t('today', lang)}'></section>
<section class='band'><div class='band-head'><h2>{t('h_featured', lang)}</h2><a class='more' href='{hrefs['media']}'>{t('h_more_watch', lang)} {I('arrow-right')}</a></div>
<div class='player-wrap' data-player data-limit='5'></div></section>
<section class='band story-trio'><div class='band-head'><h2>{t('h_explore', lang)}</h2></div><div class='trio'>
<a class='card-link' href='{hrefs['life']}'><span class='ci'>{I('book-open')}</span><strong>{escape(g_title(lang, 'life'))}</strong><small>{t('h_story_p', lang)}</small><span class='go'>{I('arrow-right')}</span></a>
<a class='card-link' href='{hrefs['barqa']}'><span class='ci'>{I('mountain')}</span><strong>{escape(g_title(lang, 'barqa'))}</strong><small>{escape(g_sum(lang, 'barqa'))}</small><span class='go'>{I('arrow-right')}</span></a>
<a class='card-link' href='{hrefs['cause']}'><span class='ci'>{I('award')}</span><strong>{escape(g_title(lang, 'cause'))}</strong><small>{escape(g_sum(lang, 'cause'))}</small><span class='go'>{I('arrow-right')}</span></a></div></section>
<section class='continue-panel' data-continue hidden></section>
<section class='journey-bar' data-journey aria-live='polite'></section>"""

_G = {}
def g_title(lang, slug): return _G["CONTENT"][lang][slug]["title"]
def g_sum(lang, slug): return _G["CONTENT"][lang][slug]["summary"]

def candle_html(lang):
    return f"""<section id='candle' class='sanct-block candle-block'>
<div class='sanct-head'><p class='eyebrow'>01</p><h2>{t('p_candle_h', lang)}</h2><p>{t('p_candle_p', lang)}</p></div>
<div class='candle-stage'><div class='hero-candle' aria-hidden='true'><i class='halo'></i><i class='flame'></i><b class='wick'></b><span class='wax'></span></div>
<div class='candle-form'><label for='candle-note'>{t('p_intention', lang)}</label><textarea id='candle-note' maxlength='140' rows='2'></textarea>
<div class='cta-row'><button id='candle-light' class='btn primary' type='button'>{I('flame')} {t('p_light', lang)}</button><button id='candle-out' class='btn ghost' type='button'>{t('p_extinguish', lang)}</button></div>
<p id='candle-count' class='soft' aria-live='polite'></p></div></div>
<ul id='candle-row' class='candle-row' aria-label='{t('p_candle_h', lang)}'></ul></section>"""

def rosary_html(lang):
    return f"""<section id='rosary' class='sanct-block'>
<div class='sanct-head'><p class='eyebrow'>02</p><h2>{t('p_rosary_h', lang)}</h2><p>{t('p_rosary_p', lang)}</p></div>
<div class='rosary-card' data-rosary><div class='mys-tabs' role='tablist' aria-label='{t('p_mys_today', lang)}'></div>
<div class='rosary-main'><p class='rosary-decade' aria-live='polite'></p><h3 class='rosary-mystery'></h3>
<ol class='beads' aria-hidden='true'></ol><p class='rosary-bead soft'></p>
<div class='cta-row center'><button class='btn primary lg' data-hail type='button'>{t('p_hail', lang)}</button><button class='btn ghost' data-undo type='button'>{I('undo-2')} {t('p_undo', lang)}</button><button class='btn ghost' data-restart type='button'>{I('rotate-ccw')} {t('p_restart', lang)}</button></div>
<p class='rosary-done' role='status'></p></div></div></section>"""

def syr(lang):
    return f"<div class='syriac-note'><p>{t('p_syr_note', lang)}</p><p class='syriac' lang='syr' dir='rtl'>ܐܒܘܢ ܕܒܫܡܝܐ ܢܬܩܕܫ ܫܡܟ</p><p class='soft'>{t('p_syr_tr', lang)}</p></div>"

def library_html(lang):
    ids = [("cross", "p_cross", "cross_t"), ("our", "p_our", "our_t"), ("hail", "p_hailmary", "hail_t"), ("glory", "p_glory", "glory_t")]
    det = "".join(f"<details class='prayer-item'{' open' if i == 1 else ''}><summary>{t(h, lang)}{I('chevron-down')}</summary><p class='prayer-text'>{t(tx, lang)}</p>{syr(lang) if i == 1 else ''}</details>" for i, (_, h, tx) in enumerate(ids))
    return f"""<section id='library' class='sanct-block'><div class='sanct-head'><p class='eyebrow'>03</p><h2>{t('p_lib_h', lang)}</h2><p>{t('p_lib_p', lang)}</p></div>
<div class='prayer-list'>{det}</div>
<div class='ambient-card'><div><h3>{t('p_ambient', lang)}</h3><p class='soft'>{t('p_ambient_p', lang)}</p></div><button id='ambient' class='btn gold' type='button' aria-pressed='false' data-on='{t('p_ambient_on', lang)}' data-off='{t('p_ambient_off', lang)}'>{I('volume-2')} <span>{t('p_ambient_off', lang)}</span></button></div>
<button class='btn ghost' data-print type='button'>{I('printer')} {t('p_print', lang)}</button></section>"""

def pray_body(lang):
    return "<div data-today class='today-panel compact'></div>" + candle_html(lang) + rosary_html(lang) + library_html(lang)

def heritage_body(lang):
    facts = "".join(f"<div><dt>{t(a, lang)}</dt><dd>{t(b, lang)}</dd></div>" for a, b in [("he_f1", "he_f1v"), ("he_f2", "he_f2v"), ("he_f3", "he_f3v"), ("he_f4", "he_f4v"), ("he_f5", "he_f5v")])
    i = IDX[lang]
    saints = "".join(f"<button class='saint-card' type='button' data-saint='{s[0]}'><span class='saint-years'>{s[1]}</span><strong>{s[2][i]}</strong><span class='text-link'>{t('he_read', lang)} {I('arrow-right')}</span></button>" for s in SAINTS)
    chips = "".join(f"<button type='button' data-filter='{k}' aria-pressed='{'true' if k == 'all' else 'false'}'>{t(l, lang)}</button>" for k, l in [("all", "he_all"), ("saint", "he_saintsf"), ("marian", "he_marian"), ("lord", "he_lord"), ("nk", "he_nk")])
    return f"""<section class='sanct-block'><div class='sanct-head'><p class='eyebrow'>01</p><h2>{t('he_intro_h', lang)}</h2><p>{t('he_intro_p', lang)}</p></div>
<dl class='fact-strip'>{facts}</dl><p class='editorial-note'>{t('he_nk_p', lang)}</p></section>
<section id='saints' class='sanct-block'><div class='sanct-head'><p class='eyebrow'>02</p><h2>{t('he_saints_h', lang)}</h2><p>{t('he_saints_p', lang)}</p></div><div class='saint-grid'>{saints}</div>
<dialog id='saint-dialog'><div class='dialog-top'><strong id='saint-name'></strong><button type='button' class='icon-btn' data-close-saint aria-label='×'>{I('x')}</button></div><p id='saint-years' class='eyebrow'></p><p id='saint-text'></p></dialog></section>
<section id='feasts' class='sanct-block'><div class='sanct-head'><p class='eyebrow'>03</p><h2>{t('he_feasts_h', lang)}</h2><p>{t('he_feasts_p', lang)}</p></div>
<div class='next-feast' data-next-feast aria-live='polite'></div>
<div class='chip-row' role='group'>{chips}</div><ol class='feast-list' data-feasts></ol>
<button id='ics' class='btn primary' type='button'>{I('calendar-days')} {t('he_ics', lang)}</button></section>"""

def play_body(lang):
    return f"""<section id='memory' class='sanct-block'><div class='sanct-head'><p class='eyebrow'>01</p><h2>{t('pl_mem_h', lang)}</h2><p>{t('pl_mem_p', lang)}</p></div>
<div class='game-bar'><span>{t('pl_moves', lang)}: <b id='mem-moves'>0</b></span><span>{t('pl_time', lang)}: <b id='mem-time'>0</b>s</span><span>{t('pl_best', lang)}: <b id='mem-best'>–</b></span><button id='mem-new' class='btn ghost sm' type='button'>{I('rotate-ccw')} {t('pl_new', lang)}</button></div>
<div id='mem-grid' class='mem-grid'></div><p id='mem-msg' class='win-msg' role='status'></p></section>
<section id='quiz' class='sanct-block'><div class='sanct-head'><p class='eyebrow'>02</p><h2>{t('pl_quiz_h', lang)}</h2><p>{t('pl_quiz_p', lang)}</p></div>
<div id='quiz2' class='quiz2'><button id='quiz2-start' class='btn primary' type='button'>{I('play')} {t('pl_start', lang)}</button></div></section>
<section id='cards' class='sanct-block'><div class='sanct-head'><p class='eyebrow'>03</p><h2>{t('pl_card_h', lang)}</h2><p>{t('pl_card_p', lang)}</p></div>
<div class='studio'><div class='studio-preview'><canvas id='card-canvas' width='1080' height='1350' role='img' aria-label='{t('pl_preview', lang)}'></canvas></div>
<div class='studio-controls'><label for='card-verse'>{t('pl_verse', lang)}</label><select id='card-verse'></select>
<fieldset><legend>{t('pl_bg', lang)}</legend><div class='chip-row'><button type='button' data-bg='0' aria-pressed='true'>{t('pl_bg1', lang)}</button><button type='button' data-bg='1' aria-pressed='false'>{t('pl_bg2', lang)}</button><button type='button' data-bg='2' aria-pressed='false'>{t('pl_bg3', lang)}</button></div></fieldset>
<fieldset><legend>{t('pl_res', lang)}</legend><div class='chip-row'><button type='button' data-res='1' aria-pressed='true'>{t('pl_hd', lang)}</button><button type='button' data-res='2' aria-pressed='false'>{t('pl_uhd', lang)}</button></div></fieldset>
<div class='cta-row'><button id='card-dl' class='btn primary' type='button'>{I('download')} {t('pl_dl', lang)}</button><button id='card-share' class='btn ghost' type='button'>{I('share-2')} {t('pl_share', lang)}</button></div></div></div></section>"""

def watch_body(lang, old):
    chans = [("https://www.youtube.com/channel/UCT3l7eP2alTz4TTGH6yqFTQ", "v_noursat", "radio"), ("https://www.youtube.com/channel/UC7_ilEmKzDPBnRXgHdoVaNQ", "v_harissa", "church"), ("https://www.youtube.com/channel/UC8dLY8SjW9Psf1OanD5ZHMQ", "v_omalta", "heart")]
    cards = "".join(f"<a class='card-link' href='{u}' target='_blank' rel='noopener noreferrer'><span class='ci'>{I(ic)}</span><strong>{t(k, lang)}</strong><span class='go'>{I('external-link')}</span></a>" for u, k, ic in chans)
    return f"""<div class='player-wrap' data-player data-full></div><p class='soft note'>{I('shield-check')} {t('v_note', lang)}</p>
<section class='band'><div class='band-head'><h2>{t('v_channels', lang)}</h2></div><p class='soft'>{t('v_channels_p', lang)}</p><div class='trio'>{cards}</div></section>{old}"""

def welcome_html(lang, hrefs):
    return f"""<dialog id='welcome-dialog' class='sheet'><div class='dialog-top'><strong>{t('w_h', lang)}</strong><button type='button' class='icon-btn' data-close-welcome aria-label='×'>{I('x')}</button></div><p class='soft'>{t('w_p', lang)}</p>
<div class='welcome-grid'><button type='button' class='card-link' data-watch='{VIDEOS[0][0]}' data-close-welcome><span class='ci'>{I('play')}</span><strong>{t('w_1', lang)}</strong><small>{t('w_1d', lang)}</small></button>
<a class='card-link' href='{hrefs['life']}'><span class='ci'>{I('book-open')}</span><strong>{t('w_2', lang)}</strong><small>{t('w_2d', lang)}</small></a>
<a class='card-link' href='{hrefs['pray']}'><span class='ci'>{I('flame')}</span><strong>{t('w_3', lang)}</strong><small>{t('w_3d', lang)}</small></a></div>
<button type='button' class='btn ghost sm' data-close-welcome>{t('w_skip', lang)}</button></dialog>"""

def hero_html(lang, hrefs, data):
    return f"""<section class='hero' data-hero><div class='hero-copy'><span class='pill'>{I('cross')} {t('h_kicker', lang)}</span><h1>{escape(data['title'])}</h1><p class='lead'>{escape(data['summary'])}</p>
<div class='cta-row'><button class='btn primary lg' type='button' data-watch='{VIDEOS[0][0]}'>{I('play')} {t('h_watch_film', lang)}</button><a class='btn ghost lg' href='{hrefs['pray']}#candle'>{I('flame')} {t('h_cta1', lang)}</a></div>
<ul class='hero-facts'><li><b>1940</b><span>{t('h_fact1', lang)}</span></li><li><b>1966</b><span>{t('h_fact2', lang)}</span></li><li><b>1973</b><span>{t('h_fact3', lang)}</span></li></ul></div>
<div class='hero-art'><div class='arch'><img src='ASSET_PREFIXportrait-restored-1536.webp' alt='{t('h_alt', lang)}' fetchpriority='high'></div><span class='arch-chip'>1940 – 1985</span></div></section>"""

def install(g):
    _G.update(g)
    LOC = g["LOCALES"]
    for lang in LOC:
        i = IDX[lang]
        labels = dict(zip(g["PAGES"], g["NAV"][lang]))
        labels.update({"pray": T["pray"][i], "heritage": T["heritage"][i], "play": T["play"][i], "media": T["watch"][i]})
        c = g["CONTENT"][lang]
        c["pray"] = {"eyebrow": T["eyebrow_pray"][i], "title": T["pray"][i], "summary": T["pray_sum"][i], "body": pray_body(lang)}
        c["heritage"] = {"eyebrow": T["eyebrow_heritage"][i], "title": T["heritage"][i], "summary": T["heritage_sum"][i], "body": heritage_body(lang)}
        c["play"] = {"eyebrow": T["eyebrow_play"][i], "title": T["play"][i], "summary": T["play_sum"][i], "body": play_body(lang)}
        hrefs = {s: ("index.html" if s == "index" else s + ".html") for s in ORDER}
        c["index"]["body"] = home_body(lang, hrefs)
        c["media"]["body"] = watch_body(lang, c["media"]["body"]); c["media"]["title"] = T["watch"][i]; c["media"]["summary"] = T["watch_sum"][i]; c["media"]["eyebrow"] = T["eyebrow_watch"][i]
        g["NAV"][lang][:] = [labels[s] for s in ORDER]
    g["PAGES"] = tuple(ORDER)
    original = g["render"]

    def render(lang, slug):
        import re
        html = original(lang, slug)
        i = IDX[lang]; up = "" if lang == "ar" else "../"; pre = "assets/" if lang == "ar" else "../assets/"
        hrefs = {s: ("index.html" if s == "index" else s + ".html") for s in ORDER}
        c = g["CONTENT"][lang]; TX = g["TEXT"][lang]
        html = html.replace("ASSET_PREFIX", pre)
        html = html.replace("<link rel='stylesheet' href='%spolish.css'>" % pre, "<link rel='stylesheet' href='%spro.css'><script src='%stheme.js'></script>" % (pre, pre), 1)
        html = html.replace("<meta name='color-scheme' content='light'>", "<meta name='color-scheme' content='light dark'>")
        # ---- header (single compact bar)
        langs = re.search(r"<div class='language-switch'[^>]*>(.*?)</div>", html, re.S).group(1)
        sect = SECTION.get(slug, slug)
        prim = [("life", "story"), ("pray", "pray"), ("heritage", "heritage"), ("media", "watch"), ("play", "play")]
        nav = "".join(f"<a href='{hrefs[s]}'{' aria-current=page' if sect == s else ''}>{t(k, lang) if k != 'story' else T['story'][i]}</a>" for s, k in prim)
        header = (f"<header class='site-header'><div class='bar'><a class='brand' href='{hrefs['index']}' aria-label='{escape(TX['site'], quote=True)}'><svg class='mark' viewBox='0 0 32 32' aria-hidden='true'><path d='M4 30V14a12 12 0 0 1 24 0v16z' fill='currentColor'/><path d='M16 8v15M10.5 13.5h11' stroke='#E9C77A' stroke-width='2.2' stroke-linecap='round'/></svg><span class='brand-text'><strong>{TX['site']}</strong><small>{TX['tagline']}</small></span></a>"
                  f"<nav class='primary' aria-label='{escape(TX['menu'], quote=True)}'>{nav}<button type='button' data-open-menu>{t('explore_all', lang)} {I('chevron-down')}</button></nav>"
                  f"<div class='bar-actions'><button type='button' class='icon-btn' data-open-search aria-label='{escape(t('search_hint', lang), quote=True)}' title='{escape(t('search_hint', lang), quote=True)}'>{I('search')}</button>"
                  f"<button type='button' class='icon-btn' data-theme-toggle aria-pressed='false' data-night='{t('theme_dark', lang)}' data-day='{t('theme_light', lang)}'><span class='ic-moon'>{I('moon')}</span><span class='ic-sun'>{I('sun')}</span><span class='sr'>{t('theme_dark', lang)}</span></button>"
                  f"<button type='button' class='icon-btn passport-chip' data-open-passport>{I('stamp')}<b data-passport-count>0</b><span class='sr'>{t('passport', lang)}</span></button>"
                  f"<div class='language-switch' role='group' aria-label='{escape(TX['langname'], quote=True)}'>{langs}</div></div></div>"
                  f"<button class='menu-toggle' aria-expanded='false' aria-controls='primary-navigation' hidden>x</button><span id='primary-navigation' hidden></span></header>")
        html = re.sub(r"<header class='site-header'>.*?</header>", lambda m: header, html, count=1, flags=re.S)
        html = re.sub(r"<div class='page-tools[^']*'>.*?</div>", "", html, count=1, flags=re.S)
        html = html.replace("<footer class='site-footer'>", "<span class='share-status sr' role='status'></span><footer class='site-footer'>", 1)
        # ---- home hero
        if slug == "index":
            hero = hero_html(lang, hrefs, c["index"]).replace("ASSET_PREFIX", pre)
            html = re.sub(r"<section class='page-hero home-hero'>.*?</section>", lambda m: hero, html, count=1, flags=re.S)
            html = re.sub(r"<section class='discovery-game'>.*?</section>", "", html, count=1, flags=re.S)
        # ---- tab bar, dialogs, keep exploring
        tabs = [("index", "tab_home", "house"), ("media", "tab_watch", "tv"), ("pray", "tab_pray", "flame"), ("play", "tab_play", "gamepad-2")]
        tab = "".join(f"<a href='{hrefs[s]}'{' aria-current=page' if s == slug else ''}>{I(ic)}<span>{t(k, lang)}</span></a>" for s, k, ic in tabs)
        tab += f"<button type='button' data-open-menu>{I('layout-grid')}<span>{t('tab_more', lang)}</span></button>"
        groups = [("story", ["life", "barqa", "timeline", "places", "archive", "discover", "sources"]), ("faith", ["pray", "heritage", "cause", "prayer"]), ("play", ["media", "play"])]
        gl = {"story": T["story"][i], "faith": {"ar": "إيمان", "en": "Faith", "fr": "Foi"}[lang], "play": {"ar": "شاهد والعب", "en": "Watch & play", "fr": "Voir et jouer"}[lang]}
        menu = "".join(f"<h3 class='menu-h'>{gl[gk]}</h3><div class='menu-grid'>" + "".join(f"<a class='menu-item' href='{hrefs[s]}'{' aria-current=page' if s == slug else ''}><span class='mi-ic'>{I(ICON[s])}</span><span><strong>{escape(c[s]['title'])}</strong><small>{escape(c[s]['summary'])}</small></span></a>" for s in items) + "</div>" for gk, items in groups)
        dialogs = (f"<nav class='tabbar' aria-label='{t('tab_more', lang)}'>{tab}</nav>"
                   f"<dialog id='menu-dialog' class='sheet'><div class='dialog-top'><strong>{t('explore_all', lang)}</strong><button type='button' class='icon-btn' data-close-menu aria-label='×'>{I('x')}</button></div>{menu}</dialog>"
                   f"<dialog id='passport-dialog' class='sheet'><div class='dialog-top'><strong>{I('stamp')} {t('passport', lang)}</strong><button type='button' class='icon-btn' data-close-passport aria-label='×'>{I('x')}</button></div><p class='soft'>{t('passport_d', lang)}</p><div class='stamp-meter'><i data-meter></i></div><ul class='stamp-grid' data-stamps></ul><button type='button' class='btn ghost sm' data-reset-passport>{t('passport_reset', lang)}</button></dialog>"
                   f"<dialog id='video-dialog' class='theater'><div class='dialog-top'><strong data-vtitle></strong><button type='button' class='icon-btn' data-close-video aria-label='×'>{I('x')}</button></div><div class='theater-frame' data-vframe></div><div class='theater-bar'><button type='button' class='btn ghost sm' data-vprev>{I('skip-back')} {t('v_prev', lang)}</button><button type='button' class='btn ghost sm' data-vnext>{t('v_next', lang)} {I('skip-forward')}</button><a class='btn ghost sm' data-vyt href='https://www.youtube.com/' target='_blank' rel='noopener noreferrer'>{t('v_yt', lang)} {I('external-link')}</a></div></dialog>"
                   + (welcome_html(lang, hrefs) if slug == "index" else "") +
                   "<div class='toast' role='status' aria-live='polite' hidden></div>")
        html = html.replace("</main>", f"<section class='keep' data-keep aria-label='{t('keep', lang)}' hidden></section></main>", 1)
        stamp_names = {s: c[s]["title"] for s in STAMP_PAGES}
        for k in ACTS: stamp_names["act_" + k] = T["s_" + k][i]
        pages = [{"slug": s, "href": hrefs[s], "title": c[s]["title"], "summary": c[s]["summary"], "ic": ICON[s], "group": GROUP.get(s, "story")} for s in ORDER]
        d = {"lang": lang, "slug": slug, "t": {k: v[i] for k, v in T.items()}, "stamps": stamp_names, "stampOrder": STAMP_PAGES + ["act_" + k for k in ACTS],
             "pages": pages, "verses": [{"ref": v[0], "text": v[1 + i]} for v in VERSES],
             "feasts": [{"id": f[0], "m": f[1], "d": f[2], "kind": f[3], "name": f[4][i]} for f in FEASTS],
             "moving": [{"id": f[0], "off": f[1], "kind": f[2], "name": f[3][i]} for f in MOVING],
             "saints": {s[0]: {"name": s[2][i], "years": s[1], "text": s[3][i]} for s in SAINTS},
             "quiz": [{"q": q[0][i], "a": q[1][i], "c": q[2], "e": q[3][i]} for q in QUIZ],
             "mys": {k: {"name": v[0][i], "items": [m[i] for m in v[1]]} for k, v in MYSTERIES.items()},
             "memory": [{"img": m[0], "name": m[1 + i]} for m in MEMORY], "assets": pre, "root": up,
             "videos": [{"id": v[0], "cat": v[1], "title": v[2], "by": v[3], "dur": v[4]} for v in VIDEOS]}
        blob = json.dumps(d, ensure_ascii=False).replace("<", "\\u003c")
        html = html.replace("</body>", f"{dialogs}<script id='exp-data' type='application/json'>{blob}</script><script src='{pre}experience.js' defer></script></body>", 1)
        html = re.sub(r"\[\[i:([\w-]+)\]\]", lambda m: f"<svg class='ic{' flip' if m.group(1) in ('arrow-right','chevron-right','skip-forward','skip-back','undo-2','arrow-left') else ''}' aria-hidden='true' focusable='false'><use href='{pre}icons.svg#i-{m.group(1)}'/></svg>", html)
        return html
    g["render"] = render
