'use strict';
(()=>{
const P=JSON.parse(document.querySelector('#polish-data').textContent);
const root=document.documentElement,rtl=root.dir==='rtl';
// Offline support
if('serviceWorker' in navigator&&location.protocol==='https:'){addEventListener('load',()=>navigator.serviceWorker.register(P.sw).catch(()=>{}));}
const badge=document.createElement('div');badge.className='offline-badge';badge.hidden=true;badge.setAttribute('role','status');badge.textContent=P.t.offline;document.body.append(badge);
const net=()=>{badge.hidden=navigator.onLine;};addEventListener('online',net);addEventListener('offline',net);net();
// Reading progress
const bar=document.createElement('div');bar.className='read-progress';bar.setAttribute('aria-hidden','true');bar.append(document.createElement('i'));document.body.prepend(bar);
const top=document.createElement('button');top.className='to-top';top.type='button';top.textContent='↑';top.setAttribute('aria-label',P.t.top);document.body.append(top);
const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
top.onclick=()=>scrollTo({top:0,behavior:reduce?'auto':'smooth'});
let tick=false;function onScroll(){if(tick)return;tick=true;requestAnimationFrame(()=>{tick=false;const h=root.scrollHeight-innerHeight,p=h>0?Math.min(1,scrollY/h):0;bar.style.setProperty('--p',p.toFixed(4));top.classList.toggle('show',scrollY>700);});}
addEventListener('scroll',onScroll,{passive:true});onScroll();
// Scroll-spy for the build-time contents list
const toc=document.querySelector('.toc');
if(toc&&'IntersectionObserver' in window){const links=[...toc.querySelectorAll('a')],map=new Map(links.map(l=>[l.getAttribute('href').slice(1),l]));const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){links.forEach(l=>l.removeAttribute('aria-current'));map.get(e.target.id)?.setAttribute('aria-current','true');}}),{rootMargin:'0px 0px -70% 0px'});map.forEach((_,id)=>{const h=document.getElementById(id);if(h)io.observe(h);});}
// Suggest the visitor's language once, never redirect automatically
try{const pref=(navigator.language||'').slice(0,2).toLowerCase();const cur=root.lang;const hint=P.hints[pref];
if(hint&&pref!==cur&&!localStorage.getItem('nk-lang-dismissed')){const d=document.createElement('div');d.className='lang-hint';d.setAttribute('role','region');d.setAttribute('aria-label','Language');d.lang=pref;d.dir=pref==='ar'?'rtl':'ltr';
const a=document.createElement('a');a.href=P.links[pref];a.hreflang=pref;a.textContent=hint;const x=document.createElement('button');x.type='button';x.textContent='×';x.setAttribute('aria-label','Dismiss');x.onclick=()=>{d.remove();try{localStorage.setItem('nk-lang-dismissed','1');}catch{}};d.append(a,x);document.body.append(d);}}catch{}
// Escape closes mobile nav
addEventListener('keydown',e=>{if(e.key==='Escape'){const h=document.querySelector('.site-header.nav-open');if(h){h.classList.remove('nav-open');const b=h.querySelector('.menu-toggle');b.setAttribute('aria-expanded','false');b.focus();}}});
})();
