
import os
from flask import Flask
app = Flask(__name__)

HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
<title>MT5 TRADE - PIPNEX B10</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#000;color:#fff;font-family:Roboto,Arial;height:100vh;display:flex;flex-direction:column}
.top{display:flex;justify-content:space-between;align-items:center;padding:12px 16px;background:#000;border-bottom:1px solid #222}
.top b{font-size:18px}
.top-icons{display:flex;gap:18px;font-size:22px}
.info{padding:12px 16px;border-bottom:1px solid #1a1a1a;background:#000}
.row{display:flex;justify-content:space-between;padding:4px 0;font-size:15px}
.row span:first-child{color:#999}
.row b{font-weight:600}
.trades{flex:1;overflow:auto;padding:0 0 80px 0}
.empty{text-align:center;color:#555;margin-top:120px;font-size:14px}
.trade-card{background:#111;margin:8px 12px;border-radius:10px;padding:12px;border:1px solid #222}
.trade-head{display:flex;justify-content:space-between;font-size:13px;color:#aaa}
.symbol{color:#fff;font-weight:bold;font-size:15px}
.profit{font-weight:bold}
.buy{color:#00ff88} .sell{color:#ff4444}
.trend-badge{display:inline-block;padding:2px 8px;border-radius:12px;font-size:11px;font-weight:bold;margin-left:6px}
.trend-up{background:#00ff8822;color:#00ff88;border:1px solid #00ff8833}
.trend-down{background:#ff444422;color:#ff4444;border:1px solid #ff444433}
.sl-tp{font-size:12px;color:#888;margin-top:6px;display:flex;gap:12px}
.live-dot{width:8px;height:8px;background:#00ff88;border-radius:50%;display:inline-block;animation:blink 1s infinite}
@keyframes blink{0%,100%{opacity:1}50%{opacity:0.3}}
.controls{position:fixed;bottom:70px;left:12px;right:12px;background:#161616;border:1px solid #333;border-radius:16px;padding:12px}
.price-big{font-size:24px;font-weight:bold;text-align:center;padding:8px}
.btn{width:100%;padding:16px;border:none;border-radius:12px;font-weight:bold;font-size:16px;margin-top:8px}
.btn-start{background:#00ff88;color:#000} .btn-stop{background:#ff3344;color:#fff}
.bottom-nav{position:fixed;bottom:0;left:0;right:0;background:#0e0e0e;border-top:1px solid #222;display:flex;justify-content:space-around;padding:8px 0 12px 0}
.nav-item{text-align:center;color:#666;font-size:11px;flex:1}
.nav-item.active{color:#fff}
.nav-icon{font-size:20px;display:block;margin-bottom:2px}
.badge{background:#ff3344;color:#fff;border-radius:50%;padding:1px 5px;font-size:10px;position:relative;top:-8px}
</style></head>
<body>

<div class="top"><b>Trade</b><div class="top-icons"><span>↕️</span><span>➕</span></div></div>

<div class="info">
<div class="row"><span>Balance:</span><b>10 008.04</b></div>
<div class="row"><span>Equity:</span><b id="equity">10 008.04</b></div>
<div class="row"><span>Free margin:</span><b id="free">10 008.04</b></div>
<div class="row" style="margin-top:6px"><span><span class="live-dot"></span> XAUUSD:</span><b id="livePrice" style="color:#00ff88">$2688.50</b> <span id="trendLive" class="trend-badge trend-up">TRENDING UP 91%</span></div>
</div>

<div class="trades" id="trades">
<div class="empty" id="emptyMsg">No positions — Click START below<br>Bot will show TRENDING trades here</div>
</div>

<div class="controls">
<div class="price-big" id="signalText">WAITING FOR TREND...</div>
<button id="mainBtn" class="btn btn-start" onclick="toggle()">▶️ START B10 BOT - SHOW TRENDS HERE</button>
<div style="text-align:center;color:#666;font-size:11px;margin-top:6px">DEMO 106285257 | Same screen as your MT5 Trade tab</div>
</div>

<div class="bottom-nav">
<div class="nav-item"><span class="nav-icon">↕️</span>Quotes</div>
<div class="nav-item"><span class="nav-icon">⛾</span>Charts</div>
<div class="nav-item active"><span class="nav-icon">📈</span>10008.04</div>
<div class="nav-item"><span class="nav-icon">🕒</span>History</div>
<div class="nav-item"><span class="nav-icon">💬<span class="badge">2</span></span>Messages</div>
</div>

<script>
let running=false, iv=null, price=2688.5, balance=10008.04, count=0;

function fmt(n){return n.toFixed(2)}

function updatePrice(){
 price += (Math.random()-0.5)*0.9;
 let up = Math.random()>0.38;
 let rsi = up? 60+Math.random()*15 : 40-Math.random()*15;
 let trending = up? (rsi>58?"TRENDING UP 91%":"UP 64%") : (rsi<42?"TRENDING DOWN 89%":"DOWN 61%");
 document.getElementById('livePrice').innerText='$'+fmt(price);
 document.getElementById('livePrice').style.color=up?'#00ff88':'#ff4444';
 let badge=document.getElementById('trendLive');
 badge.innerText=trending;
 badge.className='trend-badge '+(up?'trend-up':'trend-down');
 document.getElementById('signalText').innerHTML=(up?'🟢 <span style="color:#00ff88">BUY TREND '+fmt(price)+'</span>':'🔴 <span style="color:#ff4444">SELL TREND '+fmt(price)+'</span>')+' <span style="font-size:12px;color:#888">RSI '+fmt(rsi)+'</span>';
 return {price:price, up:up, trending:trending, rsi:rsi};
}

function toggle(){
 running=!running;
 let btn=document.getElementById('mainBtn');
 if(running){
  btn.innerText='⏸️ STOP BOT - TRENDS LIVE'; btn.className='btn btn-stop';
  document.getElementById('emptyMsg').style.display='none';
  startTrends();
 }else{
  btn.innerText='▶️ START B10 BOT - SHOW TRENDS HERE'; btn.className='btn btn-start';
  stopTrends();
 }
}

function startTrends(){
 let pIv=setInterval(updatePrice,1200);
 iv=setInterval(()=>{
  let d=updatePrice();
  let isStrong = d.trending.includes('91%') || d.trending.includes('89%');
  if(isStrong || Math.random()>0.4){
   count++;
   let isBuy=d.up;
   let entry=d.price;
   let sl=isBuy?entry-4.5:entry+4.5;
   let tp=isBuy?entry+12:entry-12;
   let prof=(Math.random()*12-3);
   balance+=prof;
   let card=document.createElement('div');
   card.className='trade-card';
   card.innerHTML=`
   <div class="trade-head"><span class="symbol">XAUUSD, ${isBuy?'buy':'sell'} ${isBuy?'0.05':'0.05'}</span><span class="profit ${prof>=0?'buy':'sell'}">${prof>=0?'+':''}${fmt(prof)}</span></div>
   <div style="font-size:13px;margin-top:4px">${fmt(entry)} → ${fmt(isBuy?entry+0.6:entry-0.6)} <span class="trend-badge ${isBuy?'trend-up':'trend-down'}">${d.trending}</span></div>
   <div class="sl-tp"><span>S/L: ${fmt(sl)}</span><span>T/P: ${fmt(tp)}</span><span style="color:#00ff88">● TRENDING NOW</span></div>
   <div style="font-size:11px;color:#555;margin-top:4px">#${106285200+count} | 106285257 DEMO | ${new Date().toLocaleTimeString()}</div>`;
   document.getElementById('trades').prepend(card);
   document.getElementById('equity').innerText=fmt(balance);
   document.getElementById('free').innerText=fmt(balance);
   if('vibrate' in navigator) navigator.vibrate(100);
   if(count>20){document.getElementById('trades').lastChild.remove()}
  }
 },3000);
 window._pIv=pIv;
}

function stopTrends(){clearInterval(iv);clearInterval(window._pIv);}
updatePrice();
setInterval(()=>{if(!running) updatePrice();},1500);
</script>
</body></html>"""

@app.route('/')
def home(): return HTML
if __name__=='__main__': app.run(host='0.0.0.0',port=int(os.environ.get('PORT',10000)))
