'use strict';
(()=>{
const D=JSON.parse(document.querySelector('#exp-data').textContent),T=D.t,$=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const store={get(k,f){try{const v=localStorage.getItem('nk-'+k);return v===null?f:JSON.parse(v);}catch{return f;}},set(k,v){try{localStorage.setItem('nk-'+k,JSON.stringify(v));}catch{}},del(k){try{localStorage.removeItem('nk-'+k);}catch{}}};
const fmt=(s,o)=>s.replace(/\{(\w+)\}/g,(_,k)=>o[k]);
const el=(tag,props={},...kids)=>{const e=document.createElement(tag);for(const[k,v]of Object.entries(props)){if(k==='class')e.className=v;else if(k==='text')e.textContent=v;else if(k.startsWith('on'))e.addEventListener(k.slice(2),v);else e.setAttribute(k,v);}e.append(...kids);return e;};
const ico=n=>{const s=document.createElementNS('http://www.w3.org/2000/svg','svg');s.setAttribute('class','ic');s.setAttribute('aria-hidden','true');const u=document.createElementNS('http://www.w3.org/2000/svg','use');u.setAttribute('href',D.assets+'icons.svg#i-'+n);s.append(u);return s;};
const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
const dayOfYear=d=>Math.floor((d-new Date(d.getFullYear(),0,0))/864e5);
const startOfDay=d=>new Date(d.getFullYear(),d.getMonth(),d.getDate());

/* ---------- toast + passport ---------- */
const toastEl=$('.toast');let toastT;
function toast(msg){toastEl.textContent=msg;toastEl.hidden=false;clearTimeout(toastT);toastT=setTimeout(()=>toastEl.hidden=true,3500);}
const stampsAll=D.stampOrder;
function stamps(){return store.get('stamps',[]);}
function award(id){const s=stamps();if(s.includes(id))return;s.push(id);store.set('stamps',s);toast(fmt(T.stamp_new,{s:D.stamps[id]}));renderPassport();if(s.length===stampsAll.length)setTimeout(()=>toast(T.complete),3800);}
function renderPassport(){const s=stamps();$$('[data-passport-count]').forEach(e=>e.textContent=s.length);const m=$('[data-meter]');if(m)m.style.setProperty('--p',(s.length/stampsAll.length).toFixed(3));
const g=$('[data-stamps]');if(g){g.replaceChildren(...stampsAll.map(id=>el('li',{class:s.includes(id)?'got':''},ico(s.includes(id)?'check':'circle'),el('span',{text:D.stamps[id]}))));}
const j=$('[data-journey]');if(j){j.replaceChildren(el('div',{class:'journey-meter'},el('i')),el('p',{text:fmt(T.h_stats,{a:s.length,b:stampsAll.length})}),el('button',{class:'btn ghost sm',type:'button',text:T.passport,onclick:()=>$('#passport-dialog').showModal()}));const i=$('i',j);i.style.setProperty('--p',(s.length/stampsAll.length).toFixed(3));}}
if(D.stampOrder.includes(D.slug))award(D.slug);
store.set('last',{slug:D.slug,t:Date.now()});
const pd=$('#passport-dialog');$$('[data-open-passport]').forEach(b=>b.onclick=()=>{renderPassport();pd.showModal();});$('[data-close-passport]').onclick=()=>pd.close();$('[data-reset-passport]').onclick=()=>{store.del('stamps');renderPassport();};
const md=$('#menu-dialog');$$('[data-open-menu]').forEach(b=>b.onclick=()=>md.showModal());$('[data-close-menu]').onclick=()=>md.close();
[pd,md,$('#saint-dialog')].filter(Boolean).forEach(d=>d.addEventListener('click',e=>{if(e.target===d)d.close();}));
renderPassport();
window.NK={award};

/* ---------- theme ---------- */
const tt=$('[data-theme-toggle]');function themeUI(){const dark=document.documentElement.getAttribute('data-theme')==='dark';tt.setAttribute('aria-pressed',String(dark));tt.querySelector('.sr').textContent=dark?tt.dataset.day:tt.dataset.night;}
tt.onclick=()=>{const dark=document.documentElement.getAttribute('data-theme')==='dark';if(dark){document.documentElement.removeAttribute('data-theme');try{localStorage.setItem('nk-theme','light');}catch{}}else{document.documentElement.setAttribute('data-theme','dark');try{localStorage.setItem('nk-theme','dark');}catch{}}themeUI();};themeUI();

/* ---------- today: verse + next feast ---------- */
function easter(y){const a=y%19,b=Math.floor(y/100),c=y%100,d=Math.floor(b/4),e=b%4,f=Math.floor((b+8)/25),g=Math.floor((b-f+1)/3),h=(19*a+b-d-g+15)%30,i=Math.floor(c/4),k=c%4,l=(32+2*e+2*i-h-k)%7,m=Math.floor((a+11*h+22*l)/451),mo=Math.floor((h+l-7*m+114)/31),da=((h+l-7*m+114)%31)+1;return new Date(y,mo-1,da);}
function feastsFor(y){const out=D.feasts.map(f=>({...f,date:new Date(y,f.m-1,f.d)}));const e=easter(y);D.moving.forEach(f=>{const d=new Date(e);d.setDate(d.getDate()+f.off);out.push({id:f.id,kind:f.kind,name:f.name,date:d});});return out.sort((a,b)=>a.date-b.date);}
function upcoming(n=60){const today=startOfDay(new Date()),all=[...feastsFor(today.getFullYear()),...feastsFor(today.getFullYear()+1)];return all.filter(f=>f.date>=today).slice(0,n).map(f=>({...f,days:Math.round((f.date-today)/864e5)}));}
const rel=n=>n===0?T.today_is:n===1?T.tomorrow:fmt(T.in_days,{n});
const dfmt=d=>d.toLocaleDateString(D.lang==='ar'?'ar-LB':D.lang,{day:'numeric',month:'long'});
let verseIdx=dayOfYear(new Date())%D.verses.length;
$$('[data-today]').forEach(box=>{function draw(){const v=D.verses[verseIdx],nf=upcoming(1)[0];box.replaceChildren(
 el('div',{class:'today-verse'},el('p',{class:'eyebrow',text:T.verse_day}),el('blockquote',{},el('p',{text:v.text}),el('cite',{text:v.ref})),el('div',{class:'cta-row'},el('button',{class:'btn ghost sm',type:'button',text:T.another,onclick:()=>{verseIdx=(verseIdx+1)%D.verses.length;draw();}}),el('a',{class:'text-link',href:'play.html#cards',text:T.make_card+' →'}))),
 el('div',{class:'today-feast'},el('p',{class:'eyebrow',text:T.next_feast}),el('strong',{text:nf.name}),el('span',{class:'soft',text:dfmt(nf.date)+' · '+rel(nf.days)})));}
 draw();});
/* ---------- continue + keep exploring ---------- */
const cont=$('[data-continue]');
if(cont){const lp=store.get('lastvisit',null);if(lp&&lp!=='index'){const p=D.pages.find(x=>x.slug===lp);if(p){cont.hidden=false;cont.append(el('p',{class:'eyebrow',text:T.h_cont}),el('a',{class:'continue-card',href:p.href},el('span',{class:'mi-ic'},ico(p.ic)),el('span',{},el('strong',{text:p.title}),el('small',{text:p.summary})),ico('arrow-right')));}}}
if(D.slug!=='index')store.set('lastvisit',D.slug);
const keep=$('[data-keep]');
if(keep){const seen=stamps(),cand=D.pages.filter(p=>p.slug!==D.slug&&p.slug!=='index');cand.sort((a,b)=>(seen.includes(a.slug)-seen.includes(b.slug))||(Math.random()-.5));
 keep.hidden=false;keep.append(el('h2',{text:T.keep}),el('div',{class:'keep-grid'},...cand.slice(0,3).map(p=>el('a',{class:'card-link',href:p.href},el('span',{class:'ci'},ico(p.ic)),el('strong',{text:p.title}),el('small',{text:p.summary})))));}

/* ---------- candles ---------- */
const candleRow=$('#candle-row');
if(candleRow){let candles=store.get('candles',[]);const count=$('#candle-count');
 function drawC(){candleRow.replaceChildren(...candles.map((c,i)=>el('li',{class:'candle',title:c.note||'','aria-label':fmt(T.p_candle_for,{i:i+1})+(c.note?': '+c.note:'')},el('i',{class:'flame'}),el('b',{class:'wick'}),el('span',{class:'wax'}),c.note?el('small',{text:c.note}):'')));count.textContent=fmt(T.p_lit,{n:candles.length});$('.hero-candle').classList.toggle('lit',candles.length>0);}
 $('#candle-light').onclick=()=>{const n=$('#candle-note');candles.push({note:n.value.trim().slice(0,140),t:Date.now()});if(candles.length>24)candles.shift();store.set('candles',candles);n.value='';drawC();award('act_candle');};
 $('#candle-out').onclick=()=>{candles=[];store.set('candles',candles);drawC();};drawC();}

/* ---------- rosary ---------- */
const ros=$('[data-rosary]');
if(ros){const day=new Date().getDay(),def=[ 'glorious','joyful','sorrowful','glorious','luminous','sorrowful','joyful'][day];
 let st=store.get('rosary',{set:def,decade:0,bead:0});if(!D.mys[st.set])st={set:def,decade:0,bead:0};
 const tabs=$('.mys-tabs',ros),beads=$('.beads',ros);
 Object.entries(D.mys).forEach(([k,v])=>tabs.append(el('button',{type:'button',role:'tab','data-set':k,text:v.name+(k===def?' ★':''),onclick:()=>{st={set:k,decade:0,bead:0};save();draw();}})));
 for(let i=0;i<10;i++)beads.append(el('li',{}));
 function save(){store.set('rosary',st);}
 function draw(){$$('button',tabs).forEach(b=>b.setAttribute('aria-selected',String(b.dataset.set===st.set)));const m=D.mys[st.set],done=st.decade>=5;
  $('.rosary-decade',ros).textContent=done?'':fmt(T.p_decade,{d:st.decade+1});$('.rosary-mystery',ros).textContent=done?m.name:m.items[st.decade];
  $$('li',beads).forEach((li,i)=>li.className=i<st.bead?'on':'');$('.rosary-bead',ros).textContent=done?'':fmt(T.p_bead,{b:Math.min(st.bead+1,10)});
  $('[data-hail]',ros).disabled=done;$('.rosary-done',ros).textContent=done?T.p_rosary_done:'';}
 $('[data-hail]',ros).onclick=()=>{st.bead++;if(st.bead>=10){st.bead=0;st.decade++;if(st.decade>=5)award('act_rosary');else if(navigator.vibrate)navigator.vibrate(30);}save();draw();};
 $('[data-undo]',ros).onclick=()=>{if(st.bead>0)st.bead--;else if(st.decade>0){st.decade--;st.bead=9;}save();draw();};
 $('[data-restart]',ros).onclick=()=>{st={set:st.set,decade:0,bead:0};save();draw();};draw();}

/* ---------- soft nay (Arabic flute) with a gentle ison, generated on the device ---------- */
const amb=$('#ambient');
if(amb){
 let ctx=null,master=null,timer=null,alive=[],step=0;
 // Maqam Rast on D (quarter-flat F# and C# approximated), the mode of much Eastern church and village chant
 const D4=293.66,ratio=c=>Math.pow(2,c/1200);
 const SC={0:0,1:200,2:350,3:500,4:700,5:900,6:1050,7:1200,8:1400}; // cents above D4
 const note=d=>D4*ratio(SC[d]);
 // slow, singable phrases: [scale degree, beats]  (0 = rest handled with null)
 const PH=[
  [[4,2],[3,1],[2,1],[1,2],[0,3]],
  [[0,2],[1,1],[2,2],[3,1],[2,2]],
  [[2,2],[4,1],[5,2],[4,1],[3,2],[2,1],[1,2],[0,4]],
  [[0,2],[2,2],[1,1],[0,1],[1,3]],
  [[5,2],[4,1],[3,1],[4,2],[2,2],[1,1],[0,4]],
  [[1,2],[2,1],[3,3],[2,1],[1,1],[0,3]]
 ];
 function impulse(c,sec){const len=c.sampleRate*sec,b=c.createBuffer(2,len,c.sampleRate);for(let ch=0;ch<2;ch++){const d=b.getChannelData(ch);for(let i=0;i<len;i++)d[i]=(Math.random()*2-1)*Math.pow(1-i/len,2.6);}return b;}
 function breath(c,when,dur,gain){const n=c.createBufferSource(),len=Math.max(1,Math.floor(c.sampleRate*(dur+.3))),b=c.createBuffer(1,len,c.sampleRate),d=b.getChannelData(0);for(let i=0;i<len;i++)d[i]=Math.random()*2-1;n.buffer=b;const f=c.createBiquadFilter();f.type='bandpass';f.frequency.value=2600;f.Q.value=.8;const g=c.createGain();g.gain.setValueAtTime(0,when);g.gain.linearRampToValueAtTime(gain,when+.08);g.gain.exponentialRampToValueAtTime(.0001,when+dur);n.connect(f).connect(g).connect(master.nay);n.start(when);n.stop(when+dur+.3);}
 function nay(freq,when,dur,vel){const c=ctx,o1=c.createOscillator(),o2=c.createOscillator(),g=c.createGain(),lp=c.createBiquadFilter(),vib=c.createOscillator(),vg=c.createGain();
  o1.type='triangle';o2.type='sine';o1.frequency.value=freq;o2.frequency.value=freq*2;
  vib.frequency.value=4.6+Math.random()*.8;vg.gain.value=freq*.006;vib.connect(vg);vg.connect(o1.frequency);vg.connect(o2.frequency);
  lp.type='lowpass';lp.frequency.value=1700;lp.Q.value=.4;
  const g2=c.createGain();g2.gain.value=.22;
  g.gain.setValueAtTime(0,when);g.gain.linearRampToValueAtTime(vel,when+.22);g.gain.setTargetAtTime(vel*.82,when+.3,.6);g.gain.linearRampToValueAtTime(0,when+dur+.5);
  o1.connect(lp);o2.connect(g2).connect(lp);lp.connect(g).connect(master.nay);
  [o1,o2,vib].forEach(o=>{o.start(when);o.stop(when+dur+.6);});alive.push(o1,o2,vib);breath(c,when,Math.min(dur,1.2),.045);}
 function ison(){ // very soft held tone, an octave below the melody's final, as in Byzantine and Maronite chant
  const c=ctx,o=c.createOscillator(),o2=c.createOscillator(),g=c.createGain(),lp=c.createBiquadFilter();o.type='sine';o2.type='sine';o.frequency.value=D4/2;o2.frequency.value=D4;lp.type='lowpass';lp.frequency.value=420;
  g.gain.setValueAtTime(0,c.currentTime);g.gain.linearRampToValueAtTime(.045,c.currentTime+6);const g2=c.createGain();g2.gain.value=.5;o.connect(lp);o2.connect(g2).connect(lp);lp.connect(g).connect(master.bed);o.start();o2.start();alive.push(o,o2);}
 function play(){const beat=1.55,ph=PH[Math.floor(Math.random()*PH.length)];let t=ctx.currentTime+.4;
  ph.forEach(([d,b])=>{const dur=b*beat;nay(note(d),t,dur*.92,.16);t+=dur;});
  const rest=2.5+Math.random()*3;timer=setTimeout(play,(t-ctx.currentTime+rest)*1000);}
 function start(){ctx=new (window.AudioContext||window.webkitAudioContext)();master=ctx.createGain();master.gain.value=0;
  const comp=ctx.createDynamicsCompressor();comp.threshold.value=-24;comp.ratio.value=3;
  const dry=ctx.createGain(),wet=ctx.createGain(),conv=ctx.createConvolver();conv.buffer=impulse(ctx,3.6);dry.gain.value=.7;wet.gain.value=.5;
  master.nay=ctx.createGain();master.nay.gain.value=1;master.bed=ctx.createGain();master.bed.gain.value=1;
  master.nay.connect(dry);master.nay.connect(conv);conv.connect(wet);master.bed.connect(dry);dry.connect(master);wet.connect(master);master.connect(comp).connect(ctx.destination);
  master.gain.linearRampToValueAtTime(.9,ctx.currentTime+3);ison();play();}
 function stop(){if(!ctx)return;clearTimeout(timer);const c=ctx;master.gain.cancelScheduledValues(c.currentTime);master.gain.setValueAtTime(master.gain.value,c.currentTime);master.gain.linearRampToValueAtTime(0,c.currentTime+1.2);setTimeout(()=>{alive.forEach(n=>{try{n.stop();}catch{}});c.close();},1400);ctx=null;alive=[];}
 amb.onclick=()=>{const on=amb.getAttribute('aria-pressed')==='true';if(on){stop();}else{start();}amb.setAttribute('aria-pressed',String(!on));amb.querySelector('span').textContent=on?amb.dataset.off:amb.dataset.on;};
 addEventListener('pagehide',stop);}
const pr=$('[data-print]');if(pr)pr.onclick=()=>{$$('details.prayer-item').forEach(d=>d.open=true);print();};

/* ---------- heritage ---------- */
$$('[data-saint]').forEach(b=>b.onclick=()=>{const s=D.saints[b.dataset.saint];$('#saint-name').textContent=s.name;$('#saint-years').textContent=s.years;$('#saint-text').textContent=s.text;$('#saint-dialog').showModal();});
const sc=$('[data-close-saint]');if(sc)sc.onclick=()=>$('#saint-dialog').close();
const flist=$('[data-feasts]');
if(flist){let filter='all';const nf=$('[data-next-feast]');
 function drawF(){const list=upcoming(40).filter(f=>filter==='all'||f.kind===filter);flist.replaceChildren(...list.slice(0,14).map(f=>el('li',{class:'feast k-'+f.kind},el('time',{datetime:f.date.toISOString().slice(0,10)},el('b',{text:f.date.getDate()}),el('span',{text:f.date.toLocaleDateString(D.lang==='ar'?'ar-LB':D.lang,{month:'short'})})),el('span',{class:'feast-name',text:f.name}),el('span',{class:'soft',text:rel(f.days)}))));const n=upcoming(1)[0];nf.replaceChildren(el('p',{class:'eyebrow',text:T.next_feast}),el('strong',{text:n.name}),el('span',{text:dfmt(n.date)+' · '+rel(n.days)}));}
 $$('[data-filter]').forEach(b=>b.onclick=()=>{filter=b.dataset.filter;$$('[data-filter]').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));drawF();});drawF();
 $('#ics').onclick=()=>{const y=new Date().getFullYear(),pad=n=>String(n).padStart(2,'0'),L=['BEGIN:VCALENDAR','VERSION:2.0','PRODID:-//nk.ci-ccg.com//Maronite feasts//EN','CALSCALE:GREGORIAN'];
  [y,y+1].forEach(yy=>feastsFor(yy).forEach(f=>{const d=f.date,s=`${d.getFullYear()}${pad(d.getMonth()+1)}${pad(d.getDate())}`,e=new Date(d);e.setDate(e.getDate()+1);const en=`${e.getFullYear()}${pad(e.getMonth()+1)}${pad(e.getDate())}`;L.push('BEGIN:VEVENT',`UID:${f.id}-${s}@nk.ci-ccg.com`,`DTSTAMP:${new Date().toISOString().replace(/[-:]/g,'').slice(0,15)}Z`,`DTSTART;VALUE=DATE:${s}`,`DTEND;VALUE=DATE:${en}`,'SUMMARY:'+f.name.replace(/[,;]/g,' '),'TRANSP:TRANSPARENT','END:VEVENT');}));L.push('END:VCALENDAR');
  const a=el('a',{href:URL.createObjectURL(new Blob([L.join('\r\n')],{type:'text/calendar'})),download:'maronite-feasts.ics'});document.body.append(a);a.click();a.remove();award('act_ics');};}

