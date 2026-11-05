# Nicolas Kluiters — A Living Legacy

An independent, static historical archive in Arabic, French, and English. It contains eight pages in each language: home, biography, Barqa, timeline, cause, places of memory, photo archive, and sources. Arabic is the root language; English and French live in `/en/` and `/fr/`.

## Build and preview

The site uses plain HTML and CSS and has no runtime or build dependencies. To regenerate the localized pages after editing the content in `build_site.py`, run `python3 build_site.py`. Then open `index.html` or serve the repository with a static HTTP server.

## Publishing

The `Publish to GitHub Pages` workflow publishes the repository root on every push to `main`. The public site is at https://ccg-cyber.github.io/nicolas-kluiters-living-legacy/.

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
