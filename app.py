import os
from flask import Flask
app = Flask(__name__)

HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1">
<title>PIPNEX ONE BUTTON</title>
<style>
body{margin:0;background:#000;color:#fff;font-family:Arial;text-align:center}
.box{background:#111;margin:10px;border-radius:20px;padding:16px;border:1px solid #222}
.price{font-size:38px;font-weight:bold;color:#00ff88}
.trend{display:inline-block;padding:8px 18px;border-radius:20px;font-weight:bold;margin:8px 0}
.btn{width:100%;padding:22px;border:none;border-radius:16px;font-weight:bold;font-size:22px;margin-top:14px}
.btn-copy{background:linear-gradient(135deg,#00ff88,#0088ff);color:#000}
.btn-start{background:#222;color:#fff;border:1px solid #444;font-size:16px}
select{width:100%;padding:14px;background:#222;color:#fff;border:1px solid #444;border-radius:12px;font-size:16px;margin-top:8px}
</style></head><body>

<div style="background:#00ff88;color:#000;padding:12px;font-weight:bold">PIPNEX - ONE BUTTON MT5 - PHONE ONLY</div>

<div class="box">
<b>XAUUSD GOLD</b><br>
<div class="price" id="price">$4,286.47</div>
<div id="trend" class="trend" style="background:#00ff88;color:#000">🚀 UP 91% - BUY NOW</div><br>
<small>Bal $<span id="bal">10,008.04</span> | Lot <span id="lotTxt">0.01</span></small>

<select id="lot" onchange="lot=parseFloat(this.value);document.getElementById('lotTxt').innerText=lot"><option value="0.01" selected>LOT 0.01 Safe $1</option><option value="0.05">LOT 0.05 Best $5</option><option value="0.10">LOT 0.10 Pro $10</option><option value="0.20">LOT 0.20 $20</option><option value="1.00">LOT 1.00 $100 MAX</option></select>
<select id="broker"><option>Exness</option><option>FBS</option><option>HFM</option><option>XM</option><option>OctaFX</option><option>Deriv</option></select>

<div style="margin-top:10px;font-size:14px">ENTRY <b id="entry">4286.47</b> | SL <b id="sl" style="color:#ff4444">4281.97</b> | TP <b id="tp" style="color:#00ff88">4298.47</b></div>

<button class="btn btn-copy" onclick="copy()">📲 COPY LAST TREND TO MT5 APP</button>
<button id="autoBtn" class="btn btn-start" onclick="toggle()">▶️ START AUTO TRENDING</button>

<div style="margin-top:12px;background:#0a0a0a;border-radius:10px;padding:10px;font-size:12px;text-align:left">
<b style="color:#00ff88">HOW IT WORKS (Phone only):</b><br>
1. Press START AUTO TRENDING<br>
2. Bot beeps when UP/DOWN 90%+<br>
3. Press 📲 COPY button<br>
4. Open Exness/M