/* ---------- memory game ---------- */
const grid=$('#mem-grid');
if(grid){const cards=[...D.memory.map(m=>({k:m.img,src:D.assets+m.img,name:m.name})),{k:'emblem',src:D.assets+'favicon.svg',name:'NK'}];let first=null,lock=false,moves=0,matched=0,timer=null,t0=0;const best=store.get('mem-best',null);
 const mv=$('#mem-moves'),tm=$('#mem-time'),bs=$('#mem-best'),msg=$('#mem-msg');if(best)bs.textContent=best;
 function shuffle(a){for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;}
 function newGame(){clearInterval(timer);timer=null;first=null;lock=false;moves=0;matched=0;mv.textContent='0';tm.textContent='0';msg.textContent='';grid.replaceChildren(...shuffle([...cards,...cards]).map((c,i)=>{const b=el('button',{class:'mem-card',type:'button','aria-label':'?','data-k':c.k},el('span',{class:'mem-face back','aria-hidden':'true'},ico('cross')),el('span',{class:'mem-face front'},el('img',{src:c.src,alt:'',loading:'lazy',decoding:'async'})));b.onclick=()=>flip(b,c);return b;}));}
 function flip(b,c){if(lock||b.classList.contains('open')||b.classList.contains('done'))return;if(!timer){t0=Date.now();timer=setInterval(()=>tm.textContent=Math.floor((Date.now()-t0)/1000),500);}b.classList.add('open');b.setAttribute('aria-label',c.name);
  if(!first){first={b,c};return;}moves++;mv.textContent=moves;const f=first;first=null;
  if(f.c.k===c.k){f.b.classList.add('done');b.classList.add('done');matched++;if(matched===cards.length){clearInterval(timer);const secs=Math.floor((Date.now()-t0)/1000);msg.textContent=fmt(T.pl_won,{m:moves,t:secs});const bb=store.get('mem-best',null);if(bb===null||moves<bb){store.set('mem-best',moves);bs.textContent=moves;}award('act_memory');}}
  else{lock=true;setTimeout(()=>{[f.b,b].forEach(x=>{x.classList.remove('open');x.setAttribute('aria-label','?');});lock=false;},reduce?400:850);}}
 $('#mem-new').onclick=newGame;newGame();}

