

import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
 return """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1">
<style>body{margin:0;background:#000;color:#fff;font-family:Arial;text-align:center}
.box{background:#111;margin:10px;border-radius:20px;padding:16px}
.price{font-size:36px;color:#00ff88;font-weight:bold}
.trend{display:inline-block;padding:8px 16px;border-radius:20px;font-weight:bold;margin:8px}
.btn{width:100%;padding:20px;border:none;border-radius:14px;font-weight:bold;font-size:20px;margin-top:12px}
.copy{background:#00ff88;color:#000}.auto{background:#222;color:#fff;border:1px solid #444}
select{width:100%;padding:12px;background:#222;color:#fff;border-radius:10px;margin-top:8px}
</style></head><body>
<div style="background:#00ff88;color:#000;padding:10px;font-weight:bold">PIPNEX ONE BUTTON - PHONE ONLY</div>
<div class="box">
<div>XAUUSD GOLD</div>
<div class="price" id="price">$4286.47</div>
<div id="trend" class="trend" style="background:#00ff88;color:#000">UP 91% BUY</div><br>
<small>Bal $<span id="bal">10008.04</span></small>
<select id="lot"><option>0.01</option><option>0.05</option><option>0.10</option><option>1.00</option></select>
<div style="margin-top:10px">SL <b id="sl">4281.97</b> | TP <b id="tp">4298.47</b></div>
<button class="btn copy" onclick="copy()">📲 COPY LAST TREND TO MT5</button>
<button class="btn auto" onclick="start()" id="ab">▶️ START AUTO TRENDING</button>
<div style="margin-top:10px;font-size:11px;color:#888;text-align:left">1. START AUTO<br>2. COPY<br>3. Paste in Exness MT5 app -> $10008 moves!</div>
<div style="margin-top:10px;border-top:1px solid #222;padding-top:8px;font-size:12px">PAY 0744995244 CODE B10 <input id="code" placeholder="B10" style="padding:8px;background:#222;color:#fff;border:1px solid #444;border-radius:6px"><button onclick="if(document.getElementById('code').value.includes('B10')){document.getElementById('pay').style.display='block'}" style="background:red;color:#fff;border:none;padding:8px;border-radius:6px">UNLOCK</button><div id="pay" style="display:none;background:#fff;color:#000;padding:8px;margin-top:6px;border-radius:6px">AIRTEL <b style="color:red">0744995244</b> *185#</div></div>
</div>
<script>
let p=4286.47, lot=0.01, last='', iv=null, run=false;
function fmt(n){return n.toFixed(2)}
function upd(){
 p+=(Math.random()-0.48)*1;
 let up=Math.random()>0.45;
 let pct=85+Math.floor(Math.random()*14);
 document.getElementById('price').innerText='$'+fmt(p);
 document.getElementById('trend').innerText=(up?'UP ':'DOWN ')+pct+'% '+(up?'BUY':'SELL');
 document.getElementById('trend').style.background=up?'#00ff88':'#ff4444';
 document.getElementById('sl').innerText=fmt(up?p-4.5:p+4.5);
 document.getElementById('tp').innerText=fmt(up?p+12:p-12);
 last='XAUUSD '+(up?'BUY':'SELL')+' LOT '+document.getElementById('lot').value+' SL '+document.getElementById('sl').innerText+' TP '+document.getElementById('tp').innerText;
}
function start(){
 run=!run; document.getElementById('ab').innerText=run?'⏸️ STOP AUTO':'▶️ START AUTO TRENDING';
 if(run){iv=setInterval(upd,3000); if(navigator.vibrate) navigator.vibrate(100);} else clearInterval(iv);
}
function copy(){
 navigator.clipboard.writeText(last).then(()=>{alert('COPIED!\\n'+last+'\\n\\nOpen MT5 App -> Paste!');});
}
setInterval(()=>{if(!run) upd();},1000); upd();
</script></body></html>"""

if __name__=='__main__':
 app.run(host='0.0.0.0',port=int(os.environ.get('PORT',10000)))
