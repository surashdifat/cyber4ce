import streamlit as st
import streamlit.components.v1 as components

def render_service():
    # إخفاء هوامش Streamlit الافتراضية لملء الشاشة
    st.markdown("""
    <style>
        .block-container {padding: 0 !important; max-width: 100% !important;}
        .main .block-container {padding-top: 0 !important; padding-left: 0 !important; padding-right: 0 !important;}
        [data-testid="stAppViewContainer"] {padding: 0 !important;}
        header[data-testid="stHeader"] {height: 0 !important;}
        iframe {width: 100% !important; border: none !important; display: block !important;}
    </style>
    """, unsafe_allow_html=True)

    # كود الواجهة (HTML/CSS/JS)
    html_code = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Privacy Shield</title>
<!-- المكتبات القوية -->
<script src="https://cdn.jsdelivr.net/npm/exifr/dist/full.umd.js"></script>
<script src="https://cdn.jsdelivr.net/npm/pdf-lib/dist/pdf-lib.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/heic2any@0.0.4/dist/heic2any.min.js"></script>
<link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@700&display=swap" rel="stylesheet">
<style>
    :root {
        --bg-main: #0B1120;
        --bg-panel: #1E293B;
        --cyan-main: #06B6D4;
        --cyan-light: #22D3EE;
        --red-danger: #EF4444;
        --green-success: #10B981;
        --text-main: #E2E8F0;
        --text-dim: #94A3B8;
    }
    body {
        background-color: var(--bg-main);
        color: var(--text-main);
        font-family: 'Share Tech Mono', monospace;
        margin: 0;
        padding: 30px 20px;
        display: flex;
        flex-direction: column;
        align-items: center;
        overflow-x: hidden;
    }
    .container {
        max-width: 900px;
        width: 100%;
        background: linear-gradient(135deg, rgba(30,41,59,0.95), rgba(11,17,32,0.95));
        border: 1px solid var(--cyan-main);
        border-radius: 12px;
        padding: 30px;
        box-shadow: 0 0 30px rgba(6, 182, 212, 0.15);
    }
    h1 {
        font-family: 'Orbitron', sans-serif;
        color: var(--cyan-main);
        text-align: center;
        font-size: 2rem;
        margin-bottom: 10px;
        text-shadow: 0 0 15px rgba(6, 182, 212, 0.6);
        letter-spacing: 2px;
    }
    p.subtitle {
        text-align: center;
        color: var(--text-dim);
        font-size: 0.9rem;
        margin-bottom: 30px;
        letter-spacing: 1px;
    }
    .drop-zone {
        border: 2px dashed #334155;
        border-radius: 10px;
        padding: 40px;
        text-align: center;
        transition: all 0.3s ease;
        cursor: pointer;
        background-color: rgba(15, 23, 42, 0.5);
    }
    .drop-zone:hover, .drop-zone.dragover {
        border-color: var(--cyan-main);
        background-color: rgba(6, 182, 212, 0.05);
        box-shadow: inset 0 0 20px rgba(6, 182, 212, 0.1);
    }
    .drop-zone input[type="file"] { display: none; }
    .drop-zone label {
        cursor: pointer;
        color: var(--cyan-light);
        font-size: 1.1rem;
        font-weight: bold;
    }
    .drop-zone p { color: var(--text-dim); font-size: 0.8rem; margin-top: 10px; }
    
    /* شاشة النتائج */
    #resultsArea { display: none; margin-top: 30px; animation: fadeIn 0.5s ease; }
    .data-box {
        background-color: #000;
        border: 1px solid #334155;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 20px;
        max-height: 300px;
        overflow-y: auto;
        font-size: 0.85rem;
    }
    .data-box h3 {
        color: var(--red-danger);
        margin: 0 0 10px 0;
        font-size: 1rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .data-item {
        color: #10B981;
        margin-bottom: 5px;
        border-bottom: 1px solid #1E293B;
        padding-bottom: 5px;
    }
    .data-item span.key { color: var(--cyan-light); font-weight: bold; }
    
    /* الصورة المصغرة */
    #thumbnailContainer { display: none; margin-top: 15px; text-align: center; }
    #thumbnailImage { max-width: 200px; border: 2px solid var(--red-danger); border-radius: 5px; box-shadow: 0 0 15px rgba(239,68,68,0.5); }
    .thumbnail-warning { color: var(--red-danger); font-weight: bold; margin-bottom: 10px; }

    /* الخريطة */
    #mapContainer { display: none; margin-top: 20px; border-radius: 8px; overflow: hidden; border: 1px solid var(--cyan-main); }
    
    /* الأزرار */
    .btn {
        background: transparent;
        color: var(--cyan-main);
        border: 2px solid var(--cyan-main);
        padding: 12px 24px;
        border-radius: 8px;
        font-family: 'Orbitron', sans-serif;
        font-weight: bold;
        letter-spacing: 2px;
        cursor: pointer;
        transition: all 0.3s ease;
        width: 100%;
        margin-top: 15px;
        font-size: 1rem;
    }
    .btn:hover { background: var(--cyan-main); color: var(--bg-main); box-shadow: 0 0 20px var(--cyan-main); }
    .btn-success { border-color: var(--green-success); color: var(--green-success); }
    .btn-success:hover { background: var(--green-success); color: var(--bg-main); box-shadow: 0 0 20px var(--green-success); }
    
    @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
    .hidden { display: none !important; }
</style>
</head>
<body>

<div class="container">
    <h1>🛡️ PRIVACY SHIELD</h1>
    <p class="subtitle">Zero-Knowledge Metadata Sanitizer (Images & PDFs)</p>

    <!-- منطقة الرفع -->
    <div class="drop-zone" id="dropZone">
        <label for="fileInput">📂 Click to Upload an Image / PDF</label>
        <p>We support JPG, PNG, HEIC, PDF (Processed 100% locally in your browser)</p>
        <!-- بدون خاصية capture لإجبار المستخدم على اختيار ملف -->
        <input type="file" id="fileInput" accept="image/jpeg, image/png, image/heic, image/heif, application/pdf">
    </div>

    <!-- منطقة النتائج -->
    <div id="resultsArea">
        <div class="data-box">
            <h3>⚠️ EXPOSED METADATA DETECTED:</h3>
            <div id="metadataList"></div>
        </div>

        <div id="thumbnailContainer" class="data-box">
            <div class="thumbnail-warning">🚨 HIDDEN THUMBNAIL FOUND! 🚨</div>
            <img id="thumbnailImage" src="" alt="Hidden Thumbnail">
        </div>

        <div id="mapContainer">
            <iframe id="mapIframe" width="100%" height="250" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
        </div>

        <!-- أزرار الاختيار (تحليل فقط، أو تنظيف) -->
        <div id="actionButtons" style="display: flex; gap: 10px; margin-top: 15px;">
            <button class="btn" id="cleanBtn" style="flex: 1;">🧹 CLEAN & DOWNLOAD</button>
            <button class="btn" id="discardBtn" style="flex: 1; border-color: #94A3B8; color: #94A3B8;">🗑️ DISCARD (VIEW ONLY)</button>
        </div>
        
        <div id="downloadArea" class="hidden" style="margin-top: 20px; text-align: center;">
            <p style="color: var(--green-success); font-weight: bold; margin-bottom: 10px;">✅ FILE CLEANED SUCCESSFULLY!</p>
            <button class="btn btn-success" id="downloadBtn">⬇️ DOWNLOAD CLEAN FILE</button>
            <button class="btn" id="resetBtn" style="margin-top: 10px; border-color: #94A3B8; color: #94A3B8;">🔄 SCAN ANOTHER FILE</button>
        </div>
    </div>
</div>

<script>
    const dropZone = document.getElementById('dropZone');
    const fileInput = document.getElementById('fileInput');
    const resultsArea = document.getElementById('resultsArea');
    const metadataList = document.getElementById('metadataList');
    const thumbnailContainer = document.getElementById('thumbnailContainer');
    const thumbnailImage = document.getElementById('thumbnailImage');
    const mapContainer = document.getElementById('mapContainer');
    const mapIframe = document.getElementById('mapIframe');
    const cleanBtn = document.getElementById('cleanBtn');
    const discardBtn = document.getElementById('discardBtn');
    const actionButtons = document.getElementById('actionButtons');
    const downloadArea = document.getElementById('downloadArea');
    const downloadBtn = document.getElementById('downloadBtn');
    const resetBtn = document.getElementById('resetBtn');

    let currentFile = null;
    let originalFileName = "";

    // التعامل مع السحب والإفلات
    dropZone.addEventListener('dragover', (e) => { e.preventDefault(); dropZone.classList.add('dragover'); });
    dropZone.addEventListener('dragleave', () => { dropZone.classList.remove('dragover'); });
    dropZone.addEventListener('drop', (e) => {
        e.preventDefault(); dropZone.classList.remove('dragover');
        if (e.dataTransfer.files.length > 0) handleFile(e.dataTransfer.files[0]);
    });
    fileInput.addEventListener('change', (e) => { if (e.target.files.length > 0) handleFile(e.target.files[0]); });

    // دالة معالجة الملف
    async function handleFile(file) {
        currentFile = file;
        originalFileName = file.name.split('.')[0];
        resultsArea.style.display = 'block';
        downloadArea.classList.add('hidden');
        actionButtons.style.display = 'flex'; 
        cleanBtn.disabled = false;
        cleanBtn.innerText = "🧹 CLEAN & DOWNLOAD";
        thumbnailContainer.style.display = 'none';
        mapContainer.style.display = 'none';
        metadataList.innerHTML = '<div style="color:#22D3EE;">[ Analyzing File... ]</div>';

        if (file.type === 'application/pdf') {
            await analyzePDF(file);
        } else {
            await analyzeImage(file);
        }
    }

    // تحليل الصور
    async function analyzeImage(file) {
        try {
            const output = await exifr.parse(file, { gps: true, tiff: true, exif: true });
            
            if (!output || Object.keys(output).length === 0) {
                metadataList.innerHTML = '<div style="color:#10B981;">✅ No sensitive EXIF metadata found.</div>';
                return;
            }

            let thumbnailUrl = await exifr.thumbnailUrl(file);
            if (thumbnailUrl) {
                thumbnailImage.src = thumbnailUrl;
                thumbnailContainer.style.display = 'block';
            }

            let htmlContent = '';
            let hasGps = false;
            for (let key in output) {
                if (['Make', 'Model', 'Software', 'DateTimeOriginal', 'Artist'].includes(key) || key.startsWith('GPS')) {
                    let val = output[key];
                    if (key.startsWith('GPS') && typeof val === 'object') {
                         val = JSON.stringify(val);
                         hasGps = true;
                    }
                    htmlContent += `<div class="data-item"><span class="key">${key}:</span> ${val}</div>`;
                }
            }
            metadataList.innerHTML = htmlContent || '<div style="color:#10B981;">No major threats found.</div>';

            if (hasGps && output.latitude && output.longitude) {
                mapIframe.src = `https://maps.google.com/maps?q=${output.latitude},${output.longitude}&z=15&output=embed`;
                mapContainer.style.display = 'block';
            }

        } catch (error) {
            metadataList.innerHTML = `<div style="color:#EF4444;">Error analyzing image: ${error.message}</div>`;
        }
    }

    // تحليل PDF
    async function analyzePDF(file) {
        try {
            const arrayBuffer = await file.arrayBuffer();
            const pdfDoc = await PDFLib.PDFDocument.load(arrayBuffer);
            
            const author = pdfDoc.getAuthor();
            const creator = pdfDoc.getCreator();
            const producer = pdfDoc.getProducer();

            let htmlContent = '';
            if (author) htmlContent += `<div class="data-item"><span class="key">Author:</span> ${author}</div>`;
            if (creator) htmlContent += `<div class="data-item"><span class="key">Creator:</span> ${creator}</div>`;
            if (producer) htmlContent += `<div class="data-item"><span class="key">Producer:</span> ${producer}</div>`;

            metadataList.innerHTML = htmlContent || '<div style="color:#10B981;">No major metadata found.</div>';
        } catch (error) {
            metadataList.innerHTML = `<div style="color:#EF4444;">Error analyzing PDF: ${error.message}</div>`;
        }
    }

    // تنظيف الملف
    cleanBtn.addEventListener('click', async () => {
        if (!currentFile) return;
        cleanBtn.innerText = "Processing...";
        cleanBtn.disabled = true;

        if (currentFile.type === 'application/pdf') {
            await cleanPDF(currentFile);
        } else {
            await cleanImage(currentFile);
        }
    });

    // تنظيف الصور
    async function cleanImage(file) {
        const isHeic = file.name.toLowerCase().endsWith('.heic') || file.name.toLowerCase().endsWith('.heif');
        
        if (isHeic) {
            try {
                const convertedBlob = await heic2any({
                    blob: file,
                    toType: "image/jpeg",
                    quality: 0.9
                });
                file = new File([convertedBlob], originalFileName + ".jpg", { type: "image/jpeg" });
            } catch (error) {
                alert("⚠️ Error converting HEIC image. Please try another file.");
                cleanBtn.innerText = "🧹 CLEAN & DOWNLOAD";
                cleanBtn.disabled = false;
                return;
            }
        }

        const reader = new FileReader();
        reader.onload = function(e) {
            const img = new Image();
            
            img.onload = function() {
                const canvas = document.createElement('canvas');
                canvas.width = img.width;
                canvas.height = img.height;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, 0, 0);
                
                const cleanDataUrl = canvas.toDataURL('image/jpeg', 0.95);
                
                downloadBtn.onclick = function() {
                    const link = document.createElement('a');
                    link.download = originalFileName + '_cleaned.jpg';
                    link.href = cleanDataUrl;
                    link.click();
                };

                actionButtons.style.display = 'none'; 
                downloadArea.classList.remove('hidden');
                metadataList.innerHTML = '<div style="color:#10B981;">✅ All EXIF metadata has been permanently stripped.</div>';
                thumbnailContainer.style.display = 'none';
                mapContainer.style.display = 'none';
            };

            img.onerror = function() {
                alert("⚠️ This image format is not supported. Please try a JPG or PNG file.");
                cleanBtn.innerText = "🧹 CLEAN & DOWNLOAD";
                cleanBtn.disabled = false;
            };
            
            img.src = e.target.result;
        };
        reader.readAsDataURL(file);
    }

    // تنظيف PDF
    async function cleanPDF(file) {
        try {
            const arrayBuffer = await file.arrayBuffer();
            const pdfDoc = await PDFLib.PDFDocument.load(arrayBuffer);
            
            pdfDoc.setAuthor('');
            pdfDoc.setCreator('');
            pdfDoc.setProducer('');
            pdfDoc.setTitle('');

            const pdfBytes = await pdfDoc.save();
            const blob = new Blob([pdfBytes], { type: 'application/pdf' });
            const url = URL.createObjectURL(blob);

            downloadBtn.onclick = function() {
                const link = document.createElement('a');
                link.download = originalFileName + '_cleaned.pdf';
                link.href = url;
                link.click();
            };

            actionButtons.style.display = 'none'; 
            downloadArea.classList.remove('hidden');
            metadataList.innerHTML = '<div style="color:#10B981;">✅ All PDF metadata has been permanently stripped.</div>';
        } catch (error) {
            alert('Error cleaning PDF: ' + error.message);
            cleanBtn.innerText = "🧹 CLEAN & DOWNLOAD";
            cleanBtn.disabled = false;
        }
    }

    // دالة الرجوع للصفحة الرئيسية (Reset)
    resetBtn.addEventListener('click', () => {
        currentFile = null;
        fileInput.value = ""; 
        resultsArea.style.display = 'none'; 
        downloadArea.classList.add('hidden'); 
        thumbnailContainer.style.display = 'none';
        mapContainer.style.display = 'none';
        metadataList.innerHTML = ""; 
        actionButtons.style.display = 'flex'; 
        cleanBtn.innerText = "🧹 CLEAN & DOWNLOAD";
        cleanBtn.disabled = false;
    });

    // دالة التخلص من الملف بدون تنظيف
    discardBtn.addEventListener('click', () => {
        resetBtn.click(); 
    });
</script>
</body>
</html>
"""
    # عرض الكود
    components.html(html_code, height=850, scrolling=True)
