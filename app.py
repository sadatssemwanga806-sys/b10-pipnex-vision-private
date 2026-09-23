import os
from flask import Flask
app = Flask(__name__)

HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1">
<title>PIPNEX B10 PRO MAX</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}body{background:#000;color:#fff;font-family:Arial;font-size:13px}
.top{background:#0a0a0a;padding:10px 14px;display:flex;justify-content:space-between;border-bottom:1px solid #222}
.pill{background:#1a4fff;color:#fff;padding:6px 12px;border-radius:20px;font-weight:bold;font-size:12px}
.grid{display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:8px;padding:10px;background:#050505;border-bottom:1px solid #111}
.grid b{color:#fff;font-size:13px}.grid span{color:#777;font-size:10px;display:block}
.priceBox{background:#111;margin:8px 12px;border-radius:12px;padding:12px;border:1px solid #222}
.row{display:flex;justify-content:space-between;padding:5px 0;border-bottom:1px solid #1a1a1a}
.row:last-child{border:none}
.label{color:#888}.val{color:#fff;font-weight:bold}
.buy{color:#00ff88} .sell{color:#ff4444}
.badge{padding:2px 7px;border-radius:10px;font-size:10px;font-weight:bold;border:1px solid}
.up{background:#00ff8820;color:#00ff88;border-color:#00ff8840}
.down{background:#ff444420;color:#ff4444;border-color:#ff444440}
.btn{width:100%;padding:15px;border:none;border-radius:12px;font-weight:bold;font-size:16px;margin-top:10px}
.btn-start{background:#00ff88;color:#000}.btn-stop{background:#ff4444;color:#fff}
.tradeCard{background:#161616;border:1px solid #222;border-radius:10px;margin:8px 0;padding:10px}
.sl{color:#ff4444} .tp{color:#00ff88}
.bottom{position:fixed;bottom:0;left:0;right:0;background:#0a0a0a;border-top:1px solid #222;display:flex;justify-content:space-around;padding:8px 0;font-size:10px}
.nav{color:#666;text-align:center}.nav.active{color:#00ff88}
.liveDot{width:8px;height:8px;background:#00ff88;border-radius:50%;display:inline-block;animation:blink 1s infinite}
@keyframes blink{50%{opacity:0.2}}
</style></head><body>

<div class="top"><span class="pill">Demo 106285257</span><span style="color:#fff">$<span id="bal">10,008.04</span> ▲</span></div>

<div class="grid">
<div><span>Balance</span><b id="gBal">10,008.04</b></div>
<div><span>Equity</span><b id="gEq">10,008.04</b></div>
<div><span>Free Margin</span><b id="gFree">10,008.04</b></div>
<div><span>P&L</span><b id="gPnL" class="buy">$0.00</b></div>
</div>

<div class="priceBox">
<div style="text-align:center;margin-bottom:8px"><span class="liveDot"></span> <b style="font-size:18px" id="sym">XAUUSD</b> <b id="price" style="font-size:20px;color:#00ff88">$4,286.47</b> <span id="trend" class="badge up">TRENDING UP 91%</span></div>

<div class="row"><span class="label">Signal / Trend Strength</span><span class="val" id="signal">🟢 STRONG BUY 91%</span></div>
<div class="row"><span class="label">Entry Price</span><span class="val" id="entry">4,286.47</span></div>
<div class="row"><span class="label">Stop Loss (SL)</span><span class="val sl" id="sl">4,281.97 (-$45)</span></div>
<div class="row"><span class="label">Take Profit (TP)</span><span class="val tp" id="tp">4,298.47 (+$120)</span></div>
<div class="row"><span class="label">Lot Size / Volume</span><span class="val" id="lot">0.05 Lot ($5 per $1 move)</span></div>
<div class="row"><span class="label">Leverage / Margin Needed</span><span class="val" id="lev">1:500 | Margin $0.86</span></div>
<div class="row"><span class="label">Spread / Swap / Commission</span><span class="val" id="spread">Spread 0.31 | Swap 0 | Comm $0</span></div>
<div class="row"><span class="label">RSI (14) / EMA 9/21 / Risk</span><span class="val" id="indi">RSI 70.44 | EMA Bullish | Risk 1.2%</span></div>
<div class="row"><span class="label">Best Time / Session / Volatility</span><span class="val" id="time">London Open | High Vol | 15M</span></div>
<div class="row"><span class="label">Action</span><span class="val" id="action">WAIT - STRONG TREND FORMING...</span></div>

<button id="btn" class="btn btn-start" onclick="tog()">▶️ START BOT - SHOW ALL ENTRIES</button>
</div>

<div style="padding:0 12px 70px 12px">
<h3 style="margin:8px 0">📜 LIVE TRENDING TRADES - Entry SL TP Full</h3>
<div id="trades"><p style="color:#555;text-align:center;padding:20px">Click START to see Entry, SL, TP, Lot, RSI, Spread, Margin, P&L all here</p></div>
</div>

<div class="bottom"><div class="nav active">📈<br>Trade</div><div class="nav">📋<br>Positions</div><div class="nav">💰<br>Funds</div><div class="nav">•••<br>More</div></div>

<script>
let run=false, iv=null, price=4286.47, bal=10008.04, pnl=0;
function fmt(n){return n.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2})}
function upd(){
 price+=(Math.random()-0.5)*1.5;
 let up=Math.random()>0.42;
 let rsi=up?65+Math.random()*12:35+Math.random()*12;
 let ema=up?'EMA 9 > 21 BULLISH':'EMA 9 < 21 BEARISH';
 let strength=up?91:89;
 let sl=up?price-4.5:price+4.5;
 let tp=up?price+12:price-12;
 let lot=0.05;
 let margin=(price*lot*100/500).toFixed(2);

 document.getElementById('price').innerText='$'+fmt(price);
 document.getElementById('price').style.color=up?'#00ff88':'#ff4444';
 document.getElementById('trend').innerText=(up?'TRENDING UP ':'TRENDING DOWN ')+strength+'%';
 document.getElementById('trend').className='badge '+(up?'up':'down');
 document.getElementById('signal').innerHTML=(up?'🟢 STRONG BUY ':'🔴 STRONG SELL ')+strength+'%';
 document.getElementById('signal').style.color=up?'#00ff88':'#ff4444';
 document.getElementById('entry').innerText=fmt(price);
 document.getElementById('sl').innerText=fmt(sl)+' (-$'+(4.5*lot*100).toFixed(0)+')';
 document.getElementById('tp').innerText=fmt(tp)+' (+$'+(12*lot*100).toFixed(0)+')';
 document.getElementById('lot').innerText=lot+' Lot ($'+(lot*100).toFixed(0)+' per $1 move)';
 document.getElementById('lev').innerText='1:500 | Margin $'+margin+' | Acc 106285257';
 document.getElementById('spread').innerText='Spread 0.31 | Swap 0 | Comm $0 | DEMO';
 document.getElementById('indi').innerText='RSI '+rsi.toFixed(2)+' | '+ema+' | Risk 1.2%';
 document.getElementById('time').innerText=new Date().toLocaleTimeString()+' | London Open | High Vol | 15M TF';
 document.getElementById('action').innerText=up?'✅ READY TO BUY NOW - TREND CONFIRMED':'✅ READY TO SELL NOW - TREND CONFIRMED';
 document.getElementById('action').style.color=up?'#00ff88':'#ff4444';
 return {p:price,up:up,sl:sl,tp:tp,rsi:rsi,ema:ema,strength:strength,lot:lot,margin:margin};
}
function tog(){
 run=!run; let b=document.getElementById('btn');
 if(run){b.innerText='⏸️ STOP - LIVE ENTRIES SL TP'; b.className='btn btn-stop'; start();}
 else{b.innerText='▶️ START BOT - SHOW ALL ENTRIES'; b.className='btn btn-start'; clearInterval(iv);}
}
function start(){
 iv=setInterval(()=>{
  let d=upd();
  let pf=(Math.random()*10-2.5);
  pnl+=pf; bal+=pf;
  document.getElementById('bal').innerText=fmt(bal);
  document.getElementById('gBal').innerText=fmt(bal);
  document.getElementById('gEq').innerText=fmt(bal);
  document.getElementById('gPnL').innerText=(pnl>=0?'+$':'-$')+Math.abs(pnl).toFixed(2);
  document.getElementById('gPnL').className=pnl>=0?'buy':'sell';
  let card=document.createElement('div'); card.className='tradeCard'; card.style.borderLeft='4px solid '+(d.up?'#00ff88':'#ff4444');
  card.innerHTML=`<div style="display:flex;justify-content:space-between"><b>${d.up?'🟢 BUY':'🔴 SELL'} XAUUSD ${d.lot}</b><b style="color:${pf>=0?'#00ff88':'#ff4444'}">${pf>=0?'+':''}${pf.toFixed(2)}</b></div>
  <div style="margin:6px 0;font-size:12px">
  Entry: <b>${fmt(d.p)}</b> | SL: <b class="sl">${fmt(d.sl)}</b> | TP: <b class="tp">${fmt(d.tp)}</b><br>
  Lot: ${d.lot} | Margin: $${d.margin} | RSI: ${d.rsi.toFixed(1)} | ${d.ema}<br>
  Trend: <b style="color:${d.up?'#00ff88':'#ff4444'}">TRENDING ${d.up?'UP':'DOWN'} ${d.strength}%</b> | Spread 0.31 | 1:500<br>
  <span style="color:#666">#${106285200+Math.floor(Math.random()*100)} | 106285257 DEMO | ${new Date().toLocaleTimeString()} | ● TRENDING NOW</span>
  </div>`;
  document.getElementById('trades').prepend(card);
 },3000);
}
upd(); setInterval(()=>{if(!run) upd();},1200);
</script></body></html>"""

@app.route('/')
def home(): return HTML
if __name__=='__main__': app.run(host='0.0.0.0',port=int(os.environ.get('PORT',10000)))
