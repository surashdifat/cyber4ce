// ============================================
// Cyber4ce - Phishing Link Scanner
// Full Logic + Terminal Animation + Sound + History
// ============================================

// DOM Elements
const urlInput = document.getElementById('urlInput');
const scanBtn = document.getElementById('scanBtn');
const terminalPanel = document.getElementById('terminalPanel');
const terminalBody = document.getElementById('terminalBody');
const skipBtn = document.getElementById('skipBtn');
const resultSection = document.getElementById('resultSection');
const scannedUrl = document.getElementById('scannedUrl');
const alertBanner = document.getElementById('alertBanner');
const alertIcon = document.getElementById('alertIcon');
const alertText = document.getElementById('alertText');
const riskPercent = document.getElementById('riskPercent');
const gaugeFill = document.getElementById('gaugeFill');
const reasonsList = document.getElementById('reasonsList');
const adviceText = document.getElementById('adviceText');
const adviceBox = document.getElementById('adviceBox');
const copyBtn = document.getElementById('copyBtn');
const clearBtn = document.getElementById('clearBtn');
const historyPanel = document.getElementById('historyPanel');
const historyList = document.getElementById('historyList');

// CONFIG
const STORAGE_KEY = 'cyber4ce_scan_history';
const MAX_HISTORY = 5;
const GAUGE_CIRCUMFERENCE = 534;

// Terminal state
let terminalCancelled = false;
let currentAudioContext = null;

