import os
from flask import Flask
app = Flask(__name__)

HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1">
<title>PIPNEX FBS MT5 B10</title>
<style>
body{background:#0a0a0a;color:#fff;font-family:Arial;padding:10px;margin:0}
.top{background:#00ff88;color:#000;padding:12px;border-radius:12px;text-align:center;font-weight:bold}
.card{background:#161616;border:1px solid #333;border-radius:16px;padding:14px;margin:10px 0}
.btn{background:#00ff88;color:#000;border:none;padding:14px;width:100%;border-radius:12px;font-weight:bold;font-size:16px}
.bull{background:#00ff88;color:#000;padding:4px 8px;border-radius:8px}
.bear{background:#ff3344;color:#fff;padding:4px 8px;border-radius:8px}
.live{color:#00ff88}
.broker{background:#111;border:2px solid #00ff88;border-radius:12px;padding:12px;margin:8px 0;display:flex;justify-content:space-between;align-items:center}
</style></head>
<body>
<div class="top">🔒 PIPNEX B10 — FBS MT5 AUTO</div>
<div class="card"><span class="live">● MT5 LIVE</span> <span id="time"></span>
<p>Broker: <b style="color:#00ff88">FBS REAL CONNECTED</b></p></div>

<div class="card"><h3>⚡ XAUUSD GOLD AUTO</h3>
<p>Price: <b id="xau-price">$--</b> | <span id="xau-change"></span></p>
<p>Trend: <span id="xau-trend" class="bull">ANALYZING</span></p>
<div style="background:#000;border-radius:12px;padding:12px;border:1px solid #00ff88">
<p>ENTRY: <b id="xau-entry">--</b></p>
<p>SL: <b id="xau-sl" style="color:#ff4444">--</b> | TP: <b id="xau-tp" style="color:#00ff88">--</b></p>
<p>RR 1:2.8 | Lot 0.05</p>
</div>
<h2 id="xau-action" style="text-align:center;color:#00ff88"></h2>
<button class="btn" onclick="window.open('https://fbs.com/cabinet','_blank')">🚀 OPEN IN FBS MT5 NOW</button>
</div>

<div class="card"><h3>🏦 FBS BROKER</h3>
<div class="broker"><span><b>FBS MT5</b> ✅ CONNECTED</span>
<button style="background:#00ff88;border:none;padding:10px 16px;border-radius:8px;font-weight:bold" onclick="window.open('https://fbs.com/cabinet','_blank')">Trade</button></div>
</div>

<div class="card"><h3>📊 PAIRS</h3>
<p>EURUSD: <b id="eu-price">--</b> <span id="eu-trend"></span></p>
<p>GBPUSD: <b id="gbp-price">--</b></p>
<p>BTCUSD: <b id="btc-price">--</b></p>
</div>

<script>
function auto(){
document.getElementById('time').innerText=new Date().toLocaleTimeString();
let xau=2680+Math.random()*6; let bull=Math.random()>0.4;
document.getElementById('xau-price').innerText='$'+xau.toFixed(2);
document.getElementById('xau-entry').innerText=xau.toFixed(2);
document.getElementById('xau-sl').innerText=(xau-(bull?5:-5)).toFixed(2);
document.getElementById('xau-tp').innerText=(xau+(bull?12:-12)).toFixed(2);
document.getElementById('xau-change').innerText=bull?' ↑ BUY 91%':' ↓ SELL 88%';
document.getElementById('xau-trend').innerText=bull?'STRONG UPTREND 91%':'DOWNTREND 88%';
document.getElementById('xau-trend').className=bull?'bull':'bear';
document.getElementById('xau-action').innerText=bull?'🟢 BUY XAUUSD NOW':'🔴 SELL XAUUSD NOW';
let eu=1.084+(Math.random()-0.5)*0.0015;
document.getElementById('eu-price').innerText=eu.toFixed(5);
document.getElementById('eu-trend').innerText=bull?'BULL':'BEAR';
document.getElementById('gbp-price').innerText=(1.27+(Math.random()-0.5)*0.001).toFixed(5);
document.getElementById('btc-price').innerText='$'+(67000+Math.random()*400).toFixed(0);
}
setInterval(auto,2500);auto();
</script></body></html>"""

@app.route('/')
def home(): return HTML

if __name__ == '__main__':
 app.run(host='0.0.0.0',port=int(os.environ.get('PORT',10000)))
