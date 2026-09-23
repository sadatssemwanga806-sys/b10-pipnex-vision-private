
import os
from flask import Flask
app = Flask(__name__)

HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1">
<title>PIPNEX LOT FIX</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}body{background:#000;color:#fff;font-family:Arial}
.top{background:#0a0a0a;padding:10px;display:flex;justify-content:space-between;border-bottom:1px solid #222}
.grid{display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:6px;padding:8px;background:#050505}
.grid b{font-size:12px}.grid span{color:#777;font-size:9px;display:block}
.box{background:#111;margin:8px;border-radius:12px;padding:12px;border:1px solid #222}
.row{display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid #1a1a1a;font-size:12px}
.label{color:#888}.val{color:#fff;font-weight:bold}
input,select{background:#222;border:1px solid #444;color:#00ff88;padding:8px;border-radius:8px;width:100%;margin-top:4px;font-weight:bold}
.lotRow{display:flex;gap:8px;margin:10px 0}
.lotRow div{flex:1}
.btn{width:100%;padding:14px;border:none;border-radius:12px;font-weight:bold;font-size:16px}
.btn-start{background:#00ff88;color:#000}.btn-stop{background:#ff4444;color:#fff}
.buy{color:#00ff88}.sell{color:#ff4444}
.tradeCard{background:#161616;border-radius:8px;padding:10px;margin:6px 0;border-left:4px solid #00ff88;font-size:11px}
</style></head><body>

<div class="top"><b>Demo 106285257</b><b>$<span id="bal">10,008.04</span></b></div>
<div class="grid">
<div><span>Balance</span><b id="gBal">10,008.04</b></div>
<div><span>Equity</span><b id="gEq">10,008.04</b></div>
<div><span>Free</span><b>10,008.04</b></div>
<div><span>P&L</span><b id="gPnL" class="buy">0.00</b></div>
</div>

<div class="box">
<div style="text-align:center"><b>XAUUSD</b> <b id="price" style="font-size:20px;color:#00ff88">$4,286.47</b> <span id="trend" style="background:#00ff8820;color:#00ff88;padding:2px 6px;border-radius:8px;font-size:10px">TRENDING UP 91%</span></div>

<!-- LOT SIZE CONTROLS - NOW WORKING!!! -->
<div class="lotRow">
<div><label class="label">LOT SIZE (Change Here)</label>
<select id="lotSelect" onchange="changeLot()">
<option value="0.01">0.01 - $1 per $1 (Safe)</option>
<option value="0.02">0.02 - $2 per $1</option>
<option value="0.05" selected>0.05 - $5 per $1 (Your Current)</option>
<option value="0.10">0.10 - $10 per $1 (Aggressive)</option>
<option value="0.20">0.20 - $20 per $1 (Pro)</option>
<option value="0.50">0.50 - $50 per $1 (Boss)</option>
<option value="1.00">1.00 - $100 per $1 (B10 MAX)</option>
</select>
</div>
<div><label class="label">CUSTOM LOT</label><input id="lotCustom" type="number" step="0.01" value="0.05" placeholder="0.05" oninput="changeLotCustom()"></div>
</div>

<div class="row"><span class="label">Entry Price</span><span class="val" id="entry">4,286.47</span></div>
<div class="row"><span class="label">Stop Loss SL</span><span class="val" style="color:#ff4444" id="sl">4,281.97 (-$22.50)</span></div>
<div class="row"><span class="label">Take Profit TP</span><span class="val" style="color:#00ff88" id="tp">4,298.47 (+$60.00)</span></div>
<div class="row"><span class="label">Margin Needed</span><span class="val" id="margin">$0.86</span></div>
<div class="row"><span class="label">Risk % / Lot Value</span><span class="val" id="risk">Risk 1.2% | $5 per $1</span></div>
<div class="row"><span class="label">RSI / EMA / Signal</span><span class="val" id="indi">RSI 70.44 | EMA Bull | BUY 91%</span></div>

<button id="btn" class="btn btn-start" onclick="tog()">▶️ START BOT - LOT <span id="btnLot">0.05</span></button>
</div>

<div style="padding:0 12px 80px 12px"><h3 style="font-size:13px;margin:8px 0">📜 LIVE TRADES WITH YOUR LOT SIZE</h3><div id="trades"><p style="color:#555;text-align:center;padding:20px">Change Lot Above → Click START → See trades with your lot</p></div></div>

<script>
let run=false, iv=null, price=4286.47, bal=10008.04, pnl=0, currentLot=0.05;
function fmt(n){return n.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2})}
function changeLot(){ currentLot=parseFloat(document.getElementById('lotSelect').value); document.getElementById('lotCustom').value=currentLot; document.getElementById('btnLot').innerText=currentLot; upd(); }
function changeLotCustom(){ let v=parseFloat(document.getElementById('lotCustom').value); if(v>0 && v<=5){ currentLot=v; document.getElementById('lotSelect').value=v; document.getElementById('btnLot').innerText=v; upd(); } }
function upd(){
 price+=(Math.random()-0.5)*1.2;
 let up=Math.random()>0.42;
 let rsi=(up?68+Math.random()*10:32+Math.random()*10).toFixed(2);
 let sl=up?price-4.5:price+4.5;
 let tp=up?price+12:price-12;
 let slMoney=(4.5*currentLot*100).toFixed(2);
 let tpMoney=(12*currentLot*100).toFixed(2);
 let margin=(price*currentLot*100/500).toFixed(2);
 let perDollar=(currentLot*100).toFixed(0);
 document.getElementById('price').innerText='$'+fmt(price);
 document.getElementById('price').style.color=up?'#00ff88':'#ff4444';
 document.getElementById('trend').innerText=(up?'TRENDING UP ':'TRENDING DOWN ')+(up?'91%':'89%');
 document.getElementById('entry').innerText=fmt(price)+' (Lot '+currentLot+')';
 document.getElementById('sl').innerText=fmt(sl)+' (-$'+slMoney+')';
 document.getElementById('tp').innerText=fmt(tp)+' (+$'+tpMoney+')';
 document.getElementById('margin').innerText='$'+margin+' | Leverage 1:500 | Acc 106285257';
 document.getElementById('risk').innerText='Risk '+((currentLot/0.05*1.2).toFixed(1))+'% | $'+perDollar+' per $1 move | Lot '+currentLot;
 document.getElementById('indi').innerText='RSI '+rsi+' | '+(up?'EMA Bull':'EMA Bear')+' | '+(up?'BUY':'SELL')+' '+(up?'91%':'89%');
 return {p:price,up:up,sl:sl,tp:tp,slM:slMoney,tpM:tpMoney,rsi:rsi,margin:margin,per:perDollar};
}
function tog(){
 run=!run; let b=document.getElementById('btn');
 if(run){b.innerText='⏸️ STOP - LOT '+currentLot+' LIVE'; b.className='btn btn-stop'; start();}
 else{b.innerText='▶️ START BOT - LOT '+currentLot; b.className='btn btn-start'; clearInterval(iv);}
}
function start(){
 iv=setInterval(()=>{
  let d=upd();
  let pf=(Math.random()*8-2)*(currentLot/0.05);
  pnl+=pf; bal+=pf;
  document.getElementById('bal').innerText=fmt(bal);
  document.getElementById('gBal').innerText=fmt(bal);
  document.getElementById('gEq').innerText=fmt(bal);
  document.getElementById('gPnL').innerText=(pnl>=0?'+$':'-$')+Math.abs(pnl).toFixed(2);
  let card=document.createElement('div'); card.className='tradeCard'; card.style.borderLeftColor=d.up?'#00ff88':'#ff4444';
  card.innerHTML=`<b>${d.up?'🟢 BUY':'🔴 SELL'} XAUUSD LOT ${currentLot}</b> <span style="float:right;color:${pf>=0?'#00ff88':'#ff4444'}">${pf>=0?'+':''}${pf.toFixed(2)}</span><br>
  Entry ${fmt(d.p)} | SL ${fmt(d.sl)} (-$${d.slM}) | TP ${fmt(d.tp)} (+$${d.tpM})<br>
  Margin $${d.margin} | $${d.per}/$1 | RSI ${d.rsi} | ${new Date().toLocaleTimeString()} | ● LOT ${currentLot}`;
  document.getElementById('trades').prepend(card);
 },2800);
}
upd(); setInterval(()=>{if(!run) upd();},1000);
</script></body></html>"""

@app.route('/')
def home(): return HTML
if __name__=='__main__': app.run(host='0.0.0.0',port=int(os.environ.get('PORT',10000)))
