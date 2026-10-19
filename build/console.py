#!/usr/bin/env python3
"""build/console-data.json -> console.html

The console is a workbench, not a slide deck: one registry page at a time,
every step for that page on one screen, one click per step.
"""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = (ROOT / "build" / "console-data.json").read_text(encoding="utf-8")
C = json.loads(DATA)["meta"]["counts"]

HTML = r"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>ReLEAF Registry Console</title>
<style>
:root{
 --bg:#fff; --bg2:#f5f5f7; --bg3:#ebebf0; --ink:#1d1d1f; --mut:#6e6e73; --line:#d2d2d7;
 --blue:#0071e3; --blueSoft:#e8f1fd; --green:#1d7a4d; --greenSoft:#eaf6ef;
 --amber:#9a5000; --amberSoft:#fdf3e7; --red:#b3261e; --redSoft:#fdeeee; --r:18px;
}
*{box-sizing:border-box}
html{-webkit-font-smoothing:antialiased}
body{margin:0;background:var(--bg);color:var(--ink);
 font:17px/1.47 -apple-system,BlinkMacSystemFont,"SF Pro Text","Helvetica Neue",Helvetica,Arial,sans-serif;
 letter-spacing:-.011em}
.wrap{max-width:1020px;margin:0 auto;padding:0 22px}
a{color:var(--blue);text-decoration:none}
a:hover{text-decoration:underline}

header{position:sticky;top:0;z-index:30;
 background:rgba(255,255,255,.82);backdrop-filter:saturate(180%) blur(20px);
 -webkit-backdrop-filter:saturate(180%) blur(20px);border-bottom:1px solid var(--line)}
.hrow{display:flex;align-items:center;gap:14px;padding:11px 0}
.brand{font-size:18px;font-weight:600;letter-spacing:-.021em;white-space:nowrap}
.brand small{display:block;font-size:11.5px;font-weight:400;color:var(--mut);letter-spacing:0}
.grow{flex:1}
.eta{text-align:right;white-space:nowrap;line-height:1.3}
.eta b{font-size:15px;font-weight:600;display:block}
.eta span{font-size:11.5px;color:var(--mut)}
.ring{width:40px;height:40px;flex:none}
.ring circle{fill:none;stroke-width:4}
.ring .t{stroke:var(--line)}
.ring .v{stroke:var(--blue);stroke-linecap:round;transition:stroke-dasharray .3s}
.ringn{font:600 11px/1 -apple-system,sans-serif;fill:var(--ink);letter-spacing:-.02em}

.seg{display:inline-flex;background:var(--bg2);border-radius:10px;padding:2px;gap:2px}
.seg button{border:0;background:none;font:inherit;font-size:14px;color:var(--ink);
 padding:6px 14px;border-radius:8px;cursor:pointer;white-space:nowrap}