/* ---------- heritage quiz ---------- */
const qs=$('#quiz2-start');
if(qs){const stage=$('#quiz2');let n=0,score=0,qset=[];function shuffle(a){for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;}
 function begin(){qset=shuffle([...D.quiz]).slice(0,6);n=0;score=0;draw();}
 function draw(){stage.replaceChildren();if(n===qset.length){const b=Math.max(store.get('quiz-best',0),score);store.set('quiz-best',b);award('act_quiz');stage.append(el('h3',{text:fmt(T.pl_score,{s:score,n:qset.length})}),el('p',{class:'soft',text:fmt(T.pl_streak,{b:b})}),el('button',{class:'button-link',type:'button',text:T.pl_again,onclick:begin}));return;}
  const q=qset[n],opts=el('div',{class:'quiz-options'}),fb=el('div',{class:'quiz-feedback','aria-live':'polite'}),h=el('h3',{text:q.q,tabindex:'-1'});
  q.a.forEach((a,i)=>opts.append(el('button',{type:'button',text:a,onclick:e=>{$$('button',opts).forEach((x,j)=>{x.disabled=true;if(j===q.c)x.classList.add('correct');});if(i===q.c)score++;else e.currentTarget.classList.add('incorrect');fb.append(el('p',{text:(i===q.c?T.pl_right:T.pl_wrong)+' '+q.e}),el('button',{class:'button-link',type:'button',text:T.pl_next,onclick:()=>{n++;draw();}}));}})));
  stage.append(el('div',{class:'q-meter'},el('i')),el('p',{class:'eyebrow',text:`${n+1} / ${qset.length}`}),h,opts,fb);$('.q-meter i',stage).style.setProperty('--p',(n/qset.length).toFixed(3));h.focus({preventScroll:true});}
 qs.onclick=begin;}

