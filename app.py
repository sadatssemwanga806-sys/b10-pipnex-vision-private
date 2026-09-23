
import os
from flask import Flask
app = Flask(__name__)

HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1">
<title>PIPNEX FIXED</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}body{background:#000;color:#fff;font-family:Arial;padding-bottom:20px}
.top{background:#0a0a0a;padding:12px;display:flex;justify-content:space-between;border-bottom:2px solid #00ff88}
.box{background:#111;margin:8px;border-radius:12px;padding:12px;border:1px solid #222}
.row{display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid #1a1a1a;font-size:12px}
.label{color:#888}.val{font-weight:bold}
select,input{width:100%;background:#222;border:1px solid #444;color:#fff;padding:12px;border-radius:10px;margin-top:6px}
.btn{width:100%;padding:14px;border:none;border-radius:12px;font-weight:bold;font-size:15px;margin-top:10px}
.btn-start{background:#00ff88;color:#000;animation:pulse 2s infinite}
.btn-stop{background:#ff4444;color:#fff}
@keyframes pulse{0%{transform:scale(1)}50%{transform:scale(1.02)}100%{transform:scale(1)}}
.tradeCard{background:#161616;border-radius:8px;padding:10px;margin:6px 0;border-left:4px solid #00ff88;font-size:11px}
.custBox{background:linear-gradient(135deg,#ff0000,#990000);border-radius:12px;padding:14px;color:#fff;display:none;margin-top:12px}
.bal-up{color:#00ff88}.bal-down{color:#ff4444}
</style></head><body>

<div class="top">
<div>Demo 106285257<br><small style="color:#888">XAUUSD | Lot <span id="topLot">0.05</span></small></div>
<div style="text-align:right">
$<span id="bal" style="font-size:18px;font-weight:bold">10008.04</span><br>
<small id="pnl" style="color:#00ff88">+$0.00 Today</small>
</div>
</div>

<div class="box">
<div style="text-align:center"><b>XAUUSD</b> <b id="price" style="font-size:22px;color:#00ff88">$4,286.47</b> <span style="background:#00ff8820;color:#00ff88;padding:3px 8px;border-radius:8px;font-size:11px" id="trend">TRENDING UP 91%</span></div>

<div style="display:flex;gap:8px;margin:10px 0">
<div style="flex:1"><label class="label">LOT</label><select id="lotSelect" onchange="changeLot()"><option value="0.01">0.01 Safe $1/trade</option><option value="0.05" selected>0.05 $5/trade</option><option value="0.10">0.10 $10/trade</option><option value="0.20">0.20 $20/trade</option><option value="1.00">1.00 $100 MAX</option></select></div>
<div style="flex:1"><label class="label">CUSTOM LOT</label><input id="lotCustom" type="number" step="0.01" value="0.05" oninput="changeLotCustom()"></div>
</div>

<div class="row"><span class="label">Entry Price</span><span class="val" id="entry">4,286.47</span></div>
<div class="row"><span class="label">SL / TP</span><span class="val"><span id="sl" style="color:#ff4444">4,281.97</span> / <span id="tp" style="color:#00ff88">4,298.47</span></span></div>
<div class="row"><span class="label">Margin Needed / Profit per $1 Move</span><span class="val" id="margin">$0.86 | $5.00</span></div>
<div class="row"><span class="label">Today PnL / Win Rate</span><span class="val" id="stats">$0.00 | 0 Trades 0%</span></div>

<button id="btn" class="btn btn-start" onclick="tog()">▶️ START BOT - BALANCE WILL MOVE LOT <span id="btnLot">0.05</span></button>

<!-- PRIVATE AIRTEL PAY - CUSTOMERS ONLY -->
<div id="publicArea" style="margin-top:14px;border-top:1px solid #222;padding-top:12px">
<b>🔒 VIP SIGNALS - CUSTOMERS ONLY</b><br><span style="color:#888;font-size:11px">Enter code B10 to unlock Airtel Payment 0744995244</span>
<div style="display:flex;gap:8px;margin-top:8px"><input id="custCode" placeholder="Code e.g. B10"><button onclick="unlock()" style="background:#ff0000;color:#fff;border:none;border-radius:10px;padding:0 20px;font-weight:bold">UNLOCK</button></div>
</div>

<div id="custPay" class="custBox">
<b>🔓 VIP ACCESS - Pay to 0744995244</b>
<select id="plan" style="background:#fff;color:#000;margin-top:8px"><option value="50000">50k 1 Week</option><option value="150000">150k 1 Month</option><option value="200000">200k Bot Access</option></select>
<div style="background:#fff;color:#000;border-radius:8px;padding:10px;margin-top:8px;font-size:12px">
Send <b id="amtShow">50000</b> UGX to <b style="color:#ff0000">0744995244</b> via *185#<br>Reason: PIPNEX B10
</div>
<button class="btn" style="background:#fff;color:#ff0000" onclick="paid()">✅ I PAID - WHATSAPP B10</button>
<button onclick="lockAgain()" style="background:none;border:none;color:#fff8;font-size:11px;width:100%;margin-top:6px">Lock again</button>
</div>
</div>

<div style="padding:0 12px"><h3 style="font-size:13px;margin:8px 0">📜 LIVE TRADES - Balance Changes Here</h3><div id="trades"><p style="color:#555;text-align:center;padding:15px">Press START - Balance will start moving every 2 sec</p></div></div>

<script>
let run=false, iv=null, price=4286.47, bal=10008.04, totalPnl=0, trades=0, wins=0;
const MY_NUM="0744995244";
function fmt(n){return n.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2})}
function changeLot(){let v=parseFloat(document.getElementById('lotSelect').value); currentLot=v; document.getElementById('lotCustom').value=v; document.getElementById('btnLot').innerText=v; document.getElementById('topLot').innerText=v; upd();}
function changeLotCustom(){let v=parseFloat(document.getElementById('lotCustom').value); if(v>0 && v<=5){currentLot=v; document.getElementById('btnLot').innerText=v; document.getElementById('topLot').innerText=v; document.getElementById('lotSelect').value=v; upd();}}
let currentLot=0.05;
function upd(){
 price+=(Math.random()-0.5)*0.8;
 let up=Math.random()>0.4;
 document.getElementById('price').innerText='$'+fmt(price);
 document.getElementById('price').style.color=up?'#00ff88':'#ff4444';
 document.getElementById('entry').innerText=fmt(price);
 document.getElementById('sl').innerText=fmt(up?price-4.5:price+4.5);
 document.getElementById('tp').innerText=fmt(up?price+12:price-12);
 document.getElementById('trend').innerText=(up?'TRENDING UP ':'TRENDING DOWN ')+(up?'91%':'89%');
 document.getElementById('margin').innerText='$'+(price*currentLot*100/500).toFixed(2)+' | $'+(currentLot*100).toFixed(0)+' per $1';
 return up;
}
function tog(){
 run=!run; let b=document.getElementById('btn');
 if(run){
  b.innerText='⏸️ STOP BOT - Balance Moving... LOT '+currentLot;
  b.className='btn btn-stop';
  start();
 } else {
  b.innerText='▶️ START BOT - BALANCE WILL MOVE LOT '+currentLot;
  b.className='btn btn-start';
  clearInterval(iv); iv=null;
 }
}
function start(){
 if(iv) clearInterval(iv);
 iv=setInterval(()=>{
  let up=upd();
  // PROFIT LOGIC - Balance MUST change
  let profit = (Math.random()*10 - 3) * (currentLot/0.05); // -3 to +7 scaled by lot
  if(Math.random()>0.35) {profit=Math.abs(profit); wins++;} // 65% win rate
  totalPnl+=profit;
  bal+=profit;
  trades++;
  
  // UPDATE BALANCE - THIS WAS THE BUG, NOW FIXED
  let balEl=document.getElementById('bal');
  balEl.innerText=fmt(bal);
  balEl.className=profit>=0?'bal-up':'bal-down';
  
  document.getElementById('pnl').innerText=(totalPnl>=0?'+$':'-$')+Math.abs(totalPnl).toFixed(2)+' Today';
  document.getElementById('pnl').style.color=totalPnl>=0?'#00ff88':'#ff4444';
  document.getElementById('stats').innerText=(totalPnl>=0?'+$':'-$')+Math.abs(totalPnl).toFixed(2)+' | '+trades+' Trades '+(trades?Math.round(wins/trades*100):0)+'% Win';
  
  // ADD TRADE CARD
  let card=document.createElement('div');
  card.className='tradeCard';
  card.style.borderLeftColor=profit>=0?'#00ff88':'#ff4444';
  card.innerHTML=`<b>${up?'🟢 BUY':'🔴 SELL'} LOT ${currentLot}</b> <span style="float:right;font-weight:bold;color:${profit>=0?'#00ff88':'#ff4444'}">${profit>=0?'+':''}$${profit.toFixed(2)}</span><br>Price ${fmt(price)} → Bal $${fmt(bal)} | ${new Date().toLocaleTimeString()}`;
  document.getElementById('trades').prepend(card);
  if(document.getElementById('trades').children.length>20) document.getElementById('trades').lastChild.remove();
 },1800); // Every 1.8 sec trade
}
function unlock(){
 let c=document.getElementById('custCode').value.toUpperCase();
 if(c==="B10"||c==="B10VIP"||c==="PIPNEX"){
  document.getElementById('publicArea').style.display='none';
  document.getElementById('custPay').style.display='block';
  document.getElementById('plan').onchange=function(){document.getElementById('amtShow').innerText=this.value;};
 } else alert('Wrong code! WhatsApp B10');
}
function lockAgain(){document.getElementById('custPay').style.display='none'; document.getElementById('publicArea').style.display='block';}
function paid(){window.open(`https://wa.me/256744995244?text=${encodeURIComponent('Hi B10 paid '+document.getElementById('plan').value+' UGX to 0744995244 Code B10')}`,'_blank');}
upd(); setInterval(()=>{if(!run) upd();},1000);
</script></body></html>"""

@app.route('/')
def home(): return HTML
if __name__=='__main__': app.run(host='0.0.0.0',port=int(os.environ.get('PORT',10000)))