.seg button[aria-selected=true],.seg button[aria-pressed=true]{background:#fff;box-shadow:0 1px 3px rgba(0,0,0,.1);font-weight:500}
.who button{font-size:13px;padding:6px 11px;color:var(--mut)}
.who button[aria-pressed=true]{color:var(--ink)}

main{padding:0 0 110px}
h2.view{font-size:26px;letter-spacing:-.022em;font-weight:600;margin:28px 0 4px}
.lede{color:var(--mut);font-size:15px;margin:0 0 22px}

.btn{border:0;border-radius:980px;padding:9px 19px;font:inherit;font-size:15px;font-weight:500;
 background:var(--blue);color:#fff;cursor:pointer;white-space:nowrap;text-decoration:none;display:inline-block}
.btn:hover{filter:brightness(1.08);text-decoration:none}
.btn.sec{background:var(--bg2);color:var(--ink)}
.btn.ok{background:var(--green)}
.btn.sm{padding:6px 13px;font-size:13px}
.btn:disabled{opacity:.3;cursor:default}

/* ---------- the rail: 33 parts at a glance ---------- */
.rail{display:flex;gap:3px;padding:12px 0 0;flex-wrap:wrap}
.rail button{flex:1 1 14px;min-width:14px;height:26px;border:0;border-radius:5px;cursor:pointer;
 background:var(--bg3);position:relative;padding:0;font:600 9px/1 ui-monospace,monospace;color:var(--mut)}
.rail button .f{position:absolute;left:0;bottom:0;width:100%;border-radius:5px;background:var(--blue);opacity:.22}
.rail button[data-s=done]{background:var(--greenSoft)} .rail button[data-s=done] .f{background:var(--green);opacity:.5}
.rail button[data-s=now]{outline:2px solid var(--ink);outline-offset:1px}
.railk{font-size:11.5px;color:var(--mut);padding:7px 0 0}

/* ---------- part bar ---------- */
.pbar{position:sticky;top:var(--htop,63px);z-index:20;background:rgba(255,255,255,.88);
 backdrop-filter:saturate(180%) blur(18px);-webkit-backdrop-filter:saturate(180%) blur(18px);
 border-bottom:1px solid var(--line);margin-bottom:22px}
.pbrow{display:flex;gap:12px;align-items:center;padding:13px 0;flex-wrap:wrap}
.pid{font:600 16px/1.2 ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:-.01em}
.ptitle{color:var(--mut);font-size:14px}
.pill{font-size:11px;font-weight:500;padding:3px 9px;border-radius:980px;background:var(--bg2);color:var(--mut);white-space:nowrap}
.pill.a{background:var(--blueSoft);color:var(--blue)}
.pill.d{background:var(--amberSoft);color:var(--amber)}
.pill.g{background:var(--greenSoft);color:var(--green)}
.bar{height:3px;background:var(--bg3);border-radius:3px;overflow:hidden}
.bar i{display:block;height:100%;background:var(--blue);transition:width .25s}

/* ---------- steps ---------- */
.step{border:1px solid var(--line);border-radius:var(--r);margin:0 0 14px;overflow:hidden;background:#fff}
.step.focus{border-color:var(--ink);box-shadow:0 0 0 2px rgba(0,0,0,.07)}
.step.tick{background:var(--bg2);border-color:var(--bg3)}
.shead{display:flex;gap:10px;align-items:center;padding:15px 20px;flex-wrap:wrap}
.sn{font:600 12px/1 ui-monospace,monospace;color:var(--mut);background:var(--bg2);
 padding:5px 7px;border-radius:6px;flex:none;min-width:24px;text-align:center}
.step.tick .sn{background:var(--green);color:#fff}
.sttl{font-size:17px;font-weight:600;letter-spacing:-.016em;flex:1;min-width:200px}
.step.tick .sttl{font-weight:400;color:var(--mut)}
.sbody{padding:0 20px 18px}
.actsub{color:var(--mut);font-size:13.5px;margin:-4px 0 14px}
pre{background:var(--bg2);border-radius:13px;padding:15px 17px;margin:0;
 font:13px/1.6 ui-monospace,SFMono-Regular,Menlo,monospace;white-space:pre-wrap;word-break:break-word;
 max-height:300px;overflow:auto;letter-spacing:0}
pre.tall{max-height:none}
pre mark{background:var(--amberSoft);color:var(--amber);border-radius:3px;padding:0 2px;font-weight:600}
pre mark.fix{background:var(--greenSoft);color:var(--green)}
.row{display:flex;gap:9px;align-items:center;flex-wrap:wrap;margin-top:14px}
.note{border-radius:12px;padding:11px 14px;font-size:13.5px;margin-top:12px;line-height:1.5}
.note.ok{background:var(--greenSoft);color:var(--green)}
.note.warn{background:var(--amberSoft);color:var(--amber)}
.note.bad{background:var(--redSoft);color:var(--red)}
.note b{font-weight:600}
.note ul{margin:6px 0 0;padding-left:18px}
.note code{background:rgba(255,255,255,.6);padding:1px 5px;border-radius:5px;font-size:12.5px}
.fig{display:flex;gap:18px;flex-wrap:wrap;align-items:flex-start}
.fig img{width:260px;max-width:100%;border:1px solid var(--line);border-radius:12px;background:#fff;cursor:zoom-in}
.fig .fi{flex:1;min-width:250px}
.fn{font:12px/1.5 ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--mut);word-break:break-all}
.cap{font-size:14px;margin:8px 0 0}
.diff{font:13px/1.6 ui-monospace,SFMono-Regular,Menlo,monospace;border-radius:12px;overflow:hidden}
.diff div{padding:10px 14px;white-space:pre-wrap;word-break:break-word}
.diff .old{background:var(--redSoft);color:#8a1c1c;text-decoration:line-through;text-decoration-color:rgba(138,28,28,.4)}
.diff .new{background:var(--greenSoft);color:var(--green)}
.navrow{display:flex;gap:10px;align-items:center;flex-wrap:wrap;
 border-top:1px solid var(--line);padding-top:20px;margin-top:26px}

/* ---------- board ---------- */
.cards3{display:grid;grid-template-columns:repeat(auto-fit,minmax(215px,1fr));gap:14px;margin:0 0 26px}
.box{border:1px solid var(--line);border-radius:var(--r);padding:17px 19px}
.box .n{font-size:27px;font-weight:600;letter-spacing:-.021em;display:block;line-height:1.15}
.box .l{font-size:13.5px;color:var(--mut);display:block;margin-top:4px;line-height:1.4}
table{width:100%;border-collapse:collapse;font-size:14px}
th{text-align:left;font-size:11.5px;text-transform:uppercase;letter-spacing:.03em;color:var(--mut);
 font-weight:600;padding:0 10px 8px 0;border-bottom:1px solid var(--line)}
td{padding:9px 10px 9px 0;border-bottom:1px solid var(--line);vertical-align:middle}
tr.done td{color:var(--mut)}
td.idc{font:600 13px/1 ui-monospace,monospace}
td a.jump{cursor:pointer}
.mini{width:62px;height:5px;background:var(--bg3);border-radius:4px;overflow:hidden;display:inline-block;vertical-align:middle}
.mini i{display:block;height:100%;background:var(--blue)}
tr.done .mini i{background:var(--green)}

/* ---------- figures ---------- */
.lib{display:grid;grid-template-columns:repeat(auto-fill,minmax(205px,1fr));gap:15px}
.lib figure{margin:0}
.lib img{width:100%;border:1px solid var(--line);border-radius:11px;cursor:zoom-in;background:#fff}
.lib figcaption{font-size:11.5px;color:var(--mut);margin-top:6px;line-height:1.42}
.lib .fdone img{opacity:.42}
details{border:1px solid var(--line);border-radius:var(--r);margin:0 0 14px;overflow:hidden}
details summary{padding:14px 20px;cursor:pointer;font-size:14.5px;font-weight:500;list-style:none}
details summary::-webkit-details-marker{display:none}
details summary::after{content:"＋";float:right;color:var(--mut);font-weight:400}
details[open] summary::after{content:"－"}
details .body{padding:0 20px 20px}

/* ---------- decisions ---------- */
.dgroup{margin:0 0 30px}
.dgroup h3{font-size:19px;font-weight:600;letter-spacing:-.019em;margin:0 0 4px}
.dgroup p.sub{color:var(--mut);font-size:14px;margin:0 0 12px}
.ditem{display:flex;gap:12px;padding:13px 0;border-top:1px solid var(--line);align-items:flex-start}
.ditem input{margin-top:4px;width:17px;height:17px;accent-color:var(--blue);flex:none}
.ditem .dt{flex:1;font-size:14.5px;line-height:1.5}
.ditem code{background:var(--bg2);padding:1px 6px;border-radius:5px;font-size:12.5px}
.done{opacity:.4}

dialog{border:0;padding:0;background:transparent;max-width:96vw}
dialog img{max-width:96vw;max-height:92vh;border-radius:14px;display:block}
dialog::backdrop{background:rgba(0,0,0,.72)}
#jump,#help{background:#fff;border-radius:var(--r);box-shadow:0 24px 70px rgba(0,0,0,.3);
 width:min(560px,94vw);padding:0;overflow:hidden}
#jump input{width:100%;border:0;border-bottom:1px solid var(--line);padding:17px 20px;font:inherit;font-size:17px;outline:0}
#jres{list-style:none;margin:0;padding:6px;max-height:50vh;overflow:auto}
#jres li{padding:10px 14px;border-radius:11px;cursor:pointer;display:flex;gap:10px;align-items:baseline;font-size:14.5px}
#jres li .jid{font:600 13px/1 ui-monospace,monospace;flex:none}
#jres li .jt{color:var(--mut);flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
#jres li[aria-selected=true]{background:var(--blueSoft)}
#help .body{padding:22px 24px 26px}
#help h3{margin:0 0 14px;font-size:20px;letter-spacing:-.019em}
.keys{display:grid;grid-template-columns:auto 1fr;gap:9px 14px;font-size:14.5px;align-items:baseline}
.kbd{font:11px/1.3 ui-monospace,monospace;border:1px solid var(--line);border-bottom-width:2px;
 border-radius:5px;padding:3px 6px;color:var(--mut);white-space:nowrap;background:#fff}

.empty{color:var(--mut);font-size:15px;padding:50px 0;text-align:center}
.toast{position:fixed;left:50%;bottom:26px;transform:translateX(-50%) translateY(14px);
 background:var(--ink);color:#fff;padding:11px 20px;border-radius:980px;font-size:14.5px;
 opacity:0;pointer-events:none;transition:.18s;z-index:60}
.toast.on{opacity:1;transform:translateX(-50%)}
footer{border-top:1px solid var(--line);color:var(--mut);font-size:12.5px;padding:22px 0 44px;margin-top:40px}
.foot{display:flex;gap:14px;flex-wrap:wrap;align-items:center}
@media(max-width:760px){
 .hrow{flex-wrap:wrap}.eta{text-align:left}.pbar{top:auto;position:static}
 .fig img{width:100%}.sttl{font-size:16px}
}
</style></head>
<body>
<header><div class="wrap hrow">
 <div class="brand">ReLEAF Registry<small>33 parts · freeze 21 Oct, 23:00 TW</small></div>
 <div class="seg" role="tablist" id="tabs">
  <button role="tab" data-v="queue" aria-selected="true">Queue</button>
  <button role="tab" data-v="board" aria-selected="false">Board</button>
  <button role="tab" data-v="figures" aria-selected="false">Figures</button>
  <button role="tab" data-v="decisions" aria-selected="false">Decisions</button>
 </div>
 <div class="grow"></div>
 <div class="seg who" id="who">
  <button data-w="A" aria-pressed="false">A</button>
  <button data-w="B" aria-pressed="false">B</button>
  <button data-w="all" aria-pressed="true">Both</button>
 </div>
 <div class="eta" id="eta"></div>
 <svg class="ring" viewBox="0 0 42 42"><circle class="t" cx="21" cy="21" r="18"/>
  <circle class="v" cx="21" cy="21" r="18" transform="rotate(-90 21 21)" id="rv"/>
  <text class="ringn" x="21" y="24.5" text-anchor="middle" id="rn">0%</text></svg>
</div></header>
<main id="main"></main>
<dialog id="lb"><img alt=""></dialog>
<dialog id="jump"><input id="jq" placeholder="Jump to a part — id, title or tier" autocomplete="off"><ul id="jres"></ul></dialog>
<dialog id="help"><div class="body">
 <h3>Keys</h3>
 <div class="keys">
  <span><span class="kbd">return</span></span><span>Copy this step and tick it, then move to the next one</span>
  <span><span class="kbd">j</span> <span class="kbd">k</span></span><span>Next / previous step on this part</span>
  <span><span class="kbd">→</span> <span class="kbd">←</span></span><span>Next / previous part</span>
  <span><span class="kbd">o</span></span><span>Open this part on the registry</span>
  <span><span class="kbd">f</span></span><span>Download the figure for this step</span>
  <span><span class="kbd">x</span></span><span>Tick or untick without copying</span>
  <span><span class="kbd">g</span></span><span>Go to the first part still unfinished</span>
  <span><span class="kbd">/</span></span><span>Jump to a part by name</span>
  <span><span class="kbd">1</span>–<span class="kbd">4</span></span><span>Queue, Board, Figures, Decisions</span>
  <span><span class="kbd">?</span></span><span>This list</span>
 </div>
</div></dialog>
<div class="toast" id="toast"></div>
<footer class="wrap"><div class="foot">
 <span><span class="kbd">return</span> copy &amp; tick · <span class="kbd">→</span> next part · <span class="kbd">/</span> jump · <span class="kbd">?</span> all keys</span>
 <span class="grow"></span>
 <a href="reference.html">Reference</a> <a href="index.html">Pack</a>
 <span id="built"></span>
</div></footer>

<script id="DATA" type="application/json">%%DATA%%</script>
<script>
const D=JSON.parse(document.getElementById('DATA').textContent);
const STEPS=D.steps, CARDS=D.cards, LIB=D.library, ORDER=D.order, META=D.meta;
const DIS=Object.assign({disputed:[],suspect_sequence:[],recheck:[],design_history:[]},D.disputes||{});
const SK='releaf-registry-v2', PK='releaf-registry-prefs-v3', TK='releaf-registry-pace-v3';
const rd=(k,f)=>{try{return JSON.parse(localStorage.getItem(k)||'null')||f}catch(e){return f}};
let st=rd(SK,{}), pf=Object.assign({lane:'all',opt:false,names:{A:'A',B:'B'},pi:0},rd(PK,{})), pace=rd(TK,{t:[]});
const wr=(k,v)=>{try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}};
const save=()=>wr(SK,st), savePf=()=>wr(PK,pf), savePace=()=>wr(TK,pace);
let view='queue', si=0, tall={};

const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const lane=()=>pf.lane, nm=w=>w==='all'?'both':(pf.names[w]||w);
const inLane=s=>lane()==='all'||s.who===lane();
const isTick=s=>!!st[s.id];
const shown=s=>s.bucket==='req'||(s.bucket==='opt'&&pf.opt)||s.bucket==='dec';
const actionable=s=>s.bucket==='req'||s.bucket==='opt';
const partSteps=p=>STEPS.filter(s=>s.part===p&&inLane(s)&&shown(s));
const partWork=p=>partSteps(p).filter(actionable);
const parts=()=>ORDER.filter(p=>STEPS.some(s=>s.part===p&&inLane(s)));
const clampPi=()=>{const n=parts().length;if(pf.pi>=n)pf.pi=n-1;if(pf.pi<0)pf.pi=0;return pf.pi};
const curPart=()=>parts()[clampPi()];
const reqAll=()=>STEPS.filter(s=>inLane(s)&&s.bucket==='req');
const workAll=()=>STEPS.filter(s=>inLane(s)&&actionable(s)&&shown(s));
const fin=p=>{const w=partWork(p);return w.length>0&&w.every(isTick)};
const hhmm=m=>{m=Math.max(0,Math.round(m));return m<60?m+' min':Math.floor(m/60)+' h '+String(m%60).padStart(2,'0')+' m'};
const URLP=p=>'https://registry.igem.org/parts/'+CARDS[p].slug;

function rate(){
 const t=pace.t||[], d=[];
 for(let i=1;i<t.length;i++){const x=t[i]-t[i-1];if(x>4000&&x<15*60000)d.push(x)}
 if(d.length<4) return null;
 d.sort((a,b)=>a-b);
 return d[Math.floor(d.length/2)]/60000;
}
function eta(){
 const w=workAll(), left=w.filter(s=>!isTick(s));
 const r=rate();
 const mins=r?left.length*r:left.reduce((a,s)=>a+s.min,0);
 return {left:left.length,total:w.length,mins,r};
}
function head(){
 const w=workAll(), done=w.filter(isTick).length, pc=w.length?done/w.length:0;
 document.getElementById('rv').setAttribute('stroke-dasharray',(pc*113).toFixed(1)+' 113');
 document.getElementById('rn').textContent=Math.round(pc*100)+'%';
 const e=eta();
 document.getElementById('eta').innerHTML=
  `<b>${e.left} left · ${hhmm(e.mins)}</b><span>${done} of ${e.total} done`
  +(e.r?` · ${e.r.toFixed(1)} min/step, measured`:'')+(lane()==='all'?' · both lanes':` · ${esc(nm(lane()))}`)+`</span>`;
 [...document.querySelectorAll('#who button')].forEach(b=>b.setAttribute('aria-pressed',b.dataset.w===lane()));
 [...document.querySelectorAll('#tabs button')].forEach(b=>b.setAttribute('aria-selected',b.dataset.v===view));
 document.getElementById('built').textContent='built '+META.built;
}
let tt;
function toast(m){const t=document.getElementById('toast');t.textContent=m;t.classList.add('on');clearTimeout(tt);tt=setTimeout(()=>t.classList.remove('on'),1400)}

function payload(s){
 return (s.kind==='image'||s.kind==='model'||s.kind==='plant')?s.caption:s.kind==='fix'?s.fix:s.text;
}
function copy(text,label){
 const ok=()=>toast((label||'Copied')+' — paste it into the registry');
 if(navigator.clipboard&&navigator.clipboard.writeText){
  navigator.clipboard.writeText(text).then(ok,()=>legacy(text,ok));
 } else legacy(text,ok);
}
function legacy(text,ok){
 const ta=document.createElement('textarea');
 ta.value=text;ta.style.position='fixed';ta.style.opacity='0';
 document.body.appendChild(ta);ta.select();
 let done=false;try{done=document.execCommand('copy')}catch(e){}
 ta.remove();
 done?ok():toast('Copy blocked — select the text and press ⌘C');
}
function tick(s,v){
 const was=isTick(s);
 if(v===was) return;
 if(v){st[s.id]=true;(pace.t=pace.t||[]).push(Date.now());savePace()} else delete st[s.id];
 save();
}

/* ------------------------------------------------ step rendering */
function marked(s){
 const t=s.text||'', m=s.marks||[];
 if(!m.length) return esc(t);
 let h='',at=0;
 m.forEach(([a,b,k])=>{if(a<at)return;h+=esc(t.slice(at,a))+`<mark class="${k==='fix'?'fix':''}">`+esc(t.slice(a,b))+'</mark>';at=b});
 return h+esc(t.slice(at));
}
const SUB={section:'Open the existing entry on the registry, select its whole body, paste over it.',
 draft:'This entry does not exist yet. Add it, then paste.',
 image:'Upload the file inside this entry, then paste the legend under it as a bold paragraph.',
 model:'Optional. A modelling figure for the Design entry.',
 plant:'Cargo-level evidence — it belongs once in the collection, not on every part.',
 noimage:'No image exists for this. Decide and move on — nothing to paste.'};

function stepCard(s,n,focus){
 const t=isTick(s), act=actionable(s);
 const cls='step'+(t?' tick':'')+(focus&&!t?' focus':'');
 let h=`<div class="${cls}" data-id="${esc(s.id)}"><div class="shead">`
  +`<span class="sn">${t?'✓':n}</span><span class="sttl">${esc(s.label)}</span>`
  +`<span class="pill">${esc(s.type)}</span>`
  +(s.words?`<span class="pill">${s.words} w</span>`:'')
  +(s.bucket==='opt'?'<span class="pill">optional</span>':'')
  +(s.bucket==='dec'?'<span class="pill d">judgement call</span>':'')
  +(s.fixed?`<span class="pill g">${s.fixed.length} fix${s.fixed.length>1?'es':''} baked in</span>`:'')
  +(s.blockers&&s.blockers.length?`<span class="pill d">${s.blockers.length} bracket${s.blockers.length>1?'s':''}</span>`:'')
  +(t&&act?`<button class="btn sec sm" data-un="${esc(s.id)}">Undo</button>`:'')
  +`</div>`;
 if(t) return h+'</div>';
 h+=`<div class="sbody"><p class="actsub">${SUB[s.kind]||''}</p>`;

 if(s.kind==='section'||s.kind==='draft'){
  h+=`<pre class="${tall[s.id]?'tall':''}" data-pre="${esc(s.id)}">${marked(s)}</pre>`;
  if((s.text||'').length>1400) h+=`<div class="row"><button class="btn sec sm" data-tall="${esc(s.id)}">${tall[s.id]?'Collapse':'Show all'}</button></div>`;
  if(s.fixed) h+=`<div class="note ok"><b>This paste also repairs what is live now.</b><ul>`
   +s.fixed.map(f=>`<li>${esc(f.why)}</li>`).join('')+`</ul></div>`;
  if(s.kind==='draft') h+=`<div class="note warn"><b>New entry, drafted here.</b> Read it before you paste — it was assembled from what the sibling parts already say.</div>`;
  if(s.blockers&&s.blockers.length) h+=`<div class="note warn"><b>Still bracketed — marked in the text above.</b> `
   +s.blockers.map(b=>`<code>[${esc(b[0])}]</code> ${esc(b[1])}`).join(' · ')+`</div>`;
  if(s.resolved&&s.resolved.length) h+=`<div class="note ok"><b>${s.resolved.length} bracket${s.resolved.length>1?'s':''} already resolved.</b> `
   +s.resolved.map(r=>`<code>[${esc(r[0])}]</code> → ${esc(r[1])} <span style="opacity:.75">(${esc(r[2])})</span>`).join(' · ')+`</div>`;
 }
 else if(s.kind==='image'||s.kind==='model'||s.kind==='plant'){
  const dir=s.kind==='image'?'upload':s.kind==='model'?'modelling':'plant';
  const th=s.kind==='image'?'thumbs/'+s.file:'thumbs/'+dir+'/'+s.file;
  h+=`<div class="fig"><img src="${esc(th)}" data-full="${esc(dir+'/'+s.file)}" alt="">`
   +`<div class="fi"><div class="fn">${esc(dir+'/'+s.file)}</div>`
   +(s.dim?`<div class="pill" style="margin-top:7px">${esc(s.dim)} · ${s.kb} KB</div>`:'')
   +`<p class="cap">${esc(s.caption)}</p>`
   +(s.why?`<div class="note ${s.kind==='plant'?'warn':'ok'}">${esc(s.why)}</div>`:'')
   +`<div class="row"><a class="btn sec" download href="${esc(dir+'/'+s.file)}">Download the file</a></div>`
   +`</div></div>`;
 }
 else if(s.kind==='noimage'){
  h+=`<pre>${esc(s.caption)}</pre><div class="note warn"><b>No such image exists.</b> ${esc(s.why)}</div>`;
 }
 else if(s.kind==='fix'){
  h+=`<div class="diff"><div class="old">${esc(s.find)}</div><div class="new">${esc(s.fix)}</div></div>`
   +`<div class="note warn"><b>Why.</b> ${esc(s.why)}</div>`;
 }
 if(act) h+=`<div class="row"><button class="btn" data-go="${esc(s.id)}">${s.kind==='section'||s.kind==='draft'?'Copy the markdown':'Copy the legend'} &amp; tick</button>`
  +`<button class="btn sec" data-cp="${esc(s.id)}">Copy only</button>`
  +`<button class="btn sec sm" data-tk="${esc(s.id)}">Tick without copying</button></div>`;
 return h+'</div></div>';
}

/* ------------------------------------------------ queue */
function viewQueue(){
 const P=parts();
 if(!P.length) return '<div class="wrap"><p class="empty">Nothing in this lane.</p></div>';
 const p=curPart(), c=CARDS[p], all=partSteps(p), work=partWork(p);
 const done=work.filter(isTick).length, pc=work.length?done/work.length:0;
 const nxt=P.findIndex((q,i)=>i>pf.pi&&!fin(q));
 let h='<div class="wrap"><div class="rail">'+P.map((q,i)=>{
   const w=partWork(q), d=w.filter(isTick).length;
   const s=i===pf.pi?'now':(w.length&&d===w.length?'done':'');
   return `<button data-pi="${i}" data-s="${s}" title="${esc(q+' — '+(CARDS[q].title||''))}">`
    +`<span class="f" style="height:${w.length?Math.round(d/w.length*100):0}%"></span></button>`}).join('')
  +`</div><p class="railk">Part ${pf.pi+1} of ${P.length} · ${P.filter(fin).length} finished`
  +(nxt>=0?` · <a data-pi="${nxt}" style="cursor:pointer">skip to the next unfinished</a>`:'')+`</p></div>`;

 h+=`<div class="pbar"><div class="wrap"><div class="pbrow">
  <span class="pid">${p}</span><span class="ptitle">${esc(c.title||'untitled')}</span>
  <span class="pill ${c.tier==='A'?'a':''}">Tier ${c.tier}</span><span class="pill">${esc(c.grp)}</span>
  ${c.status==='draft'?'<span class="pill d">part is a draft</span>':''}
  <span class="pill ${done===work.length?'g':''}">${done}/${work.length} steps</span>
  <span class="pill">lane ${esc(nm(c.who))}</span>
  <span class="grow"></span>
  <a class="btn" href="${URLP(p)}" target="_blank" rel="noopener" id="openp">Open ${p} ↗</a>
  <button class="btn sec sm" data-pi="${pf.pi-1}" ${pf.pi===0?'disabled':''}>←</button>
  <button class="btn sec sm" data-pi="${pf.pi+1}" ${pf.pi>=P.length-1?'disabled':''}>→</button>
 </div><div class="bar"><i style="width:${(pc*100).toFixed(0)}%"></i></div></div></div>`;

 const vis=all.filter(actionable);
 if(si>=vis.length) si=Math.max(0,vis.length-1);
 h+='<div class="wrap">';
 let n=0, fid=vis[si]?vis[si].id:null;
 all.forEach(s=>{if(actionable(s))n++;h+=stepCard(s,n,s.id===fid)});
 if(!all.length) h+='<p class="empty">No steps for this part in this lane.</p>';

 h+=`<div class="navrow">
  <button class="btn ${done===work.length?'ok':''}" data-pi="${pf.pi+1}" ${pf.pi>=P.length-1?'disabled':''}>`
  +`${done===work.length?'Part done — next part':'Next part'} →</button>`
  +`<button class="btn sec" data-allp="${esc(p)}">Tick every step on this part</button>`
  +`<span class="grow"></span>`
  +`<label class="pill" style="cursor:pointer;padding:7px 12px"><input type="checkbox" id="optx" ${pf.opt?'checked':''} style="vertical-align:-2px"> show the ${META.counts.optional} optional figure steps (+${hhmm(META.counts.min_opt)})</label>`
  +`</div></div>`;
 return h;
}

/* ------------------------------------------------ board */
function viewBoard(){
 const P=parts(), e=eta();
 const A=STEPS.filter(s=>s.who==='A'&&s.bucket==='req'), B=STEPS.filter(s=>s.who==='B'&&s.bucket==='req');
 const cnt=(a)=>a.filter(isTick).length;
 let h=`<div class="wrap"><h2 class="view">Board</h2>
 <p class="lede">Where both lanes stand. Click any part to work it.</p>
 <div class="cards3">
  <div class="box"><span class="n">${cnt(A)}/${A.length}</span><span class="l">lane ${esc(nm('A'))} · required steps<br><a data-ren="A" style="cursor:pointer">rename</a></span></div>
  <div class="box"><span class="n">${cnt(B)}/${B.length}</span><span class="l">lane ${esc(nm('B'))} · required steps<br><a data-ren="B" style="cursor:pointer">rename</a></span></div>
  <div class="box"><span class="n">${P.filter(fin).length}/${P.length}</span><span class="l">parts finished in the current lane view</span></div>
  <div class="box"><span class="n">${hhmm(e.mins)}</span><span class="l">left in this lane${e.r?` at your measured ${e.r.toFixed(1)} min a step`:' on the staged estimate'}</span></div>
 </div>
 <table><thead><tr><th>Part</th><th>Title</th><th>Tier</th><th>Lane</th><th>Steps</th><th></th><th></th></tr></thead><tbody>`;
 P.forEach((p,i)=>{
  const c=CARDS[p], w=partWork(p), d=w.filter(isTick).length;
  h+=`<tr class="${fin(p)?'done':''}"><td class="idc"><a class="jump" data-pi="${i}">${p}</a></td>
   <td>${esc(c.title||'untitled')}${c.status==='draft'?' <span class="pill d">draft</span>':''}</td>
   <td>${c.tier}</td><td>${esc(nm(c.who))}</td>
   <td>${d}/${w.length}</td>
   <td><span class="mini"><i style="width:${w.length?Math.round(d/w.length*100):0}%"></i></span></td>
   <td><a href="${URLP(p)}" target="_blank" rel="noopener">registry ↗</a></td></tr>`;
 });
 h+=`</tbody></table>
 <details style="margin-top:26px"><summary>Handoff and backup — progress lives in this browser only</summary><div class="body">
  <p class="actsub">Ticks are kept in this browser. Use these to move progress to another machine, to merge the two lanes at the end, or to recover after a crash.</p>
  <div class="row">
   <button class="btn sec" id="pexp">Copy a progress code</button>
   <button class="btn sec" id="pimp">Paste a progress code</button>
   <button class="btn sec" id="prep">Copy a status report</button>
   <button class="btn sec" id="pclr">Clear all ticks</button>
  </div></div></details></div>`;
 return h;
}

/* ------------------------------------------------ figures */
function viewFigures(){
 const img=STEPS.filter(s=>s.kind==='image'&&inLane(s));
 const left=img.filter(s=>!isTick(s));
 let h=`<div class="wrap"><h2 class="view">Figures</h2>
 <p class="lede">${img.length} wet-lab figures have a slot waiting; ${left.length} still to upload. Download the file, then upload it on the part page.</p>
 <div class="row" style="margin:0 0 18px">${left.map(s=>`<a class="btn sec sm" download href="upload/${esc(s.file)}">${esc(s.part)} · ${esc(s.type).slice(0,4)} fig ${(s.label.match(/figure (\d+)/)||[,'1'])[1]}</a>`).join('')||'<span class="pill g">all uploaded</span>'}</div>
 <div class="lib">`+img.map(s=>`<figure class="${isTick(s)?'fdone':''}">
  <img src="thumbs/${esc(s.file)}" data-full="upload/${esc(s.file)}" alt="">
  <figcaption><b>${esc(s.part)}</b> · ${esc(s.type)} fig ${(s.label.match(/figure (\d+)/)||[,'1'])[1]}${isTick(s)?' · done':''}<br>${esc(s.caption.slice(0,120))}…<br>
  <a download href="upload/${esc(s.file)}">download</a> · <a class="jump" data-pid="${esc(s.part)}" style="cursor:pointer">work this part</a></figcaption></figure>`).join('')+`</div>`;
 Object.keys(LIB).forEach(fam=>{
  if(!LIB[fam].length) return;
  h+=`<details style="margin-top:22px"><summary>${esc(fam)} — ${LIB[fam].length} modelling figures, legends already written</summary><div class="body"><div class="lib">`
   +LIB[fam].map(f=>`<figure><img src="thumbs/modelling/${esc(f.file)}" data-full="modelling/${esc(f.file)}" alt="">
    <figcaption>${esc(f.legend.slice(0,150))}…<br><a download href="modelling/${esc(f.file)}">download</a></figcaption></figure>`).join('')
   +`</div></div></details>`;
 });
 return h+'</div>';
}

/* ------------------------------------------------ decisions */
function viewDecisions(){
 const mine=p=>lane()==='all'||(CARDS[p]&&CARDS[p].who===lane());
 const open=[],fixes=[],noimg=[];
 STEPS.forEach(s=>{
  if(!inLane(s)) return;
  if(s.kind==='fix') fixes.push(s);
  else if(s.kind==='noimage') noimg.push(s);
  else if(s.blockers) s.blockers.forEach(b=>open.push({s,b}));
 });
 const dd=DIS.disputed.filter(d=>mine(d.part)), ds=DIS.suspect_sequence.filter(d=>mine(d.part)),
       dr=DIS.recheck.filter(d=>mine(d.part)), dh=DIS.design_history||[];
 const item=(id,txt)=>`<div class="ditem${st[id]?' done':''}"><input type="checkbox" data-k="${esc(id)}"${st[id]?' checked':''}><div class="dt">${txt}</div></div>`;
 let h=`<div class="wrap"><h2 class="view">Decisions</h2>
 <p class="lede">Settle these once, here, rather than ${open.length+ds.length+dd.length+noimg.length} times at the keyboard. Nothing here blocks a paste.</p>`;
 h+=`<div class="dgroup"><h3>Values still in brackets</h3><p class="sub">${open.length} across the set, each marked amber in the text where it appears. Nothing corroborates them — the wiki caption does not confirm it and it appears nowhere else on the part.</p>`
  +open.map((o,i)=>item('dec:open:'+i,`<code>[${esc(o.b[0])}]</code> on <b>${esc(o.s.part)}</b> ${esc(o.s.type)} — ${esc(o.b[1])}`)).join('')+`</div>`;
 if(ds.length) h+=`<div class="dgroup"><h3>Deposited sequence looks wrong</h3><p class="sub">${ds.length}. Not a documentation problem — editing text cannot fix a sequence that is the vector rather than the construct.</p>`
  +ds.map((d,i)=>item('dec:seq:'+i,`<b>${esc(d.part)}</b> — ${esc(d.why)}`)).join('')+`</div>`;
 if(dd.length) h+=`<div class="dgroup"><h3>Numbers the sequences dispute</h3><p class="sub">${dd.length} values on public pages that the parts' own sequences contradict. Seven are one fault: the Pveg cassettes each assume a promoter of about 290&nbsp;bp where every Pveg part carries 97&nbsp;bp.</p>`
  +dd.map((d,i)=>item('dec:dis:'+i,`<b>${esc(d.part)}</b> ${esc(d.what)} — page says <b>${esc(d.says)}</b>, sequence gives <b>${esc(d.computed)}</b><br><span style="color:var(--mut);font-size:13px">${esc(d.why)}</span>`)).join('')+`</div>`;
 if(dh.length) h+=`<div class="dgroup"><h3>Design history to settle</h3><p class="sub">${dh.length}. Someone who knows the ordering history has to answer these; they are not visible in the deposits.</p>`
  +dh.map((d,i)=>item('dec:dh:'+i,`<b>${esc(d.title)}</b><br><span style="color:var(--mut);font-size:13px">${esc(d.why)}</span><br><span class="pill">${(d.parts||[]).map(esc).join(' · ')}</span>`)).join('')+`</div>`;
 if(dr.length) h+=`<div class="dgroup"><h3>Resolutions worth a second look</h3><p class="sub">${dr.length}. Treated as corroborated by a wiki caption, but the arithmetic disagrees.</p>`
  +dr.map((d,i)=>item('dec:rec:'+i,`<b>${esc(d.part)}</b> — ${esc(d.why)}`)).join('')+`</div>`;
 h+=`<div class="dgroup"><h3>Captions with no possible image</h3><p class="sub">${noimg.length}. All 30 wiki pages were searched; these images do not exist.</p>`
  +noimg.map((n,i)=>item('dec:ni:'+i,`<b>${esc(n.part)}</b> ${esc(n.type)} — ${esc(n.label.replace(/^Decide: /,''))}<br><span style="color:var(--mut);font-size:13px">${esc(n.why)}</span>`)).join('')+`</div>`;
 h+=`<div class="dgroup"><h3>Corrections already carried by the pastes</h3><p class="sub">${fixes.length} defects found by checking every cross-reference against the part it points at. Each is baked into the staged body, so pasting the section repairs it. Listed here as the record of what changed.</p>`
  +fixes.map(f=>item('dec:fix:'+f.id,`<b>${esc(f.part)}</b> ${esc(f.type)} — ${esc(f.why)}`)).join('')+`</div>`;
 return h+'</div>';
}

/* ------------------------------------------------ shell */
function htop(){
 const h=document.querySelector('header');
 if(h) document.documentElement.style.setProperty('--htop',h.offsetHeight+'px');
}
addEventListener('resize',htop);
function render(){
 document.getElementById('main').innerHTML=
  view==='queue'?viewQueue():view==='board'?viewBoard():view==='figures'?viewFigures():viewDecisions();
 head(); htop(); savePf();
}
const vis=()=>partWork(curPart());
function focusStep(){
 const el=document.querySelector('.step.focus');
 if(el) el.scrollIntoView({block:'nearest',behavior:'smooth'});
}
function nextOpen(){
 const v=vis();
 for(let i=si;i<v.length;i++) if(!isTick(v[i])) {si=i;return}
 for(let i=0;i<v.length;i++) if(!isTick(v[i])) {si=i;return}
 si=Math.max(0,v.length-1);
}
function goPart(i){const P=parts();pf.pi=Math.max(0,Math.min(i,P.length-1));si=0;view='queue';render();nextOpen();render();window.scrollTo({top:0,behavior:'smooth'})}
function doStep(s,withCopy){
 if(withCopy) copy(payload(s),s.kind==='section'||s.kind==='draft'?'Markdown copied':'Legend copied');
 tick(s,true);
 const v=vis(), at=v.findIndex(x=>x.id===s.id);
 if(at>=0) si=at;
 nextOpen(); render(); focusStep();
}
const byId=id=>STEPS.find(s=>s.id===id);

document.addEventListener('click',e=>{
 const t=e.target;
 const tab=t.closest('#tabs button'); if(tab){view=tab.dataset.v;render();return}
 const w=t.closest('#who button'); if(w){pf.lane=w.dataset.w;pf.pi=0;si=0;render();if(view==='queue'){nextOpen();render()}return}
 const pi=t.closest('[data-pi]'); if(pi&&!pi.disabled){goPart(+pi.dataset.pi);return}
 const pid=t.closest('[data-pid]'); if(pid){const i=parts().indexOf(pid.dataset.pid);if(i>=0)goPart(i);return}
 const go=t.closest('[data-go]'); if(go){doStep(byId(go.dataset.go),true);return}
 const cp=t.closest('[data-cp]'); if(cp){const s=byId(cp.dataset.cp);copy(payload(s),'Copied');return}
 const tk=t.closest('[data-tk]'); if(tk){doStep(byId(tk.dataset.tk),false);return}
 const un=t.closest('[data-un]'); if(un){tick(byId(un.dataset.un),false);render();return}
 const ta=t.closest('[data-tall]'); if(ta){tall[ta.dataset.tall]=!tall[ta.dataset.tall];render();return}
 const ap=t.closest('[data-allp]');
 if(ap){const w=partWork(ap.dataset.allp);w.forEach(s=>tick(s,true));render();toast(w.length+' steps ticked');return}
 const rn=t.closest('[data-ren]');
 if(rn){const v=prompt('Name for lane '+rn.dataset.ren,pf.names[rn.dataset.ren]||rn.dataset.ren);
  if(v){pf.names[rn.dataset.ren]=v.slice(0,18);savePf();render()}return}
 if(t.id==='pexp'){copy(btoa(unescape(encodeURIComponent(JSON.stringify(st)))),'Progress code copied');return}
 if(t.id==='pimp'){const v=prompt('Paste a progress code — it merges with what is here');
  if(v){try{Object.assign(st,JSON.parse(decodeURIComponent(escape(atob(v.trim())))));save();render();toast('Progress merged')}catch(err){toast('That code did not read')}}return}
 if(t.id==='prep'){
  const L=['ReLEAF registry — '+new Date().toLocaleString()];
  ['A','B'].forEach(k=>{const r=STEPS.filter(s=>s.who===k&&s.bucket==='req');
   L.push(`lane ${nm(k)}: ${r.filter(isTick).length}/${r.length} required steps`)});
  L.push('');
  ORDER.forEach(p=>{const w=STEPS.filter(s=>s.part===p&&actionable(s)&&s.bucket==='req');
   const d=w.filter(isTick).length;
   L.push(`${d===w.length?'[x]':'[ ]'} ${p}  ${d}/${w.length}  ${CARDS[p].title||''}`)});
  copy(L.join('\n'),'Status report copied');return}
 if(t.id==='pclr'){if(confirm('Clear every tick in this browser?')){st={};save();render()}return}
 const im=t.closest('img[data-full]');
 if(im){const dl=document.getElementById('lb');dl.querySelector('img').src=im.dataset.full;dl.showModal();return}
 if(t.closest('#lb')){document.getElementById('lb').close();return}
 const jr=t.closest('#jres li'); if(jr){document.getElementById('jump').close();goPart(+jr.dataset.i);return}
});
document.addEventListener('change',e=>{
 if(e.target.id==='optx'){pf.opt=e.target.checked;savePf();si=0;render();return}
 const c=e.target.closest('input[data-k]'); if(!c) return;
 if(c.checked) st[c.dataset.k]=true; else delete st[c.dataset.k];
 save(); c.closest('.ditem').classList.toggle('done',c.checked);
});

/* jump palette */
function jopen(){
 const d=document.getElementById('jump'); document.getElementById('jq').value=''; jfill(''); d.showModal();
 document.getElementById('jq').focus();
}
let jsel=0;
function jfill(q){
 q=q.trim().toLowerCase();
 const P=parts();
 const hit=P.map((p,i)=>({p,i,c:CARDS[p]})).filter(o=>!q
  ||o.p.toLowerCase().includes(q)||(o.c.title||'').toLowerCase().includes(q)
  ||('tier '+o.c.tier).toLowerCase().includes(q)||(o.c.grp||'').toLowerCase().includes(q)).slice(0,40);
 jsel=0;
 document.getElementById('jres').innerHTML=hit.map((o,k)=>{
  const w=partWork(o.p), d=w.filter(isTick).length;
  return `<li data-i="${o.i}" aria-selected="${k===0}"><span class="jid">${o.p}</span>
   <span class="jt">${esc(o.c.title||'')}</span><span class="pill">${d}/${w.length}</span></li>`}).join('')
  ||'<li><span class="jt">no part matches</span></li>';
}
document.getElementById('jq').addEventListener('input',e=>jfill(e.target.value));
document.getElementById('jq').addEventListener('keydown',e=>{
 const li=[...document.querySelectorAll('#jres li[data-i]')];
 if(e.key==='ArrowDown'||e.key==='ArrowUp'){
  e.preventDefault(); jsel=Math.max(0,Math.min(li.length-1,jsel+(e.key==='ArrowDown'?1:-1)));
  li.forEach((n,k)=>n.setAttribute('aria-selected',k===jsel)); li[jsel]&&li[jsel].scrollIntoView({block:'nearest'});
 } else if(e.key==='Enter'){
  e.preventDefault(); if(li[jsel]){document.getElementById('jump').close();goPart(+li[jsel].dataset.i)}
 }
});

document.addEventListener('keydown',e=>{
 if(e.metaKey||e.ctrlKey||e.altKey){
  if((e.metaKey||e.ctrlKey)&&e.key.toLowerCase()==='k'){e.preventDefault();jopen()}
  return}
 if(/^(INPUT|TEXTAREA|SELECT)$/.test(e.target.tagName)) return;
 if(document.querySelector('dialog[open]')&&e.key!=='Escape') return;
 const k=e.key.toLowerCase();
 if(k==='/'||e.code==='Slash'){e.preventDefault();jopen();return}
 if(k==='?'){document.getElementById('help').showModal();return}
 if(e.key==='Escape'){[...document.querySelectorAll('dialog[open]')].forEach(d=>d.close());return}
 if('1234'.includes(e.key)){view=['queue','board','figures','decisions'][+e.key-1];render();return}
 if(view!=='queue') return;
 const P=parts(), v=vis();
 if(e.key==='ArrowRight'||k===']'){goPart(pf.pi+1);return}
 if(e.key==='ArrowLeft'||k==='['){goPart(pf.pi-1);return}
 if(k==='g'){const i=P.findIndex(p=>!fin(p));if(i>=0)goPart(i);else toast('Every part in this lane is done');return}
 if(k==='o'){const a=document.getElementById('openp');if(a)window.open(a.href,'_blank','noopener');return}
 if(!v.length) return;
 if(k==='j'||e.key==='ArrowDown'){e.preventDefault();si=Math.min(si+1,v.length-1);render();focusStep();return}
 if(k==='k'||e.key==='ArrowUp'){e.preventDefault();si=Math.max(si-1,0);render();focusStep();return}
 const s=v[si]; if(!s) return;
 if(e.key==='Enter'||k==='c'){e.preventDefault();doStep(s,true);return}
 if(k==='x'){tick(s,!isTick(s));if(isTick(s))nextOpen();render();focusStep();return}
 if(k==='f'){const a=document.querySelector(`.step[data-id="${s.id}"] a[download]`);if(a)a.click();return}
 if(k==='u'){const prev=v.slice(0,si+1).reverse().find(isTick);if(prev){tick(prev,false);render()}return}
});

/* open where you stopped */
(function start(){
 const P=parts();
 if(!(pf.pi>=0&&pf.pi<P.length)) pf.pi=0;
 if(fin(P[pf.pi])){const i=P.findIndex(p=>!fin(p)); if(i>=0) pf.pi=i}
 render(); nextOpen(); render();
})();
</script></body></html>
"""

out = ROOT / "console.html"
out.write_text(HTML.replace("%%DATA%%", DATA), encoding="utf-8")
print("wrote console.html", round(out.stat().st_size / 1024), "KB")