/* ---------- prayer card studio (canvas, HD) ---------- */
const cv=$('#card-canvas');
if(cv){const sel=$('#card-verse');D.verses.forEach((v,i)=>sel.append(el('option',{value:i,text:v.ref})));sel.value=verseIdx;let bg=0,res=1;const imgs={};
 const srcs=[null,'portrait-archive.jpg','memorial-art.jpg'];function load(i){return new Promise(r=>{if(!srcs[i]||imgs[i])return r(imgs[i]);const im=new Image();im.onload=()=>{imgs[i]=im;r(im);};im.onerror=()=>r(null);im.src=D.assets+srcs[i];});}
 function wrap(ctx,text,maxW){const words=text.split(/\s+/),lines=[];let cur='';for(const w of words){const test=cur?cur+' '+w:w;if(ctx.measureText(test).width>maxW&&cur){lines.push(cur);cur=w;}else cur=test;}if(cur)lines.push(cur);return lines;}
 async function draw(target=cv,scale=1){const W=1080*scale,H=1350*scale,ctx=target.getContext('2d');target.width=W;target.height=H;const v=D.verses[+sel.value],rtl=D.lang==='ar';
  const fam=rtl?'"Amiri",serif':'"Newsreader",Georgia,serif';try{await Promise.all([document.fonts.load('700 40px "Amiri"'),document.fonts.load('600 40px "Inter"'),document.fonts.load('italic 400 40px "Newsreader"')]);}catch{}
  const g=ctx.createLinearGradient(0,0,W,H);g.addColorStop(0,'#0e1d17');g.addColorStop(1,'#26493b');ctx.fillStyle=g;ctx.fillRect(0,0,W,H);
  const im=await load(bg);if(im){const r=Math.max(W/im.width,H/im.height),w=im.width*r,h=im.height*r;ctx.save();ctx.filter='saturate(.7) blur(0px)';ctx.drawImage(im,(W-w)/2,(H-h)/2,w,h);ctx.restore();const o=ctx.createLinearGradient(0,0,0,H);o.addColorStop(0,'rgba(8,20,15,.55)');o.addColorStop(.5,'rgba(8,20,15,.8)');o.addColorStop(1,'rgba(8,20,15,.92)');ctx.fillStyle=o;ctx.fillRect(0,0,W,H);}
  else{ctx.strokeStyle='rgba(177,138,80,.16)';ctx.lineWidth=2*scale;for(let i=1;i<9;i++){ctx.beginPath();ctx.ellipse(W*.8,H*.18,i*110*scale,i*80*scale,-.35,0,7);ctx.stroke();}}
  ctx.strokeStyle='#b18a50';ctx.lineWidth=3*scale;ctx.strokeRect(50*scale,50*scale,W-100*scale,H-100*scale);
  ctx.textAlign='center';ctx.direction=rtl?'rtl':'ltr';ctx.fillStyle='#d9bc86';ctx.font=`${70*scale}px ${fam}`;ctx.fillText('✝',W/2,200*scale);
  let size=(rtl?66:62)*scale,lines;const maxW=W-230*scale;do{ctx.font=`${rtl?'':'italic '}400 ${size}px ${fam}`;lines=wrap(ctx,v.text,maxW);size-=2*scale;}while(lines.length*size*1.5>H*.52&&size>30*scale);size+=2*scale;
  const lh=size*1.5,total=lines.length*lh;let y=H/2-total/2+size*.2;ctx.fillStyle='#f6f1e5';lines.forEach(l=>{ctx.fillText(l,W/2,y);y+=lh;});
  ctx.fillStyle='#d9bc86';ctx.font=`600 ${34*scale}px "Inter",Arial,sans-serif`;ctx.direction='ltr';ctx.fillText(v.ref.toUpperCase(),W/2,y+50*scale);
  ctx.fillStyle='#b9c4b9';ctx.font=`500 ${28*scale}px "Inter",Arial,sans-serif`;ctx.fillText(T.share_title+' · nk.ci-ccg.com',W/2,H-100*scale);}
 draw();sel.onchange=()=>draw();
 $$('[data-bg]').forEach(b=>b.onclick=()=>{bg=+b.dataset.bg;$$('[data-bg]').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));draw();});
 $$('[data-res]').forEach(b=>b.onclick=()=>{res=+b.dataset.res;$$('[data-res]').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));});
 async function blob(){const c=document.createElement('canvas');await draw(c,res);return new Promise(r=>c.toBlob(r,'image/png'));}
 $('#card-dl').onclick=async()=>{const b=await blob(),a=el('a',{href:URL.createObjectURL(b),download:`nk-prayer-card-${res===2?'uhd':'hd'}.png`});document.body.append(a);a.click();a.remove();award('act_card');};
 $('#card-share').onclick=async()=>{try{const b=await blob(),f=new File([b],'nk-prayer-card.png',{type:'image/png'});if(navigator.canShare&&navigator.canShare({files:[f]})){await navigator.share({files:[f],title:T.share_title});award('act_card');}else{$('#card-dl').click();}}catch(e){if(e.name!=='AbortError')$('#card-dl').click();}};}

