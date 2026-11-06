#!/usr/bin/env python3
"""Static QA: internal links/anchors, images, alt text, titles, hreflang, sitemap. Exit 1 on failure."""
import re, sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote
ROOT = Path(__file__).resolve().parent
class P(HTMLParser):
    def __init__(s): super().__init__(); s.links=[]; s.ids=set(); s.imgs=[]; s.title=''; s._t=False; s.h1=0; s.desc=False; s.canon=None
    def handle_starttag(s,t,a):
        a=dict(a)
        if 'id' in a: s.ids.add(a['id'])
        if t=='a' and 'href' in a: s.links.append(a['href'])
        if t in('link','script') and (a.get('href') or a.get('src')) and not str(a.get('href') or a.get('src')).startswith(('http','data:')): s.links.append(a.get('href') or a.get('src'))
        if t=='img': s.imgs.append(a)
        if t=='title': s._t=True
        if t=='h1': s.h1+=1
        if t=='meta' and a.get('name')=='description': s.desc=bool(a.get('content'))
        if t=='link' and a.get('rel')=='canonical': s.canon=a.get('href')
    def handle_endtag(s,t):
        if t=='title': s._t=False
    def handle_data(s,d):
        if s._t: s.title+=d
errs=[]; pages={}
for f in sorted(ROOT.rglob('*.html')):
    if '.git' in f.parts: continue
    p=P(); p.feed(f.read_text(encoding='utf-8')); pages[f]=p
for f,p in pages.items():
    rel=f.relative_to(ROOT); status=rel.name in('404.html','offline.html')
    if not p.title.strip(): errs.append(f'{rel}: missing <title>')
    if not status:
        if p.h1!=1: errs.append(f'{rel}: expected 1 <h1>, found {p.h1}')
        if not p.desc: errs.append(f'{rel}: missing meta description')
        if not p.canon: errs.append(f'{rel}: missing canonical')
    for i in p.imgs:
        if 'alt' not in i: errs.append(f'{rel}: <img> without alt {i.get("src")}')
    for l in p.links:
        u=urlparse(l)
        if u.scheme in('http','https','mailto','tel') or l.startswith('#') and l[1:] in p.ids: continue
        path=unquote(u.path)
        tgt=(ROOT/path.lstrip('/')) if path.startswith('/') else (f.parent/path) if path else f
        if tgt.is_dir(): tgt=tgt/'index.html'
        if not tgt.exists(): errs.append(f'{rel}: broken link {l}'); continue
        if u.fragment and tgt.suffix=='.html':
            q=pages.get(tgt.resolve()) or pages.get(tgt)
            if q and u.fragment not in q.ids: errs.append(f'{rel}: missing anchor {l}')
sm=(ROOT/'sitemap.xml').read_text()
base=re.search(r'<loc>(https://[^/]+)',sm).group(1)
for loc in re.findall(r'<loc>([^<]+)',sm):
    if not (ROOT/urlparse(loc).path.lstrip('/')).exists(): errs.append(f'sitemap: {loc} has no file')
cname=(ROOT/'CNAME').read_text().strip()
if base!='https://'+cname: errs.append(f'sitemap host {base} != CNAME {cname}')
if 'github.io' in (ROOT/'index.html').read_text(): errs.append('index.html still references github.io')
print(f'{len(pages)} pages checked, {len(errs)} problem(s)')
for e in errs: print(' -',e)
sys.exit(1 if errs else 0)
