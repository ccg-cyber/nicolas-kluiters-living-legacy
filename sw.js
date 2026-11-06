'use strict';
// Network-first for everything on this origin so visitors always get the newest design; cache is only an offline fallback.
const VERSION='nk-v5';const CORE=['./','assets/site.css','assets/pro.css','assets/icons.svg','assets/village.svg','assets/site.js','assets/polish.js','assets/experience.js','assets/theme.js','assets/favicon.svg','offline.html'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(VERSION).then(c=>c.addAll(CORE)).then(()=>self.skipWaiting()));});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==VERSION).map(x=>caches.delete(x)))).then(()=>self.clients.claim()));});
self.addEventListener('fetch',e=>{const r=e.request;if(r.method!=='GET')return;const u=new URL(r.url);if(u.origin!==location.origin)return;
e.respondWith(fetch(r,{cache:'no-cache'}).then(res=>{if(res.ok){const copy=res.clone();caches.open(VERSION).then(c=>c.put(r,copy));}return res;}).catch(()=>caches.match(r).then(m=>m||(r.mode==='navigate'?caches.match('offline.html'):Response.error()))));});
