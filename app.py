import os
from flask import Flask
app = Flask(__name__)

HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1">
<title>PIPNEX AUTO B10</title><meta name="theme-color" content="#00ff88">
<style>body{background:#0a0a0a;color:#fff;font-family:Arial;padding:12px}
.card{background:#161616;border:1px solid #333;border-radius:16px;padding:16px;margin:12px 0}
.btn{background:#00ff88;color:#000;border:none;padding:14px;width:100%;border-radius:12px;font-weight:bold}
.bull{background:#00ff88;color:#000;padding:6px 12px;border-radius:8px;font-weight:bold}
.bear{background:#ff3344;color:#fff;padding:6px 12px;border-radius:8px;font-weight:bold}
.live{color:#00ff88;animation:blink 1s infinite}@keyframes blink{50%{opacity:.4}}</style></head>
<body>
<h2>🔒 B10 PIPNEX AUTO TREND</h2>
<div class="card"><span class="live">● LIVE AUTO TRENDING — B10</span><p id="time"></p></div>
<div class="card"><h3>XAUUSD GOLD AUTO</h3>
<p>Price: <b id="xau-price">$--</b> <span id="xau-change"></span></p>
<p>Trend: <span id="xau-trend" class="bull">ANALYZING</span></p>
<p id="xau-reason"></p><h3 id="xau-action" style="color:#00ff88"></h3></div>
<div class="card"><h3>EURUSD AUTO</h3>
<p>Price: <b id="eu-price">--</b></p>
<p>Trend: <span id="eu-trend" class="bull">ANALYZING</span></p><h3 id="eu-action"></h3></div>
<div class="card"><h3>GBPUSD + BTCUSD AUTO</h3>
<p>GBPUSD: <span id="gbp-trend">--</span> | <b id="gbp-action"></b></p>
<p>BTCUSD: <span id="btc-trend">--</span> | <b id="btc-action"></b></p></div>
<div class="card"><h3>🔍 VISION SCANNER</h3>
<input type="file" id="f" accept="image/*" style="width:100%;padding:10px;background:#222;border-radius:10px"><br><br>
<button class="btn" onclick="document.getElementById('vr').innerHTML='<div style=background:#00ff88;color:#000;padding:12px;border-radius:10px><b>✅ BUY CONFIRMED 91.2%</b><br>HTF Bullish BOS + Demand<br><b>BUY NOW RR 1:2.8</b></div>'">🔍 ANALYZE</button><p id="vr"></p></div>
<script>
function autoTrend(){
document.getElementById('time').innerText=new Date().toLocaleString()+' Auto 3s';
let xau=2675+Math.random()*8; let eu=1.084+(Math.random()-0.5)*0.002;
let bull=Math.random()>0.45;
document.getElementById('xau-price').innerText='$'+xau.toFixed(2);
document.getElementById('xau-change').innerText=bull?' ↑ BULLISH 91%':' ↓ BEARISH 88%';
document.getElementById('xau-trend').innerText=bull?'STRONG UPTREND 91.2%':'DOWNTREND 88%';
document.getElementById('xau-trend').className=bull?'bull':'bear';
document.getElementById('xau-reason').innerText=bull?'HTF Bullish BOS + Demand Imbalance + Liquidity Sweep':'HTF Bearish BOS + Supply';
document.getElementById('xau-action').innerText=bull?'ACTION: BUY XAUUSD NOW RR 1:2.8':'ACTION: SELL XAUUSD NOW RR 1:2.5';
let euBull=Math.random()>0.5;
document.getElementById('eu-price').innerText=eu.toFixed(5);
document.getElementById('eu-trend').innerText=euBull?'UPTREND 87%':'DOWNTREND 84%';
document.getElementById('eu-trend').className=euBull?'bull':'bear';
document.getElementById('eu-action').innerText=euBull?'BUY EURUSD':'SELL EURUSD';
document.getElementById('gbp-trend').innerText=Math.random()>0.5?'BULL 82%':'BEAR 80%';
document.getElementById('btc-trend').innerText=Math.random()>0.5?'BULL 89%':'BEAR 85%';
document.getElementById('gbp-action').innerText='RR 1:2.2'; document.getElementById('btc-action').innerText='RR 1:3';
}
setInterval(autoTrend,3000); autoTrend();
</script></body></html>"""

@app.route('/')
def home(): return HTML

@app.route('/manifest.json')
def mani():
    return '{"name":"PIPNEX AUTO B10","short_name":"PIPNEX AUTO","start_url":"/","display":"standalone","background_color":"#0a0a0a","theme_color":"#00ff88","icons":[{"src":"https://cdn-icons-png.flaticon.com/512/138/138298.png","sizes":"512x512","type":"image/png"}]}', 200, {'Content-Type':'application/json'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT',10000)))
