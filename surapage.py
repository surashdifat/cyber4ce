import streamlit as st
import streamlit.components.v1 as components


def render_service():
    st.markdown("""
    <style>
        .block-container {padding: 0 !important; max-width: 100% !important;}
        .main .block-container {padding-top: 0 !important; padding-left: 0 !important; padding-right: 0 !important;}
        [data-testid="stAppViewContainer"] {padding: 0 !important;}
        [data-testid="stAppViewContainer"] > .main {padding-top: 0 !important;}
        .main > div:first-child {padding-top: 0 !important;}
        header[data-testid="stHeader"] {height: 0 !important; min-height: 0 !important;}
        iframe {width: 100% !important; border: none !important; display: block !important; margin: 0 !important; padding: 0 !important;}
        [data-testid="stVerticalBlock"] {gap: 0 !important;}
        [data-testid="stVerticalBlock"] > div:first-child {margin-top: 0 !important; padding-top: 0 !important;}
    </style>
    """, unsafe_allow_html=True)

    html_code = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Phishing Link Scanner</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&family=JetBrains+Mono:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
:root{--bg-main:#0B1120;--bg-panel:#1E293B;--bg-input:#0F172A;--cyan-main:#06B6D4;--cyan-light:#22D3EE;--cyan-dim:#0E7490;--text-main:#E2E8F0;--text-dim:#94A3B8;--text-darker:#64748B;--danger:#EF4444;--warning:#F59E0B;--success:#10B981;--border:#334155;--border-bright:#475569;--font-display:'Orbitron',Arial,sans-serif;--font-mono:'JetBrains Mono',Courier New,monospace}
*{margin:0;padding:0;box-sizing:border-box}
body{background:var(--bg-main);color:var(--text-main);font-family:var(--font-mono);padding:15px 20px;overflow-x:hidden;position:relative}
.cyber-bg{position:fixed;top:0;left:0;width:100%;height:100%;z-index:-1;overflow:hidden}
.bg-grid{position:absolute;inset:0;background-image:linear-gradient(rgba(6,182,212,0.04) 1px,transparent 1px),linear-gradient(90deg,rgba(6,182,212,0.04) 1px,transparent 1px);background-size:60px 60px;-webkit-mask-image:radial-gradient(ellipse at center,black 20%,transparent 80%);mask-image:radial-gradient(ellipse at center,black 20%,transparent 80%)}
.bg-glow{position:absolute;border-radius:50%;filter:blur(140px);opacity:.4}
.bg-glow-1{width:500px;height:500px;background:var(--cyan-main);top:-150px;right:-150px;animation:floatGlow 16s ease-in-out infinite}
.bg-glow-2{width:450px;height:450px;background:#0E7490;bottom:-200px;left:-150px;animation:floatGlow 20s ease-in-out infinite reverse}
@keyframes floatGlow{0%,100%{transform:translate(0,0) scale(1)}50%{transform:translate(50px,-50px) scale(1.1)}}
.container{width:100%;max-width:680px;display:flex;flex-direction:column;gap:18px;animation:fadeIn .8s ease;position:relative;z-index:1;margin:0 auto}
.hero-section{display:flex;flex-direction:column;align-items:center;gap:8px;position:relative;padding:5px 0}
.hero-rings{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:180px;height:180px;pointer-events:none}
.ring{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);border:1px solid var(--cyan-main);border-radius:50%;opacity:.4}
.ring-1{width:90px;height:90px;opacity:.5;animation:ringPulse 3s ease-in-out infinite}
.ring-2{width:130px;height:130px;opacity:.25;animation:ringPulse 3s ease-in-out infinite .5s;border-style:dashed}
.ring-3{width:180px;height:180px;opacity:.15;animation:ringPulse 3s ease-in-out infinite 1s}
@keyframes ringPulse{0%,100%{transform:translate(-50%,-50%) scale(1);opacity:.5}50%{transform:translate(-50%,-50%) scale(1.05);opacity:.2}}
.hero-shield{width:55px;height:55px;color:var(--cyan-main);filter:drop-shadow(0 0 15px rgba(6,182,212,.6)) drop-shadow(0 0 30px rgba(6,182,212,.15));animation:shieldFloat 4s ease-in-out infinite;position:relative;z-index:2}
.hero-shield svg{width:100%;height:100%}
@keyframes shieldFloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}
.hero-orbit{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:180px;height:180px;pointer-events:none}
.orbit-item{position:absolute;width:26px;height:26px;color:var(--cyan-light);background:var(--bg-panel);border:1px solid var(--border-bright);border-radius:50%;padding:6px;box-shadow:0 0 15px rgba(6,182,212,.15),inset 0 0 10px rgba(6,182,212,.15);animation:orbitFloat 5s ease-in-out infinite}
.orbit-item svg{width:100%;height:100%}
.orbit-1{top:-10px;left:50%;transform:translateX(-50%)}
.orbit-2{right:-10px;top:50%;transform:translateY(-50%);animation-delay:1.2s}
.orbit-3{bottom:-10px;left:50%;transform:translateX(-50%);animation-delay:2.4s}
.orbit-4{left:-10px;top:50%;transform:translateY(-50%);animation-delay:3.6s}
@keyframes orbitFloat{0%,100%{opacity:.7}50%{opacity:1;box-shadow:0 0 25px rgba(6,182,212,.6)}}
.hero-title{font-family:var(--font-display);font-size:1.2rem;font-weight:700;letter-spacing:3px;color:var(--text-main);text-align:center;margin-top:5px;text-shadow:0 0 20px rgba(6,182,212,.6),0 0 40px rgba(6,182,212,.15);position:relative;z-index:2}
.hero-subtitle{font-family:var(--font-mono);font-size:.75rem;letter-spacing:3px;color:var(--cyan-light);text-transform:uppercase;opacity:.8;position:relative;z-index:2}
.panel-header{display:flex;align-items:center;gap:12px;margin-bottom:20px;padding-bottom:15px;border-bottom:1px solid var(--border)}
.panel-dot{width:8px;height:8px;background:var(--cyan-main);border-radius:50%;box-shadow:0 0 10px rgba(6,182,212,.6);animation:dotPulse 2s ease-in-out infinite}
@keyframes dotPulse{0%,100%{opacity:1}50%{opacity:.4}}
.panel-title{font-family:var(--font-mono);font-size:.9rem;letter-spacing:4px;color:var(--cyan-light);font-weight:700;text-transform:uppercase}
.input-panel{background:linear-gradient(135deg,rgba(30,41,59,.95),rgba(11,17,32,.95));padding:26px;border-radius:12px;border:1px solid var(--border);width:100%;box-shadow:0 0 40px rgba(6,182,212,.08),inset 0 1px 0 rgba(6,182,212,.1)}
.input-wrapper{display:flex;gap:12px;flex-wrap:wrap}
#urlInput{flex:1;min-width:250px;background:var(--bg-input);border:1px solid var(--border-bright);border-radius:8px;padding:15px 18px;color:var(--text-main);font-family:var(--font-mono);font-size:.9rem;transition:all .3s ease}
#urlInput:focus{outline:none;border-color:var(--cyan-main);box-shadow:0 0 0 3px rgba(6,182,212,.15),0 0 25px rgba(6,182,212,.15)}
#urlInput::placeholder{color:var(--text-darker)}
#scanBtn{background:linear-gradient(135deg,var(--cyan-main),var(--cyan-light));color:#0B1120;border:none;padding:15px 36px;border-radius:8px;font-family:var(--font-display);font-size:.85rem;font-weight:700;letter-spacing:3px;cursor:pointer;transition:all .3s ease;box-shadow:0 0 25px rgba(6,182,212,.15)}
#scanBtn:hover{transform:translateY(-2px);box-shadow:0 0 30px rgba(6,182,212,.6),0 0 60px rgba(6,182,212,.15)}
#scanBtn:disabled{opacity:.5;cursor:not-allowed}
.terminal-panel{background:#000;border:1px solid var(--cyan-dim);border-radius:12px;width:100%;overflow:hidden;box-shadow:0 0 40px rgba(6,182,212,.2);animation:fadeIn .4s ease}
.terminal-header{display:flex;align-items:center;gap:12px;background:#0a0a0a;padding:12px 16px;border-bottom:1px solid #1a1a1a}
.terminal-dots{display:flex;gap:6px}
.dot{width:10px;height:10px;border-radius:50%}
.dot-red{background:#EF4444}.dot-yellow{background:#F59E0B}.dot-green{background:#10B981}
.terminal-title{flex:1;font-size:.75rem;color:#666;font-family:var(--font-mono);letter-spacing:1px}
.skip-btn{background:transparent;border:1px solid var(--cyan-dim);color:var(--cyan-light);font-family:var(--font-display);font-size:.65rem;letter-spacing:2px;padding:5px 12px;border-radius:4px;cursor:pointer;transition:all .2s ease}
.skip-btn:hover{border-color:var(--cyan-main);color:var(--cyan-main);box-shadow:0 0 15px rgba(6,182,212,.15)}
.terminal-body{padding:20px;font-family:var(--font-mono);font-size:.82rem;line-height:1.8;color:#10B981;min-height:240px;max-height:320px;overflow-y:auto}
.term-line{display:block;white-space:pre-wrap;word-break:break-all}
.term-cmd{color:#06B6D4}.term-ok{color:#10B981}.term-warn{color:#F59E0B}.term-err{color:#EF4444}.term-info{color:#94A3B8}
.term-cursor{display:inline-block;width:8px;height:14px;background:#10B981;animation:cursorBlink 1s step-end infinite;vertical-align:middle;margin-left:2px}
@keyframes cursorBlink{0%,100%{opacity:1}50%{opacity:0}}
.result-panel{background:linear-gradient(135deg,rgba(30,41,59,.95),rgba(11,17,32,.95));padding:26px;border-radius:12px;border:1px solid var(--border);width:100%;display:flex;flex-direction:column;gap:22px;animation:fadeIn .5s ease}
.scanned-url{display:flex;flex-direction:column;gap:6px;background:rgba(6,182,212,.04);border-left:3px solid var(--cyan-main);padding:12px 16px;border-radius:4px}
.scanned-label{font-size:.65rem;letter-spacing:2px;color:var(--text-darker);text-transform:uppercase;font-weight:600}
.scanned-value{font-family:var(--font-mono);font-size:.85rem;color:var(--cyan-light);word-break:break-all;direction:ltr;text-align:left}
.alert-banner{display:flex;align-items:center;gap:14px;padding:16px 20px;border-radius:8px;font-family:var(--font-mono);font-size:.95rem;font-weight:700;letter-spacing:2px;text-transform:uppercase;animation:alertPulse 2.5s ease-in-out infinite}
.alert-banner.safe{background:rgba(16,185,129,.08);border:2px solid #10B981;color:#10B981;box-shadow:0 0 30px rgba(16,185,129,.25)}
.alert-banner.warning{background:rgba(245,158,11,.08);border:2px solid #F59E0B;color:#F59E0B;box-shadow:0 0 30px rgba(245,158,11,.25)}
.alert-banner.danger{background:rgba(239,68,68,.08);border:2px solid #EF4444;color:#EF4444;box-shadow:0 0 30px rgba(239,68,68,.3)}
.alert-icon{font-size:1.6rem}.alert-text{flex:1}
@keyframes alertPulse{0%,100%{transform:scale(1)}50%{transform:scale(1.008)}}
.risk-section{display:flex;justify-content:center;padding:10px 0}
.risk-gauge{position:relative;width:180px;height:180px}
.gauge-svg{width:100%;height:100%;transform:rotate(-90deg)}
.gauge-bg{fill:none;stroke:var(--border);stroke-width:8}
.gauge-fill{fill:none;stroke:#10B981;stroke-width:8;stroke-linecap:round;stroke-dasharray:534;stroke-dashoffset:534;transition:stroke-dashoffset 1.2s cubic-bezier(.4,0,.2,1),stroke 1.2s ease;filter:drop-shadow(0 0 8px currentColor)}
.gauge-content{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);text-align:center;display:flex;flex-direction:column;gap:4px}
.gauge-percent{font-family:var(--font-display);font-size:2.2rem;font-weight:700;color:var(--cyan-main);text-shadow:0 0 20px rgba(6,182,212,.6)}
.gauge-label{font-size:.6rem;letter-spacing:2px;color:var(--text-darker);text-transform:uppercase}
.reasons h3{font-family:var(--font-mono);font-size:.9rem;letter-spacing:3px;color:var(--cyan-light);margin-bottom:14px;text-transform:uppercase;display:flex;align-items:center;gap:8px;font-weight:700}
.h3-marker{color:var(--cyan-main);text-shadow:0 0 10px rgba(6,182,212,.6)}
#reasonsList{list-style:none;display:flex;flex-direction:column;gap:8px}
#reasonsList li{background:rgba(239,68,68,.06);border-left:3px solid var(--danger);padding:12px 16px;border-radius:4px;color:var(--text-main);font-size:.82rem;font-family:var(--font-mono);animation:slideIn .3s ease backwards}
#reasonsList li.safe{background:rgba(16,185,129,.06);border-left-color:var(--success)}
.advice{background:rgba(6,182,212,.06);border:1px solid var(--cyan-main);border-radius:8px;padding:16px;text-align:center}
.advice.safe{background:rgba(16,185,129,.06);border-color:#10B981}
.advice.warning{background:rgba(245,158,11,.06);border-color:#F59E0B}
.advice.danger{background:rgba(239,68,68,.06);border-color:#EF4444}
#adviceText{color:var(--cyan-light);font-size:.85rem;letter-spacing:1.5px;font-weight:500;text-transform:uppercase}
.advice.safe #adviceText{color:#10B981}.advice.warning #adviceText{color:#F59E0B}.advice.danger #adviceText{color:#EF4444}
.result-actions{display:flex;gap:10px;flex-wrap:wrap}
.action-btn{flex:1;min-width:140px;display:flex;align-items:center;justify-content:center;gap:8px;background:transparent;border:1px solid var(--border-bright);color:var(--cyan-light);padding:12px 18px;border-radius:6px;font-family:var(--font-display);font-size:.7rem;font-weight:600;letter-spacing:2px;cursor:pointer;transition:all .3s ease;text-transform:uppercase}
.action-btn:hover{border-color:var(--cyan-main);color:var(--cyan-main);background:rgba(6,182,212,.05);box-shadow:0 0 20px rgba(6,182,212,.15)}
.history-panel{background:linear-gradient(135deg,rgba(30,41,59,.95),rgba(11,17,32,.95));padding:24px;border-radius:12px;border:1px solid var(--border);width:100%;animation:fadeIn .6s ease}
.history-list{list-style:none;display:flex;flex-direction:column;gap:8px;max-height:220px;overflow-y:auto;padding-right:6px}
.history-list li{display:flex;justify-content:space-between;align-items:center;gap:12px;background:rgba(6,182,212,.03);border-left:2px solid var(--cyan-dim);padding:10px 14px;border-radius:4px;font-size:.78rem;font-family:var(--font-mono);animation:slideIn .3s ease}
.history-url{flex:1;color:var(--text-dim);overflow:hidden;text-overflow:ellipsis;white-space:nowrap;direction:ltr;text-align:left}
.history-score{font-family:var(--font-display);font-weight:700;font-size:.85rem;padding:2px 8px;border-radius:4px;min-width:45px;text-align:center}
.history-score.safe{color:#10B981;background:rgba(16,185,129,.1)}
.history-score.warning{color:#F59E0B;background:rgba(245,158,11,.1)}
.history-score.danger{color:#EF4444;background:rgba(239,68,68,.1)}
.clear-history-btn{background:transparent;border:1px solid var(--danger);color:var(--danger);font-family:var(--font-display);font-size:.6rem;font-weight:700;letter-spacing:2px;padding:5px 12px;border-radius:4px;cursor:pointer;transition:all .3s ease;margin-left:auto;text-transform:uppercase}
.clear-history-btn:hover{background:var(--danger);color:#0B1120;box-shadow:0 0 15px rgba(239,68,68,.6)}
.history-delete-btn{background:transparent;border:none;color:var(--danger);font-size:.9rem;cursor:pointer;padding:2px 8px;border-radius:3px;transition:all .2s ease;line-height:1;opacity:.5;font-family:var(--font-mono)}
.history-delete-btn:hover{opacity:1;background:rgba(239,68,68,.15);transform:scale(1.15)}
.page-footer{display:flex;align-items:center;justify-content:center;gap:12px;padding:10px 0}
.footer-line{flex:0 0 40px;height:1px;background:linear-gradient(90deg,transparent,var(--cyan-dim),transparent)}
.footer-dot{width:5px;height:5px;background:var(--cyan-main);border-radius:50%;box-shadow:0 0 10px rgba(6,182,212,.6);animation:dotPulse 2s ease-in-out infinite}
.footer-text{font-family:var(--font-display);font-size:.65rem;letter-spacing:3px;color:var(--text-darker)}
.validation-error{background:rgba(239,68,68,.08);border:2px solid #EF4444;color:#EF4444;padding:14px 18px;border-radius:8px;font-family:'JetBrains Mono',monospace;font-size:.85rem;margin-top:12px;animation:slideIn .3s ease;text-align:center;letter-spacing:1px}
@keyframes fadeIn{from{opacity:0;transform:translateY(15px)}to{opacity:1;transform:translateY(0)}}
@keyframes slideIn{from{opacity:0;transform:translateX(-15px)}to{opacity:1;transform:translateX(0)}}
@media (max-width:600px){body{padding:20px 12px}.container{gap:18px}.hero-title{font-size:1.05rem;letter-spacing:2px;margin-top:15px}.hero-subtitle{font-size:.65rem;letter-spacing:2px}.hero-shield{width:55px;height:55px}.hero-rings{width:180px;height:180px}.ring-1{width:90px;height:90px}.ring-2{width:130px;height:130px}.ring-3{width:180px;height:180px}.hero-orbit{display:none}.input-panel,.result-panel,.history-panel{padding:18px}.input-wrapper{flex-direction:column}#urlInput,#scanBtn{width:100%}}
</style>
</head>
<body>
<div class="cyber-bg"><div class="bg-grid"></div><div class="bg-glow bg-glow-1"></div><div class="bg-glow bg-glow-2"></div></div>
<main class="container">
<header class="hero-section">
<div class="hero-rings"><div class="ring ring-1"></div><div class="ring ring-2"></div><div class="ring ring-3"></div></div>
<div class="hero-shield"><svg viewBox="0 0 24 24" fill="none"><path d="M12 2L4 5V11C4 16 7.5 20.5 12 22C16.5 20.5 20 16 20 11V5L12 2Z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="M9 12L11 14L15 10" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
<div class="hero-orbit">
<div class="orbit-item orbit-1"><svg viewBox="0 0 24 24" fill="none"><path d="M10 13a5 5 0 007.54.54l3-3a5 5 0 00-7.07-7.07l-1.72 1.71" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><path d="M14 11a5 5 0 00-7.54-.54l-3 3a5 5 0 007.07 7.07l1.71-1.71" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg></div>
<div class="orbit-item orbit-2"><svg viewBox="0 0 24 24" fill="none"><path d="M12 9v4M12 17h.01M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
<div class="orbit-item orbit-3"><svg viewBox="0 0 24 24" fill="none"><rect x="3" y="11" width="18" height="11" rx="2" stroke="currentColor" stroke-width="1.5"/><path d="M7 11V7a5 5 0 0110 0v4" stroke="currentColor" stroke-width="1.5"/></svg></div>
<div class="orbit-item orbit-4"><svg viewBox="0 0 24 24" fill="none"><circle cx="11" cy="11" r="8" stroke="currentColor" stroke-width="1.5"/><path d="M21 21l-4.35-4.35" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg></div>
</div>
<h1 class="hero-title">PHISHING LINK SCANNER</h1>
<p class="hero-subtitle">Think before you click</p>
</header>
<section class="input-panel">
<div class="panel-header"><span class="panel-dot"></span><span class="panel-title">URL INPUT</span></div>
<div class="input-wrapper"><input type="text" id="urlInput" placeholder="https://example.com" autocomplete="off"><button id="scanBtn"><span>SCAN</span></button></div>
</section>
<section class="terminal-panel" id="terminalPanel" style="display:none">
<div class="terminal-header"><div class="terminal-dots"><span class="dot dot-red"></span><span class="dot dot-yellow"></span><span class="dot dot-green"></span></div><span class="terminal-title">cyber4ce@scanner: ~</span><button class="skip-btn" id="skipBtn">SKIP</button></div>
<div class="terminal-body" id="terminalBody"></div>
</section>
<section class="result-panel" id="resultSection" style="display:none">
<div class="panel-header"><span class="panel-dot"></span><span class="panel-title">ANALYSIS RESULT</span></div>
<div class="scanned-url"><span class="scanned-label">SCANNED URL</span><span class="scanned-value" id="scannedUrl"></span></div>
<div class="alert-banner" id="alertBanner"><span class="alert-icon" id="alertIcon">!</span><span class="alert-text" id="alertText">SCANNING...</span></div>
<div class="risk-section"><div class="risk-gauge"><svg viewBox="0 0 200 200" class="gauge-svg"><circle class="gauge-bg" cx="100" cy="100" r="85"></circle><circle class="gauge-fill" cx="100" cy="100" r="85" id="gaugeFill"></circle></svg><div class="gauge-content"><span class="gauge-percent" id="riskPercent">0%</span><span class="gauge-label">THREAT LEVEL</span></div></div></div>
<div class="reasons"><h3><span class="h3-marker">&#9670;</span> DETECTED ISSUES</h3><ul id="reasonsList"></ul></div>
<div class="advice" id="adviceBox"><p id="adviceText"></p></div>
<div class="result-actions"><button class="action-btn" id="copyBtn"><span>COPY REPORT</span></button><button class="action-btn" id="clearBtn"><span>NEW SCAN</span></button></div>
</section>
<section class="history-panel" id="historyPanel" style="display:none">
<div class="panel-header">
<span class="panel-dot"></span>
<span class="panel-title">RECENT SCANS</span>
<button class="clear-history-btn" id="clearHistoryBtn">🗑 CLEAR ALL</button>
</div>
<ul class="history-list" id="historyList"></ul>
</section>
<footer class="page-footer"><span class="footer-line"></span><span class="footer-dot"></span><span class="footer-text">SECURE &#183; ANALYZE &#183; PROTECT</span><span class="footer-dot"></span><span class="footer-line"></span></footer>
</main>
<script>
function getStorage(){try{if(typeof(Storage)!=="undefined"&&window.localStorage){window.localStorage.setItem("__test__","1");window.localStorage.removeItem("__test__");return window.localStorage}}catch(e){}return null}
function getAudioContext(){try{var AC=window.AudioContext||window.webkitAudioContext;if(AC)return new AC()}catch(e){}return null}
function copyToClipboard(text){try{if(navigator.clipboard&&navigator.clipboard.writeText)return navigator.clipboard.writeText(text)}catch(e){}try{var ta=document.createElement("textarea");ta.value=text;ta.style.position="fixed";ta.style.opacity="0";document.body.appendChild(ta);ta.select();document.execCommand("copy");document.body.removeChild(ta);return Promise.resolve()}catch(e){return Promise.reject(e)}}
var urlInput=document.getElementById("urlInput");
var scanBtn=document.getElementById("scanBtn");
var terminalPanel=document.getElementById("terminalPanel");
var terminalBody=document.getElementById("terminalBody");
var skipBtn=document.getElementById("skipBtn");
var resultSection=document.getElementById("resultSection");
var scannedUrl=document.getElementById("scannedUrl");
var alertBanner=document.getElementById("alertBanner");
var alertIcon=document.getElementById("alertIcon");
var alertText=document.getElementById("alertText");
var riskPercent=document.getElementById("riskPercent");
var gaugeFill=document.getElementById("gaugeFill");
var reasonsList=document.getElementById("reasonsList");
var adviceText=document.getElementById("adviceText");
var adviceBox=document.getElementById("adviceBox");
var copyBtn=document.getElementById("copyBtn");
var clearBtn=document.getElementById("clearBtn");
var historyPanel=document.getElementById("historyPanel");
var historyList=document.getElementById("historyList");
var STORAGE_KEY="cyber4ce_scan_history";
var MAX_HISTORY=5;
var GAUGE_CIRCUMFERENCE=534;
var terminalCancelled=false;
var currentAudioContext=null;

function isValidURL(url){
if(!url||url.length<4)return false;
var urlPattern=/^(https?:\/\/)?([\w-]+\.)+[\w-]{2,}(\/[\w\-._~:\/?#[\]@!$&'()*+,;=]*)?$/i;
return urlPattern.test(url);
}

function showValidationError(message){
var oldError=document.getElementById("validationError");
if(oldError)oldError.remove();
var errorDiv=document.createElement("div");
errorDiv.id="validationError";
errorDiv.className="validation-error";
errorDiv.textContent=message;
var inputPanel=document.querySelector(".input-panel");
inputPanel.appendChild(errorDiv);
setTimeout(function(){if(errorDiv.parentNode)errorDiv.remove()},4000);
}

function analyzeURL(url){
var score=0;var issues=[];var lowerUrl=url.toLowerCase();
if(url.length>75){score+=10;issues.push("URL is too long ("+url.length+" chars)")}
if(lowerUrl.indexOf("http://")===0){score+=20;issues.push("Uses insecure HTTP (not encrypted)")}
var ipPattern=new RegExp("\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}");
if(ipPattern.test(url)){score+=25;issues.push("Uses IP address instead of domain")}
if(url.indexOf("@")!==-1){score+=25;issues.push('Contains "@" symbol (visual trick)')}
var typos=["rnicrosoft","paypa1","g00gle","app1e","faceb00k","arnazon","yaho0","netfl1x"];
for(var i=0;i<typos.length;i++){if(lowerUrl.indexOf(typos[i])!==-1){score+=30;issues.push('Brand impersonation: "'+typos[i]+'"')}}
var words=["login","verify","update","account","secure","bank","signin","confirm","password"];
var found=[];
for(var j=0;j<words.length;j++){if(lowerUrl.indexOf(words[j])!==-1){score+=8;found.push(words[j])}}
if(found.length>0)issues.push("Suspicious keywords: "+found.join(", "));
var badTlds=[".xyz",".tk",".ml",".ga",".cf",".gq",".top",".work",".click"];
for(var k=0;k<badTlds.length;k++){if(lowerUrl.indexOf(badTlds[k])!==-1){score+=20;issues.push('Suspicious extension: "'+badTlds[k]+'"')}}
var dashMatches=url.match(/-/g);
var dashCount=dashMatches?dashMatches.length:0;
if(dashCount>3){score+=10;issues.push("Too many hyphens ("+dashCount+")")}
var domain=url.replace(/https?:\/\//,"").split("/")[0];
var numPattern=new RegExp("\\d");
if(numPattern.test(domain)){score+=12;issues.push("Numbers in domain name")}
var subs=domain.split(".").length;
if(subs>4){score+=15;issues.push("Too many subdomains ("+subs+")")}
var shorteners=["bit.ly","tinyurl","t.co","goo.gl","ow.ly","short.link","rb.gy","cutt.ly"];
for(var s=0;s<shorteners.length;s++){if(lowerUrl.indexOf(shorteners[s])!==-1){score+=15;issues.push("URL shortener detected (hides real destination)");break;}}
if(lowerUrl.indexOf("xn--")!==-1){score+=30;issues.push("Punycode detected (possible homograph attack)")}
if(lowerUrl.indexOf("data:")===0){score+=40;issues.push("Data URL detected (can execute malicious code)")}
if(url.length>150){score+=15;issues.push("Extremely long URL ("+url.length+" chars)")}
var atCount=(url.match(/@/g)||[]).length;
if(atCount>1){score+=20;issues.push("Multiple @ symbols (visual spoofing)")}
if(score>100)score=100;
return{score:score,issues:issues}
}

function getLevelInfo(score){
if(score<30)return{level:"safe",icon:"\u2713",alertMsg:"\u0622\u0645\u0646 | SAFE",adviceMsg:"\u064A\u0645\u0643\u0646\u0643 \u0627\u0644\u0645\u062A\u0627\u0628\u0639\u0629 | Safe to proceed",color:"#10B981"};
if(score<60)return{level:"warning",icon:"\u26A0",alertMsg:"\u062A\u062D\u0630\u064A\u0631 | WARNING",adviceMsg:"\u062A\u062D\u0642\u0642 \u0645\u0646 \u0627\u0644\u0645\u0635\u062F\u0631 | Verify before clicking",color:"#F59E0B"};
return{level:"danger",icon:"\uD83D\uDEA8",alertMsg:"\u062E\u0637\u0631 | DANGER",adviceMsg:"\u0644\u0627 \u062A\u0641\u062A\u062D \u0647\u0630\u0627 \u0627\u0644\u0631\u0627\u0628\u0637 | Do NOT open this link",color:"#EF4444"}
}

function playBeep(freq,dur,delay){delay=delay||0;try{if(!currentAudioContext)currentAudioContext=getAudioContext();if(!currentAudioContext)return;setTimeout(function(){try{var osc=currentAudioContext.createOscillator();var gain=currentAudioContext.createGain();osc.connect(gain);gain.connect(currentAudioContext.destination);osc.frequency.value=freq;osc.type="sine";gain.gain.setValueAtTime(0.08,currentAudioContext.currentTime);gain.gain.exponentialRampToValueAtTime(0.001,currentAudioContext.currentTime+dur);osc.start(currentAudioContext.currentTime);osc.stop(currentAudioContext.currentTime+dur)}catch(e){}},delay)}catch(e){}}
function playResultSound(level){if(level==="safe")playBeep(880,0.15,0);else if(level==="warning"){playBeep(660,0.15,0);playBeep(660,0.15,200)}else{playBeep(220,0.4,0);playBeep(180,0.5,300)}}
function sleep(ms){return new Promise(function(r){setTimeout(r,ms)})}
function typeLine(text,colorClass,speed){
colorClass=colorClass||"term-ok";speed=speed||12;
return new Promise(function(resolve){
if(terminalCancelled){resolve();return}
var line=document.createElement("span");
line.className="term-line "+colorClass;
terminalBody.appendChild(line);
var i=0;
function typeChar(){if(terminalCancelled||i>=text.length){terminalBody.appendChild(document.createElement("br"));resolve();return}line.textContent+=text.charAt(i);terminalBody.scrollTop=terminalBody.scrollHeight;i++;setTimeout(typeChar,speed)}
typeChar()
})
}
function runTerminal(url,result){
terminalPanel.style.display="block";
terminalBody.innerHTML="";
terminalCancelled=false;
var hasHttp=url.toLowerCase().indexOf("http://")===0;
var hasTypos=result.issues.some(function(i){return i.indexOf("impersonation")!==-1});
var hasKeywords=result.issues.some(function(i){return i.indexOf("keywords")!==-1});
var hasBadTld=result.issues.some(function(i){return i.indexOf("extension")!==-1});
var hasIp=result.issues.some(function(i){return i.indexOf("IP address")!==-1});
var hasAt=result.issues.some(function(i){return i.indexOf("@")!==-1});
var chain=Promise.resolve();
chain=chain.then(function(){return typeLine("$ cyber4ce scan "+url,"term-cmd",8)}).then(function(){return sleep(180)});
chain=chain.then(function(){return typeLine("[OK] Initializing scanner v2.1...","term-ok")}).then(function(){return sleep(120)});
chain=chain.then(function(){return typeLine("[OK] Parsing URL structure...","term-ok")}).then(function(){return sleep(120)});
chain=chain.then(function(){return hasHttp?typeLine("[!] Warning: HTTP detected (insecure)","term-warn"):typeLine("[OK] Protocol: HTTPS (secure)","term-ok")}).then(function(){return sleep(120)});
chain=chain.then(function(){return typeLine("[OK] Analyzing domain reputation...","term-ok")}).then(function(){return sleep(120)});
chain=chain.then(function(){return hasTypos?typeLine("[!] Brand impersonation detected!","term-warn"):typeLine("[OK] No typosquatting patterns","term-ok")}).then(function(){return sleep(120)});
chain=chain.then(function(){return hasKeywords?typeLine("[!] Suspicious keywords found","term-warn"):typeLine("[OK] No suspicious keywords","term-ok")}).then(function(){return sleep(120)});
chain=chain.then(function(){return hasBadTld?typeLine("[!] High-risk TLD detected","term-warn"):typeLine("[OK] TLD reputation OK","term-ok")}).then(function(){return sleep(120)});
if(hasIp)chain=chain.then(function(){return typeLine("[!] IP address used instead of domain","term-warn")});
if(hasAt)chain=chain.then(function(){return typeLine('[!] "@" symbol detected (visual trick)',"term-warn")});
chain=chain.then(function(){return typeLine("[OK] Calculating risk score...","term-ok")}).then(function(){return sleep(180)});
var statusText=result.score>=60?"THREAT DETECTED":result.score>=30?"SUSPICIOUS":"CLEAN";
var statusClass=result.score>=60?"term-err":result.score>=30?"term-warn":"term-ok";
chain=chain.then(function(){return typeLine("> Result: "+result.score+"% - "+statusText,statusClass,10)}).then(function(){return sleep(400)});
chain=chain.then(function(){
if(!terminalCancelled){
var cur=document.createElement("span");
cur.className="term-line term-info";
cur.textContent="> Loading report";
var c=document.createElement("span");
c.className="term-cursor";
cur.appendChild(c);
terminalBody.appendChild(cur);
terminalBody.scrollTop=terminalBody.scrollHeight;
return sleep(500)
}
});
return chain.then(function(){
if(!terminalCancelled){
terminalPanel.style.display="none";
showResult(result.score,result.issues)
}
})
}
function showResult(score,issues){
resultSection.style.display="flex";
alertBanner.classList.remove("safe","warning","danger");
adviceBox.classList.remove("safe","warning","danger");
var info=getLevelInfo(score);
scannedUrl.textContent=urlInput.value.trim();
alertBanner.classList.add(info.level);
alertIcon.textContent=info.icon;
alertText.textContent=info.alertMsg;
riskPercent.textContent=score+"%";
riskPercent.style.color=info.color;
riskPercent.style.textShadow="0 0 20px "+info.color;
var offset=GAUGE_CIRCUMFERENCE-(GAUGE_CIRCUMFERENCE*score/100);
gaugeFill.style.stroke=info.color;
gaugeFill.style.strokeDashoffset=offset;
reasonsList.innerHTML="";
if(issues.length===0){
var li=document.createElement("li");
li.textContent="\u2713 \u0644\u0627 \u062A\u0648\u062C\u062F \u0645\u0634\u0627\u0643\u0644 | No issues detected";
li.classList.add("safe");
reasonsList.appendChild(li)
}else{
issues.forEach(function(issue,index){
var li=document.createElement("li");
li.textContent="\u2717 "+issue;
li.style.animationDelay=(index*0.08)+"s";
reasonsList.appendChild(li)
})
}
adviceBox.classList.add(info.level);
adviceText.textContent=info.adviceMsg;
playResultSound(info.level);
saveToHistory(urlInput.value.trim(),score,info.level)
}
function saveToHistory(url,score,level){
var storage=getStorage();
if(!storage)return;
try{
var h=getHistory();
h=h.filter(function(item){return item.url!==url});
h.unshift({url:url,score:score,level:level,time:Date.now()});
h=h.slice(0,MAX_HISTORY);
storage.setItem(STORAGE_KEY,JSON.stringify(h));
renderHistory()
}catch(e){}
}
function getHistory(){
var storage=getStorage();
if(!storage)return[];
try{
var data=storage.getItem(STORAGE_KEY);
return data?JSON.parse(data):[]
}catch(e){return[]}
}
function renderHistory(){
var history=getHistory();
if(history.length===0){historyPanel.style.display="none";return}
historyPanel.style.display="block";
historyList.innerHTML="";
history.forEach(function(item){
var li=document.createElement("li");
var u=document.createElement("span");
u.className="history-url";
u.textContent=item.url;
u.title=item.url;
var s=document.createElement("span");
s.className="history-score "+item.level;
s.textContent=item.score+"%";
var delBtn=document.createElement("button");
delBtn.className="history-delete-btn";
delBtn.textContent="\u2715";
delBtn.title="Delete this scan";
delBtn.addEventListener("click",function(e){
e.stopPropagation();
deleteHistoryItem(item.url);
});
li.appendChild(u);
li.appendChild(s);
li.appendChild(delBtn);
li.style.cursor="pointer";
li.addEventListener("click",function(){urlInput.value=item.url;urlInput.focus()});
historyList.appendChild(li)
})
}

function deleteHistoryItem(url){
var storage=getStorage();
if(!storage)return;
try{
var h=getHistory();
h=h.filter(function(item){return item.url!==url});
storage.setItem(STORAGE_KEY,JSON.stringify(h));
renderHistory();
}catch(e){}
}

function clearAllHistory(){
var storage=getStorage();
if(!storage)return;
try{
storage.removeItem(STORAGE_KEY);
renderHistory();
}catch(e){}
}

function copyReport(){
var url=urlInput.value.trim();
var score=riskPercent.textContent;
var advice=adviceText.textContent;
var issues=[];
document.querySelectorAll("#reasonsList li").forEach(function(li){issues.push(li.textContent)});
var report="CYBER4CE - PHISHING SCANNER\n==============================\n\n";
report+="URL: "+url+"\nThreat Level: "+score+"\nStatus: "+advice+"\n\n";
report+="Detected Issues:\n";
issues.forEach(function(i){report+="  "+i+"\n"});
report+="\nScan Time: "+new Date().toLocaleString();
copyToClipboard(report).then(function(){
var orig=copyBtn.querySelector("span").textContent;
copyBtn.querySelector("span").textContent="COPIED!";
copyBtn.style.borderColor="#10B981";
copyBtn.style.color="#10B981";
setTimeout(function(){
copyBtn.querySelector("span").textContent=orig;
copyBtn.style.borderColor="";
copyBtn.style.color=""
},2000)
}).catch(function(){alert("Copy failed")})
}
function clearScan(){
urlInput.value="";
resultSection.style.display="none";
terminalPanel.style.display="none";
var oldError=document.getElementById("validationError");
if(oldError)oldError.remove();
urlInput.focus();
gaugeFill.style.strokeDashoffset=GAUGE_CIRCUMFERENCE;
riskPercent.textContent="0%"
}
function performScan(){
var url=urlInput.value.trim();
if(url===""){
urlInput.focus();
urlInput.style.borderColor="#EF4444";
showValidationError("\u26A0\uFE0F Please enter a URL first.");
setTimeout(function(){urlInput.style.borderColor=""},2000);
return
}
if(!isValidURL(url)){
urlInput.focus();
urlInput.style.borderColor="#EF4444";
showValidationError("\u274C Invalid URL format. Please enter a valid URL like: https://example.com");
setTimeout(function(){urlInput.style.borderColor=""},3000);
return
}
resultSection.style.display="none";
scanBtn.disabled=true;
scanBtn.style.opacity="0.5";
var result=analyzeURL(url);
runTerminal(url,result).then(function(){
scanBtn.disabled=false;
scanBtn.style.opacity="1"
})
}
scanBtn.addEventListener("click",performScan);
urlInput.addEventListener("keypress",function(e){if(e.key==="Enter")performScan()});
skipBtn.addEventListener("click",function(){
terminalCancelled=true;
terminalPanel.style.display="none";
var url=urlInput.value.trim();
var result=analyzeURL(url);
showResult(result.score,result.issues);
scanBtn.disabled=false;
scanBtn.style.opacity="1"
});
copyBtn.addEventListener("click",copyReport);
clearBtn.addEventListener("click",clearScan);
document.getElementById("clearHistoryBtn").addEventListener("click",clearAllHistory);
document.addEventListener("DOMContentLoaded",function(){renderHistory()});
</script>
</body>
</html>
"""

    components.html(html_code, height=900, scrolling=True)
