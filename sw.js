'use strict';
const VERSION='nk-v1';const CORE=['./','assets/site.css','assets/polish.css','assets/site.js','assets/polish.js','assets/favicon.svg','offline.html'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(VERSION).then(c=>c.addAll(CORE)).then(()=>self.skipWaiting()));});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==VERSION).map(x=>caches.delete(x)))).then(()=>self.clients.claim()));});
self.addEventListener('fetch',e=>{const r=e.request;if(r.method!=='GET')return;const u=new URL(r.url);if(u.origin!==location.origin)return;
if(r.mode==='navigate'){e.respondWith(fetch(r).then(res=>{const copy=res.clone();caches.open(VERSION).then(c=>c.put(r,copy));return res;}).catch(()=>caches.match(r).then(m=>m||caches.match('offline.html'))));return;}
e.respondWith(caches.match(r).then(m=>m||fetch(r).then(res=>{if(res.ok){const copy=res.clone();caches.open(VERSION).then(c=>c.put(r,copy));}return res;})));});