/* ---------- streaming player (privacy-friendly facade; loads YouTube only on play) ---------- */
const yt=id=>`https://www.youtube-nocookie.com/embed/${id}?autoplay=1&rel=0&modestbranding=1&playsinline=1`;
const thumb=id=>`https://i.ytimg.com/vi/${id}/hqdefault.jpg`;
function iframe(id,title){return el('iframe',{src:yt(id),title:title,allow:'autoplay; encrypted-media; picture-in-picture; fullscreen',allowfullscreen:'',referrerpolicy:'strict-origin-when-cross-origin'});}
const vd=$('#video-dialog');let vcur=0;
function openTheater(id){const v=D.videos.find(x=>x.id===id)||D.videos[0];vcur=D.videos.indexOf(v);$('[data-vtitle]',vd).textContent=v.title;$('[data-vframe]',vd).replaceChildren(iframe(v.id,v.title));$('[data-vyt]',vd).href='https://www.youtube.com/watch?v='+v.id;if(!vd.open)vd.showModal();award('act_watch');store.set('lastvideo',v.id);}
if(vd){const step=d=>openTheater(D.videos[(vcur+d+D.videos.length)%D.videos.length].id);$('[data-vprev]',vd).onclick=()=>step(-1);$('[data-vnext]',vd).onclick=()=>step(1);$('[data-close-video]',vd).onclick=()=>vd.close();vd.addEventListener('close',()=>$('[data-vframe]',vd).replaceChildren());vd.addEventListener('click',e=>{if(e.target===vd)vd.close();});}
$$('[data-watch]').forEach(b=>b.addEventListener('click',()=>openTheater(b.dataset.watch)));
$$('[data-player]').forEach(box=>{const limit=+box.dataset.limit||99;let cat='all',idx=0;
 const cats=[['all',T.v_all],['nk',T.v_nk],['lit',T.v_lit],['sai',T.v_sai]];
 const main=el('div',{class:'player-main'}),side=el('div',{class:'player-list'});box.append(main,side);
 const list=()=>D.videos.filter(v=>cat==='all'||v.cat===cat);
 function screen(){const v=list()[idx]||D.videos[0];
  const facade=el('button',{class:'facade',type:'button','aria-label':T.v_play+': '+v.title},el('img',{src:thumb(v.id),alt:'',width:'480',height:'360',decoding:'async'}),el('span',{class:'play'},ico('play')),el('span',{class:'dur','aria-hidden':'true',text:v.dur}));
  const scr=el('div',{class:'player-screen'},facade);facade.onclick=()=>{scr.replaceChildren(iframe(v.id,v.title));award('act_watch');store.set('lastvideo',v.id);};
  const pop=el('button',{class:'btn ghost sm',type:'button',onclick:()=>openTheater(v.id)},ico('maximize-2'),el('span',{text:T.v_popout}));
  main.replaceChildren(scr,el('div',{class:'player-meta'},el('div',{},el('div',{class:'ptitle',text:v.title}),el('p',{text:v.by+' · '+v.dur})),pop));}
 function listUI(){const items=list().slice(0,limit);side.replaceChildren(el('div',{class:'vchips',role:'group'},...cats.map(([k,l])=>el('button',{type:'button','aria-pressed':String(k===cat),text:l,onclick:()=>{cat=k;idx=0;screen();listUI();}}))),
  el('div',{class:'vlist'},...items.map((v,i)=>el('button',{class:'vitem',type:'button','aria-current':String(i===idx),onclick:()=>{idx=i;screen();listUI();}},el('span',{class:'th'},el('img',{src:thumb(v.id),alt:'',loading:'lazy',decoding:'async'}),el('b',{text:v.dur})),el('span',{},el('strong',{text:v.title}),el('small',{text:v.by}))))));}
 screen();listUI();});

/* ---------- welcome sheet (first visit, home only) ---------- */
const wd=$('#welcome-dialog');
if(wd){$$('[data-close-welcome]',wd).forEach(b=>b.addEventListener('click',()=>{store.set('welcomed',1);wd.close();}));wd.addEventListener('click',e=>{if(e.target===wd){store.set('welcomed',1);wd.close();}});
 if(!store.get('welcomed',0)&&!/[?&]nowelcome/.test(location.search))setTimeout(()=>{if(!document.querySelector('dialog[open]'))wd.showModal();},1400);}

/* ---------- keyboard: Ctrl/Cmd+K or "/" opens search ---------- */
addEventListener('keydown',e=>{const tag=(e.target.tagName||'').toLowerCase();if(((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='k')||(e.key==='/'&&!['input','textarea','select'].includes(tag))){const b=document.querySelector('[data-open-search]');if(b){e.preventDefault();b.click();}}});
})();
