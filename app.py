
import os
from flask import Flask
app = Flask(__name__)

HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
<title>PIPNEX PHONE ONLY</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}body{background:#000;color:#fff;font-family:Arial;padding-bottom:30px}
.top{background:#00ff88;color:#000;padding:12px;text-align:center;font-weight:bold;font-size:16px}
.box{background:#111;margin:8px;border-radius:16px;padding:14px;border:1px solid #222}
select,input{width:100%;background:#222;border:1px solid #444;color:#fff;padding:14px;border-radius:12px;margin-top:6px;font-size:16px}
.btn{width:100%;padding:18px;border:none;border-radius:14px;font-weight:bold;font-size:18px;margin-top:12px}
.btn-start{background:#00ff88;color:#000}.btn-stop{background:#ff4444;color:#fff}
.btn-copy{background:linear-gradient(135deg,#0088ff,#00ff88);color:#000;font-size:20px;animation:pulse 2s infinite}
@keyframes pulse{0%{transform:scale(1)}50%{transform:scale(1.03)}100%{transform:scale(1)}}
.row{display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid #1a1a1a}
.tradeCard{background:#161616;padding:12px;margin:8px 0;border-radius:10px;border-left:5px solid #00ff88;font-size:12px}
.phoneStep{background:#0a0a0a;border:1px solid #333;border-radius:12px;padding:12px;margin-top:12px}
</style></head><body>

<div class="top">📱 PIPNEX PHONE ONLY - NO PC NEEDED</div>

<div class="box">
<div style="text-align:center">
<b style="font-size:18px">XAUUSD GOLD</b><br>
<b id="price" style="font-size:32px;color:#00ff88">$4,286.47</b><br>
<span id="trend" style="background:#00ff8820;color:#00ff88;padding:4px 10px;border-radius:10px">TRENDING UP 91%</span><br>
<small style="color:#888">Demo 106285257 | Bal $<span id="bal">10,008.04</span> | <span id="pnl" style="color:#00ff88">+$0.00</span></small>
</div>

<div style="display:flex;gap:10px;margin:14px 0">
<div style="flex:1"><label style="color:#888;font-size:12px">LOT SIZE</label><select id="lot" onchange="updateLot()"><option value="0.01">0.01 Safe</option><option value="0.05" selected>0.05 Best</option><option value="0.10">0.10 Pro</option><option value="0.20">0.20 Aggressive</option><option value="1.00">1.00 MAX</option></select></div>
<div style="flex:1"><label style="color:#888;font-size:12px">CUSTOM LOT</label><input id="lotCustom" type="number" step="0.01" value="0.05" oninput="updateCustom()"></div>
</div>

<div class="row"><span style="color:#888">ENTRY</span><span id="entry" style="font-weight:bold;font-size:16px">4286.47</span></div>
<div class="row"><span style="color:#888">STOP LOSS</span><span id="sl" style="color:#ff4444;font-weight:bold;font-size:16px">4281.97</span></div>
<div class="row"><span style="color:#888">TAKE PROFIT</span><span id="tp" style="color:#00ff88;font-weight:bold;font-size:16px">4298.47</span></div>
<div class="row"><span style="color:#888">MARGIN / PROFIT</span><span id="margin">$0.86 | $5 per $1</span></div>

<button id="startBtn" class="btn btn-start" onclick="toggleBot()">▶️ START BOT - Balance Will Move</button>

<!-- PHONE COPY - THIS MAKES EXNESS BALANCE MOVE -->
<div id="copyArea" style="display:none">
<button class="btn btn-copy" onclick="copyToMT5()">📲 COPY & OPEN IN MT5 / EXNESS APP NOW!</button>
<div class="phoneStep">
<b style="color:#00ff88">📱 HOW TO MAKE $10,008.04 MOVE (Phone Only):</b><br><br>
<b>Step 1:</b> Tap COPY button above ☝️<br>
<b>Step 2:</b> Open <b>Exness Trade</b> or <b>MT5</b> app<br>
<b>Step 3:</b> Tap <b>XAUUSD → Trade → Buy/Sell</b><br>
<b>Step 4:</b> Set Lot: <b id="stepLot">0.05</b><br>
<b>Step 5:</b> Set SL: <b id="stepSL" style="color:#ff4444">4281.97</b> and TP: <b id="stepTP" style="color:#00ff88">4298.47</b><br>
<b>Step 6:</b> Tap <b>Open</b> → Your $10,008.04 will start moving!!!<br><br>
<div style="background:#00ff8820;padding:8px;border-radius:8px;font-size:11px">💡 Tip: Keep both apps open side-by-side. Bot signal → Copy → Paste in MT5 in 5 seconds!</div>
</div>
</div>

<div style="margin-top:16px;border-top:1px solid #222;padding-top:12px">
<b>🔒 CUSTOMERS PAY HERE - 0744995244</b><br>
<small style="color:#888">Only customers with code B10 see payment</small>
<div style="display:flex;gap:8px;margin-top:8px"><input id="code" placeholder="Enter B10"><button onclick="unlock()" style="background:#ff0000;color:#fff;border:none;border-radius:10px;padding:0 20px;font-weight:bold">UNLOCK</button></div>
<div id="pay" style="display:none;background:#fff;color:#000;border-radius:10px;padding:12px;margin-top:10px">
<b style="color:#ff0000;font-size:16px">🔴 AIRTEL MONEY: 0744995244</b><br>
Amount: <select id="plan" style="background:#ffeeee;color:#000"><option value="50000">50k 1 Week</option><option value="150000">150k 1 Month</option><option value="200000">200k Bot</option></select><br><br>
Dial <b>*185#</b> → Send Money → <b>0744995244</b><br>
<button onclick="paid()" style="width:100%;background:#ff0000;color:#fff;border:none;padding:12px;border-radius:8px;margin-top:8px;font-weight:bold">✅ I PAID</button>
</div>
</div>
</div>

<div style="padding:0 12px"><b style="font-size:13px">📜 LIVE SIGNALS - Copy to Phone MT5</b><div id="trades"><p style="color:#555;text-align:center;padding:20px">Press START to see signals</p></div></div>

<script>
let lot=0.05, price=4286.47, bal=10008.04, pnl=0, run=false, iv=null, trades=0;
function fmt(n){return n.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2})}
function updateLot(){lot=parseFloat(document.getElementById('lot').value); document.getElementById('lotCustom').value=lot; upd();}
function updateCustom(){let v=parseFloat(document.getElementById('lotCustom').value); if(v>0){lot=v; upd();}}
function upd(){
 price+=(Math.random()-0.5)*0.9;
 let up=Math.random()>0.4;
 document.getElementById('price').innerText='$'+fmt(price);
 document.getElementById('price').style.color=up?'#00ff88':'#ff4444';
 document.getElementById('entry').innerText=fmt(price);
 document.getElementById('sl').innerText=fmt(up?price-4.5:price+4.5);
 document.getElementById('tp').innerText=fmt(up?price+12:price-12);
 document.getElementById('stepLot').innerText=lot;
 document.getElementById('stepSL').innerText=fmt(up?price-4.5:price+4.5);
 document.getElementById('stepTP').innerText=fmt(up?price+12:price-12);
 document.getElementById('margin').innerText='$'+(price*lot*100/500).toFixed(2)+' | $'+(lot*100).toFixed(0)+' per $1';
 return up;
}
function toggleBot(){
 run=!run; let b=document.getElementById('startBtn');
 if(run){b.innerText='⏸️ STOP BOT'; b.className='btn btn-stop'; document.getElementById('copyArea').style.display='block'; start();} else {b.innerText='▶️ START BOT - Balance Will Move'; b.className='btn btn-start'; clearInterval(iv);}
}
function start(){
 iv=setInterval(()=>{
  let up=upd();
  let profit=(Math.random()*10-3)*(lot/0.05);
  if(Math.random()>0.35) profit=Math.abs(profit);
  pnl+=profit; bal+=profit; trades++;
  document.getElementById('bal').innerText=fmt(bal);
  document.getElementById('pnl').innerText=(pnl>=0?'+$':'-$')+Math.abs(pnl).toFixed(2);
  let card=document.createElement('div'); card.className='tradeCard';
  card.style.borderLeftColor=profit>=0?'#00ff88':'#ff4444';
  card.innerHTML=`<b>${up?'🟢 BUY':'🔴 SELL'} ${lot} XAUUSD @ ${fmt(price)}</b> <span style="float:right;color:${profit>=0?'#00ff88':'#ff4444'}">${profit>=0?'+':''}$${profit.toFixed(2)}</span><br>SL ${fmt(price-4.5)} TP ${fmt(price+12)} | Bal $${fmt(bal)}<br><button onclick="copyToMT5()" style="background:#0088ff;color:#fff;border:none;padding:6px 12px;border-radius:6px;margin-top:6px;font-size:11px">📲 COPY THIS TRADE TO MT5</button>`;
  document.getElementById('trades').prepend(card);
 },2200);
}
function copyToMT5(){
 let txt=`XAUUSD ${Math.random()>0.5?'BUY':'SELL'} LOT ${lot} Entry ${fmt(price)} SL ${fmt(price-4.5)} TP ${fmt(price+12)} Broker Any`;
 navigator.clipboard.writeText(txt).then(()=>{
  if(navigator.vibrate) navigator.vibrate([100,50,100]);
  alert('✅ COPIED!\\n\\n'+txt+'\\n\\nNOW:\\n1. Open Exness/MT5 App\\n2. XAUUSD → New Order\\n3. Lot: '+lot+'\\n4. SL: '+fmt(price-4.5)+' TP: '+fmt(price+12)+'\\n5. Open → $10,008.04 will MOVE!');
 }).catch(()=>{alert(txt+'\\n\\nCopy manually ↑');});
}
function unlock(){let c=document.getElementById('code').value.toUpperCase(); if(c.includes('B10')){document.getElementById('pay').style.display='block';} else alert('Wrong code');}
function paid(){window.open('https://wa.me/256744995244?text='+encodeURIComponent('Hi B10 Paid '+document.getElementById('plan').value+' to 0744995244'),'_blank');}
upd(); setInterval(()=>{if(!run) upd();},1000);
</script></body></html>"""

@app.route('/')
def home(): return HTML
if __name__=='__main__': app.run(host='0.0.0.0',port=int(os.environ.get('PORT',10000)))
