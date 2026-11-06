# Nicolas Kluiters — A Living Legacy

An independent, static historical archive in Arabic, French, and English. It contains eight pages in each language: home, biography, Barqa, timeline, cause, places of memory, photo archive, and sources. Arabic is the root language; English and French live in `/en/` and `/fr/`.

## Build and preview

The site uses plain HTML and CSS and has no runtime or build dependencies. To regenerate the localized pages after editing the content in `build_site.py`, run `python3 build_site.py` (needs Pillow). Run `python3 check.py` to validate links, anchors, alt text and metadata. Then open `index.html` or serve the repository with a static HTTP server.

## Publishing

For direct publication, set GitHub Pages to “Deploy from a branch”, `main`, `/(root)`. GitHub then publishes the repository root after pushes. The manual `Publish to GitHub Pages` workflow remains available as an alternative; artifact names include the attempt number to make retries unambiguous. The public site is at https://nk.ci-ccg.com/ (custom domain via the `CNAME` file; DNS needs `nk CNAME ccg-cyber.github.io`, then enable “Enforce HTTPS” in Pages settings).

## Research and editorial approach

- Claims are linked to sources near the text and collected on the sources page. The archive uses “mid-1970s” for the start of Barqa ministry because published accounts differ on the year.
- The diocesan inquiry opened in Beirut on 22 January 2022, according to [Jesuits in Europe](https://jesuits.eu/news/1998-beatification-process-dutch-jesuit-started). The site does not claim beatification, canonization, or any later cause stage without an official announcement.
- The [Order of Malta Lebanon](https://orderofmaltalebanon.org/center/barqa-bekaa) says the Barqa community health centre was established in 1985 in his memory. It arose after his death; the archive does not call it a centre he founded.
- The gallery keeps the five supplied project images. It adds nine historical images attributed by [Nidaa Al Watan](https://www.nidaalwatan.com/article/356466-%D8%A7%D9%84%D8%A3%D8%A8-%D8%A7%D9%84%D8%B4%D9%87%D9%8A%D8%AF-%D9%86%D9%8A%D9%83%D9%88%D9%84%D8%A7-%D9%83%D9%84%D9%88%D9%8A%D8%AA%D8%B1%D8%B2-%D8%AD%D9%8A%D9%86-%D8%B5%D8%A7%D8%B1-%D8%A7%D9%84%D9%83%D8%A7%D9%87%D9%86-%D9%88%D8%B7%D9%86%D8%A7-%D9%84%D8%A8%D9%84%D8%AF%D8%A9-%D8%A8%D8%B1%D9%82%D8%A7) to the Barqa Archive, plus one contemporary Barqa centre photograph credited to the Order of Malta Lebanon via L’Orient-Le Jour. Publisher-hosted photos are linked, not copied into this repository. Rights remain with their owners.
- `portrait-restored.jpg` is digitally colorized. `memorial-art.jpg` is contemporary artwork, not a historical photograph. The project images were supplied without photographer or date information.
- The archive did not verify a dedicated official Facebook or Instagram account, a standalone Wikipedia biography, an officially designated sanctuary, or an official transfer of remains to Barqa. These points are described with that uncertainty on the site.

This is an independent project, not an official Jesuit, Order of Malta, or beatification-cause website.

## Interactive experience

The archive now has 11 sections per language (33 pages), including village discovery, prayer and a media room. `premium.py` and `quiz.py` extend the content generator. `assets/site.js` adds search, native sharing with copy fallback, photo filters and an accessible image dialog, a five-question discovery challenge, and a one-minute reflection timer. Optional intentions are stored only in the visitor’s browser on an explicit save action. The site collects no prayer submissions. Community contributions link to public GitHub issues.

Additional village research includes OSAD’s 2008 reservoir account, Anera’s December 2012 Barqa-Rabiaa irrigation report, and Maria Chakhtoura’s September 2010 village feature. Historical project reports are labelled by date.

## Production polish

`polish.py` adds: self-hosted fonts (no third-party requests), a strict Content-Security-Policy and referrer policy, Open Graph/Twitter cards and JSON-LD, favicon/manifest/offline service worker (`sw.js`), a trilingual `404.html`, intrinsic image sizes, a build-time “on this page” list, previous/next navigation, reading progress, back-to-top, a dismissible language suggestion, and print styles. Lighthouse (local, mobile emulation): 100 accessibility, 100 best practices, 100 SEO, 98–100 performance. The `QA` workflow rebuilds the site and runs `check.py` on every push.

## Experience layer

`experience.py` + `experience_data.py` + `assets/experience.{css,js}` add a second design language and new sections in all three languages: **Prayer sanctuary** (virtual candles, interactive Rosary with the four sets of mysteries, prayer library incl. Syriac Aramaic opening of the Our Father, generated ambient tone), **Maronite heritage** (saints, computed feast calendar with `.ics` export), **Play & learn** (archive memory game, 11-question heritage quiz, HD/UHD prayer-card studio), a day/night theme, an app-style bottom tab bar on phones, a local-only “Pilgrim passport” with stamps, “continue where you left off” and personalised “keep exploring”. Everything is stored in the visitor’s browser only. Feast dates and saint facts should be reviewed by a Maronite parish or the Maronite Patriarchate before being treated as authoritative.

## Design system (v3)

`assets/pro.css` is the single design system: Newsreader / Inter (Latin) and Amiri / IBM Plex Sans Arabic, all self-hosted and subset; a Lucide icon sprite (`assets/icons.svg`, ISC licence); arch-shaped hero, pill controls, compact sticky header, bottom tab bar on phones, bottom-sheet popups. The built-in player (`[data-player]`) is a privacy-friendly facade: nothing loads from YouTube until Play, then `youtube-nocookie.com`. Video list lives in `experience_data.py` (`VIDEOS`); every ID was verified embeddable via YouTube oEmbed.

Deploy note: network-first service worker (nk-v4) ships with the glass redesign.