// ============================================
// Analyze URL
// ============================================
function analyzeURL(url) {
    let score = 0;
    const issues = [];
    const lowerUrl = url.toLowerCase();

    if (url.length > 75) {
        score += 10;
        issues.push('URL is too long (' + url.length + ' chars)');
    }

    if (lowerUrl.startsWith('http://')) {
        score += 20;
        issues.push('Uses insecure HTTP (not encrypted)');
    }

    const ipPattern = /\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/;
    if (ipPattern.test(url)) {
        score += 25;
        issues.push('Uses IP address instead of domain');
    }

    if (url.includes('@')) {
        score += 25;
        issues.push('Contains "@" symbol (visual trick)');
    }

    const typos = ['rnicrosoft', 'paypa1', 'g00gle', 'app1e', 'faceb00k', 'arnazon', 'yaho0', 'netfl1x'];
    for (let typo of typos) {
        if (lowerUrl.includes(typo)) {
            score += 30;
            issues.push('Brand impersonation: "' + typo + '"');
        }
    }

    const suspiciousWords = ['login', 'verify', 'update', 'account', 'secure', 'bank', 'signin', 'confirm', 'password'];
    const foundWords = [];
    for (let word of suspiciousWords) {
        if (lowerUrl.includes(word)) {
            score += 8;
            foundWords.push(word);
        }
    }
    if (foundWords.length > 0) {
        issues.push('Suspicious keywords: ' + foundWords.join(', '));
    }

    const badTlds = ['.xyz', '.tk', '.ml', '.ga', '.cf', '.gq', '.top', '.work', '.click'];
    for (let tld of badTlds) {
        if (lowerUrl.includes(tld)) {
            score += 20;
            issues.push('Suspicious extension: "' + tld + '"');
        }
    }

    const dashCount = (url.match(/-/g) || []).length;
    if (dashCount > 3) {
        score += 10;
        issues.push('Too many hyphens (' + dashCount + ')');
    }

    const domain = url.replace(/https?:\/\//, '').split('/')[0];
    if (/\d/.test(domain)) {
        score += 12;
        issues.push('Numbers in domain name');
    }

    const subdomains = domain.split('.').length;
    if (subdomains > 4) {
        score += 15;
        issues.push('Too many subdomains (' + subdomains + ')');
    }

    if (score > 100) score = 100;

    return { score, issues };
}

// ============================================
// Level Info
// ============================================
function getLevelInfo(score) {
    if (score < 30) {
        return {
            level: 'safe',
            icon: '✓',
            alertMsg: 'آمن  |  SAFE',
            adviceMsg: 'يمكنك المتابعة بحذر  |  Safe to proceed',
            color: '#00ff9f'
        };
    } else if (score < 60) {
        return {
            level: 'warning',
            icon: '⚠',
            alertMsg: 'تحذير  |  WARNING',
            adviceMsg: 'تحقق من المصدر قبل الفتح  |  Verify before clicking',
            color: '#ffb340'
        };
    } else {
        return {
            level: 'danger',
            icon: '🚨',
            alertMsg: 'خطر  |  DANGER',
            adviceMsg: 'لا تفتح هذا الرابط  |  Do NOT open this link',
            color: '#ff3333'
        };
    }
}

// ============================================
// Sound (Web Audio API - no files needed)
// ============================================
function playBeep(frequency, duration, delay = 0) {
    try {
        if (!currentAudioContext) {
            currentAudioContext = new (window.AudioContext || window.webkitAudioContext)();
        }
        const ctx = currentAudioContext;
        
        setTimeout(() => {
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();
            
            osc.connect(gain);
            gain.connect(ctx.destination);
            
            osc.frequency.value = frequency;
            osc.type = 'sine';
            
            gain.gain.setValueAtTime(0.08, ctx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);
            
            osc.start(ctx.currentTime);
            osc.stop(ctx.currentTime + duration);
        }, delay);
    } catch (e) {
        // Silent fail
    }
}

function playResultSound(level) {
    if (level === 'safe') {
        playBeep(880, 0.15, 0);
    } else if (level === 'warning') {
        playBeep(660, 0.15, 0);
        playBeep(660, 0.15, 200);
    } else {
        playBeep(220, 0.4, 0);
        playBeep(180, 0.5, 300);
    }
}

// ============================================
// Terminal Animation
// ============================================
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function typeLine(text, colorClass = 'term-ok', speed = 12) {
    if (terminalCancelled) return;
    
    const line = document.createElement('span');
    line.className = 'term-line ' + colorClass;
    terminalBody.appendChild(line);
    
    for (let i = 0; i < text.length; i++) {
        if (terminalCancelled) break;
        line.textContent += text[i];
        terminalBody.scrollTop = terminalBody.scrollHeight;
        await sleep(speed);
    }
    
    // Add newline
    terminalBody.appendChild(document.createElement('br'));
}

async function runTerminal(url, result) {
    terminalPanel.style.display = 'block';
    terminalBody.innerHTML = '';
    terminalCancelled = false;
    
    const hasHttp = url.toLowerCase().startsWith('http://');
    const hasTypos = result.issues.some(i => i.includes('impersonation'));
    const hasKeywords = result.issues.some(i => i.includes('keywords'));
    const hasBadTld = result.issues.some(i => i.includes('extension'));
    const hasIp = result.issues.some(i => i.includes('IP address'));
    const hasAt = result.issues.some(i => i.includes('@'));
    
    // 1. Command
    await typeLine('$ cyber4ce scan ' + url, 'term-cmd', 8);
    await sleep(180);
    
    // 2. Init
    await typeLine('[✓] Initializing scanner v2.1...', 'term-ok');
    await sleep(120);
    
    // 3. Parse
    await typeLine('[✓] Parsing URL structure...', 'term-ok');
    await sleep(120);
    
    // 4. Protocol check
    if (hasHttp) {
        await typeLine('[!] Warning: HTTP detected (insecure)', 'term-warn');
    } else {
        await typeLine('[✓] Protocol: HTTPS (secure)', 'term-ok');
    }
    await sleep(120);
    
    // 5. Domain
    await typeLine('[✓] Analyzing domain reputation...', 'term-ok');
    await sleep(120);
    
    // 6. Typosquatting
    if (hasTypos) {
        await typeLine('[!] Brand impersonation detected!', 'term-warn');
    } else {
        await typeLine('[✓] No typosquatting patterns', 'term-ok');
    }
    await sleep(120);
    
    // 7. Keywords
    if (hasKeywords) {
        await typeLine('[!] Suspicious keywords found', 'term-warn');
    } else {
        await typeLine('[✓] No suspicious keywords', 'term-ok');
    }
    await sleep(120);
    
    // 8. TLD
    if (hasBadTld) {
        await typeLine('[!] High-risk TLD detected', 'term-warn');
    } else {
        await typeLine('[✓] TLD reputation OK', 'term-ok');
    }
    await sleep(120);
    
    // 9. IP
    if (hasIp) {
        await typeLine('[!] IP address used instead of domain', 'term-warn');
    }
    
    // 10. @ symbol
    if (hasAt) {
        await typeLine('[!] "@" symbol detected (visual trick)', 'term-warn');
    }
    
    // 11. Calculate
    await typeLine('[✓] Calculating risk score...', 'term-ok');
    await sleep(180);
    
    // 12. Final
    const statusText = result.score >= 60 ? 'THREAT DETECTED' : 
                       result.score >= 30 ? 'SUSPICIOUS' : 'CLEAN';
    const statusClass = result.score >= 60 ? 'term-err' : 
                        result.score >= 30 ? 'term-warn' : 'term-ok';
    
    await typeLine('> Result: ' + result.score + '% - ' + statusText, statusClass, 10);
    await sleep(400);
    
    // 13. Cursor effect
    if (!terminalCancelled) {
        const cursorLine = document.createElement('span');
        cursorLine.className = 'term-line term-info';
        cursorLine.textContent = '> Loading report';
        const cursor = document.createElement('span');
        cursor.className = 'term-cursor';
        cursorLine.appendChild(cursor);
        terminalBody.appendChild(cursorLine);
        terminalBody.scrollTop = terminalBody.scrollHeight;
        
        await sleep(500);
    }
    
    // Done
    if (!terminalCancelled) {
        terminalPanel.style.display = 'none';
        showResult(result.score, result.issues);
    }
}

// ============================================
// Show Result
// ============================================
function showResult(score, issues) {
    resultSection.style.display = 'flex';

    alertBanner.classList.remove('safe', 'warning', 'danger');
    adviceBox.classList.remove('safe', 'warning', 'danger');

    const info = getLevelInfo(score);

    scannedUrl.textContent = urlInput.value.trim();

    alertBanner.classList.add(info.level);
    alertIcon.textContent = info.icon;
    alertText.textContent = info.alertMsg;

    riskPercent.textContent = score + '%';
    riskPercent.style.color = info.color;
    riskPercent.style.textShadow = '0 0 20px ' + info.color;

    const offset = GAUGE_CIRCUMFERENCE - (GAUGE_CIRCUMFERENCE * score / 100);
    gaugeFill.style.stroke = info.color;
    gaugeFill.style.strokeDashoffset = offset;

    reasonsList.innerHTML = '';
    if (issues.length === 0) {
        const li = document.createElement('li');
        li.textContent = '✓ لا توجد مشاكل  |  No issues detected';
        li.classList.add('safe');
        reasonsList.appendChild(li);
    } else {
        issues.forEach((issue, index) => {
            const li = document.createElement('li');
            li.textContent = '✗ ' + issue;
            li.style.animationDelay = (index * 0.08) + 's';
            reasonsList.appendChild(li);
        });
    }

    adviceBox.classList.add(info.level);
    adviceText.textContent = info.adviceMsg;

    // Play sound
    playResultSound(info.level);

    saveToHistory(urlInput.value.trim(), score, info.level);
}

// ============================================
// History
// ============================================
function saveToHistory(url, score, level) {
    let history = getHistory();
    history = history.filter(item => item.url !== url);
    history.unshift({ url, score, level, time: Date.now() });
    history = history.slice(0, MAX_HISTORY);
    localStorage.setItem(STORAGE_KEY, JSON.stringify(history));
    renderHistory();
}

function getHistory() {
    try {
        const data = localStorage.getItem(STORAGE_KEY);
        return data ? JSON.parse(data) : [];
    } catch (e) {
        return [];
    }
}

function renderHistory() {
    const history = getHistory();
    
    if (history.length === 0) {
        historyPanel.style.display = 'none';
        return;
    }
    
    historyPanel.style.display = 'block';
    historyList.innerHTML = '';
    
    history.forEach(item => {
        const li = document.createElement('li');
        
        const urlSpan = document.createElement('span');
        urlSpan.className = 'history-url';
        urlSpan.textContent = item.url;
        urlSpan.title = item.url;
        
        const scoreSpan = document.createElement('span');
        scoreSpan.className = 'history-score ' + item.level;
        scoreSpan.textContent = item.score + '%';
        
        li.appendChild(urlSpan);
        li.appendChild(scoreSpan);
        
        li.style.cursor = 'pointer';
        li.addEventListener('click', () => {
            urlInput.value = item.url;
            urlInput.focus();
        });
        
        historyList.appendChild(li);
    });
}

// ============================================
// Copy Report
// ============================================
function copyReport() {
    const url = urlInput.value.trim();
    const score = riskPercent.textContent;
    const advice = adviceText.textContent;
    
    const issues = [];
    document.querySelectorAll('#reasonsList li').forEach(li => {
        issues.push(li.textContent);
    });
    
    const report = `
╔══════════════════════════════════════╗
║   CYBER4CE - PHISHING SCANNER        ║
╚══════════════════════════════════════╝

URL: ${url}
Threat Level: ${score}
Status: ${advice}

Detected Issues:
${issues.map(i => '  ' + i).join('\n')}

Scan Time: ${new Date().toLocaleString()}
    `.trim();
    
    navigator.clipboard.writeText(report).then(() => {
        const originalText = copyBtn.querySelector('span').textContent;
        copyBtn.querySelector('span').textContent = 'COPIED!';
        copyBtn.style.borderColor = '#00ff9f';
        copyBtn.style.color = '#00ff9f';
        
        setTimeout(() => {
            copyBtn.querySelector('span').textContent = originalText;
            copyBtn.style.borderColor = '';
            copyBtn.style.color = '';
        }, 2000);
    });
}

// ============================================
// Clear
// ============================================
function clearScan() {
    urlInput.value = '';
    resultSection.style.display = 'none';
    terminalPanel.style.display = 'none';
    urlInput.focus();
    gaugeFill.style.strokeDashoffset = GAUGE_CIRCUMFERENCE;
    riskPercent.textContent = '0%';
}

// ============================================
// Perform Scan
// ============================================
async function performScan() {
    const url = urlInput.value.trim();

    if (url === '') {
        urlInput.focus();
        urlInput.style.borderColor = '#ff3333';
        setTimeout(() => { urlInput.style.borderColor = ''; }, 1000);
        return;
    }

    // Hide old result
    resultSection.style.display = 'none';
    
    // Disable scan button
    scanBtn.disabled = true;
    scanBtn.style.opacity = '0.5';
    
    const result = analyzeURL(url);
    
    // Run terminal animation
    await runTerminal(url, result);
    
    // Re-enable scan button
    scanBtn.disabled = false;
    scanBtn.style.opacity = '1';
}

// ============================================
// Events
// ============================================
scanBtn.addEventListener('click', performScan);

urlInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') performScan();
});

skipBtn.addEventListener('click', () => {
    terminalCancelled = true;
    terminalPanel.style.display = 'none';
    const url = urlInput.value.trim();
    const result = analyzeURL(url);
    showResult(result.score, result.issues);
    scanBtn.disabled = false;
    scanBtn.style.opacity = '1';
});

copyBtn.addEventListener('click', copyReport);

clearBtn.addEventListener('click', clearScan);

document.addEventListener('DOMContentLoaded', () => {
    renderHistory();
});