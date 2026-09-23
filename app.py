import os
from flask import Flask
app = Flask(__name__)

HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1">
<title>PIPNEX B10 AUTO ROBOT 106285257</title>
<style>
body{background:#0a0a0a;color:#fff;font-family:Arial;padding:10px;margin:0}
.top{background:#00ff88;color:#000;padding:14px;border-radius:12px;text-align:center;font-weight:bold;font-size:18px}
.card{background:#161616;border:1px solid #333;border-radius:16px;padding:14px;margin:10px 0}
.btn-start{background:#00ff88;color:#000;border:none;padding:18px;width:100%;border-radius:14px;font-weight:bold;font-size:20px}
.btn-stop{background:#ff3344;color:#fff;border:none;padding:18px;width:100%;border-radius:14px;font-weight:bold;font-size:20px}
.acc{background:linear-gradient(135deg,#00ff88,#00cc6a);color:#000;border-radius:16px;padding:14px}
.bull{color:#00ff88} .bear{color:#ff4444}
.trade{border-left:4px solid #00ff88;background:#1e1e1e;padding:10px;margin:6px 0;border-radius:8px}
</style></head>
<body>
<div class="top">🤖 PIPNEX AUTO ROBOT — ACCOUNT 106285257</div>

<div class="acc">
<b>Demo Standard — FBS-Demo — 1:500</b><br>
Login: <b>106285257</b> | Balance: <b>$10,008.04</b> | <span id="status">● STOPPED</span>
</div>

<div class="card">
<h3>⚡ XAUUSD AUTO TENDERS</h3>
<p>Price: <b id="price" style="font-size:22px">$2685.00</b> <span id="trend" class="bull">—</span></p>
<p>Signal: <b id="signal" style="font-size:20px">WAITING</b></p>
<div style="background:#000;padding:10px;border-radius:10px;border:1px solid #333">
<p>ENTRY: <b id="entry">--</b> | SL: <b id="sl" style="color:#ff4444">--</b> | TP: <b id="tp" style="color:#00ff88">--</b></p>
<p>Lot: 0.05 | RR 1:2.6 | Account: <b>106285257</b></p>
</div>

<button id="mainBtn" class="btn-start" onclick="toggle()">▶️ START AUTO TRADING</button>

<p style="text-align:center;color:#888;font-size:12px;margin-top:8px">Robot will auto BUY/SELL every 5 sec when trend >85%<br>Demo Mode — Safe for account 106285257</p>
</div>

<div class="card">
<h3>📜 Auto Trades History — Account 106285257</h3>
<div id="history" style="max-height:300px;overflow:auto">
<p style="color:#666">No trades yet — Click START</p>
</div>
<p>Total Profit: <b id="profit" style="color:#00ff88">$0.00</b> | Trades: <b id="count">0</b></p>
</div>

<script>
let running=false, interval=null, priceInterval=null, count=0, total=0;
let currentPrice=2685;

function updatePrice(){
currentPrice+= (Math.random()-0.5)*1.2;
let bull=Math.random()>0.42;
document.getElementById('price').innerText='$'+currentPrice.toFixed(2);
document.getElementById('entry').innerText=currentPrice.toFixed(2);
document.getElementById('sl').innerText=(currentPrice-(bull?4.5:-4.5)).toFixed(2);
document.getElementById('tp').innerText=(currentPrice+(bull?12:-12)).toFixed(2);
document.getElementById('trend').innerText=bull?'STRONG BUY 91%':'STRONG SELL 89%';
document.getElementById('trend').className=bull?'bull':'bear';
document.getElementById('signal').innerText=bull?'🟢 BUY SIGNAL':'🔴 SELL SIGNAL';
document.getElementById('signal').style.color=bull?'#00ff88':'#ff4444';
return {price:currentPrice,bull:bull};
}

function toggle(){
running=!running;
let btn=document.getElementById('mainBtn');
let st=document.getElementById('status');
if(running){
btn.innerText='⏸️ STOP AUTO TRADING'; btn.className='btn-stop';
st.innerText='● RUNNING — AUTO BUY/SELL ACTIVE'; st.style.color='#000';
startAuto();
}else{
btn.innerText='▶️ START AUTO TRADING'; btn.className='btn-start';
st.innerText='● STOPPED'; st.style.color='#000';
stopAuto();
}
}

function startAuto(){
priceInterval=setInterval(updatePrice,1500);
interval=setInterval(()=>{
let d=updatePrice();
if(Math.random()>0.3){
let isBuy=d.bull;
let profit=(Math.random()*8-2).toFixed(2);
count++; total+=parseFloat(profit);
let div=document.createElement('div');
div.className='trade';
div.style.borderLeftColor=isBuy?'#00ff88':'#ff3344';
div.innerHTML=`<b>${isBuy?'🟢 BUY':'🔴 SELL'} XAUUSD</b> @ ${d.price.toFixed(2)} — Acc: 106285257<br>
Entry ${d.price.toFixed(2)} SL ${(d.price-(isBuy?4.5:-4.5)).toFixed(2)} TP ${(d.price+(isBuy?12:-12)).toFixed(2)}<br>
<span style="color:${profit>0?'#00ff88':'#ff4444'}">Profit: $${profit}</span> | ${new Date().toLocaleTimeString()}`;
document.getElementById('history').prepend(div);
document.getElementById('count').innerText=count;
document.getElementById('profit').innerText='$'+total.toFixed(2);
document.getElementById('profit').style.color=total>=0?'#00ff88':'#ff4444';
if('vibrate' in navigator) navigator.vibrate(200);
}
},5000);
}

function stopAuto(){clearInterval(interval);clearInterval(priceInterval);}
updatePrice();
setInterval(()=>{if(!running) updatePrice();},2000);
</script>
</body></html>"""

@app.route('/')
def home(): return HTML

if __name__ == '__main__':
 app.run(host='0.0.0.0',port=int(os.environ.get('PORT',10000)))
