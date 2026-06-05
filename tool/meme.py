# v4.3.3.4 顯示版號與原生選圖版
import os
import sys
import traceback
import webbrowser
from io import BytesIO
import base64
from PIL import Image, ImageDraw, ImageFont

try:
    from flask import Flask, render_template_string, request, jsonify
except ImportError:
    print("\n==================================================")
    print(" 🛑 缺少必要套件：Flask 🛑")
    print("==================================================")
    print("請先在您的命令提示字元 (CMD) 輸入以下指令安裝：")
    print("pip install flask")
    print("==================================================")
    input("\n按下 Enter 鍵以關閉此視窗...")
    sys.exit(1)

app = Flask(__name__)

# 全域暫存使用者選擇的底圖物件，預設嘗試載入 input.jpg
CURRENT_BASE_IMAGE = None

def get_current_image():
    """獲取當前使用的底圖，若無則建立預設畫布"""
    global CURRENT_BASE_IMAGE
    if CURRENT_BASE_IMAGE is not None:
        try:
            return CURRENT_BASE_IMAGE.copy()
        except Exception:
            pass
            
    input_path = "input.jpg"
    if os.path.exists(input_path):
        try:
            CURRENT_BASE_IMAGE = Image.open(input_path).convert("RGBA")
            return CURRENT_BASE_IMAGE.copy()
        except Exception:
            pass
            
    return Image.new("RGBA", (800, 600), (30, 30, 30, 255))

def safe_int(value, default):
    """防護核心：安全轉換為整數，絕不噴錯閃退"""
    if value is None:
        return default
    try:
        return int(round(float(value)))
    except (ValueError, TypeError):
        return default

def generate_preview_base64(text, font_size, rotation, pos_x, pos_y):
    """根據參數與當前底圖生成圖片 base64 碼"""
    base_image = get_current_image()
        
    px = safe_int(pos_x, base_image.width // 2)
    py = safe_int(pos_y, base_image.height // 2)
    f_size = safe_int(font_size, 80)
    rot = safe_int(rotation, 0)

    try:
        font = ImageFont.truetype("C:\\Windows\\Fonts\\msjh.ttc", f_size)
    except Exception:
        font = ImageFont.load_default()
        
    safe_text = str(text or "").replace("\\n", "\n")
    
    temp_img = Image.new("RGBA", (1, 1))
    temp_draw = ImageDraw.Draw(temp_img)
    bbox = temp_draw.multiline_textbbox((0, 0), safe_text, font=font, align="center")
    text_w = max(1, bbox[2] - bbox[0])
    text_h = max(1, bbox[3] - bbox[1])
    
    pad = int(max(text_w, text_h) * 0.6) + 150
    text_layer_size = (text_w + pad, text_h + pad)
    text_layer = Image.new("RGBA", text_layer_size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(text_layer)
    
    draw.multiline_text(
        (text_layer_size[0] // 2, text_layer_size[1] // 2),
        safe_text,
        font=font,
        fill=(255, 255, 255, 255),
        align="center",
        anchor="mm"
    )
    
    rotated_text = text_layer.rotate(rot, resample=Image.Resampling.BICUBIC, expand=True)
    
    final_image = Image.new("RGBA", base_image.size)
    final_image.paste(base_image, (0, 0))
    
    paste_x = int(px - (rotated_text.width / 2))
    paste_y = int(py - (rotated_text.height / 2))
    
    final_image.paste(rotated_text, (paste_x, paste_y), mask=rotated_text)
    
    buffered = BytesIO()
    final_image.convert("RGB").save(buffered, format="JPEG", quality=90)
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Inkscape 仿製網頁操控台 v4.3.3.4</title>
    <meta charset="utf-8">
    <style>
        body { font-family: 'Segoe UI', "微軟正黑體", sans-serif; background: #222; color: #fff; margin: 0; padding: 20px; display: flex; }
        .control-panel { width: 350px; background: #333; padding: 20px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.5); flex-shrink: 0; }
        .preview-panel { flex-grow: 1; margin-left: 20px; display: flex; justify-content: center; align-items: center; background: #111; border-radius: 8px; border: 2px dashed #444; padding: 10px; min-height: 500px; position: relative; }
        
        h2 { margin-top: 0; margin-bottom: 2px; color: #4CAF50; }
        .version-tag { color: #888; font-size: 13px; margin-bottom: 15px; padding-bottom: 10px; border-bottom: 2px solid #444; font-weight: bold; }
        
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; font-weight: bold; font-size: 14px; }
        
        /* 採用最標準、最乾淨、絕不消失的原始輸入框區塊 */
        .upload-box { background: #2a2a2a; border: 1px solid #444; padding: 12px; border-radius: 6px; margin-bottom: 20px; }
        .upload-box input { margin-top: 5px; width: 100%; color: #fff; }
        
        input[type="text"] { width: 93%; padding: 8px; background: #444; border: 1px solid #555; color: #fff; border-radius: 4px; }
        input[type="range"] { width: 100%; margin-top: 5px; }
        .val-display { float: right; color: #aaa; font-size: 12px; }
        button { width: 100%; padding: 12px; border: none; font-size: 16px; font-weight: bold; border-radius: 4px; cursor: pointer; margin-top: 10px; }
        .btn-save { background: #4CAF50; color: white; }
        .btn-save:hover { background: #45a049; }
        .btn-save:disabled { background: #555; cursor: not-allowed; }
        .btn-reset { background: #e05d44; color: white; font-size: 14px; padding: 8px; margin-top: 5px; margin-bottom: 15px; width: 100%; border-radius: 4px; cursor: pointer; font-weight: bold; }
        .btn-reset:hover { background: #c94f38; }
        .img-container { position: relative; cursor: crosshair; }
        img { max-width: 100%; max-height: 85vh; box-shadow: 0 4px 15px rgba(0,0,0,0.7); display: block; user-select: none; -webkit-user-drag: none; }
    </style>
</head>
<body>

<div class="control-panel">
    <h2>Inkscape 仿製工具</h2>
    <div class="version-tag">版本號：v4.3.3.4 安全穩定版</div>
    
    <div class="upload-box">
        <label style="color: #4CAF50;">🖼️ 點擊下方按鈕自選底圖:</label>
        <input type="file" id="imageUploader" accept="image/*">
    </div>
    
    <div class="form-group">
        <label>輸入文字内容:</label>
        <input type="text" id="textInput" value="貓貓abc">
        <small style="color:#888;">(提示: 換行請打 \\n)</small>
    </div>
    
    <div class="form-group">
        <label>字體大小: <span class="val-display" id="sizeVal">80 px</span></label>
        <input type="range" id="sizeInput" min="10" max="300" value="80">
    </div>
    
    <div class="form-group">
        <label>旋轉角度: <span class="val-display" id="rotVal">0 度</span></label>
        <input type="range" id="rotInput" min="-180" max="180" value="0">
    </div>
    
    <div class="form-group">
        <label>水平位置 (X 軸): <span class="val-display" id="xVal">0 px</span></label>
        <input type="range" id="xInput" min="0" max="{{ img_w }}" value="{{ default_x }}">
    </div>
    
    <div class="form-group">
        <label>垂直位置 (Y 軸): <span class="val-display" id="yVal">0 px</span></label>
        <input type="range" id="yInput" min="0" max="{{ img_h }}" value="{{ default_y }}">
    </div>
    
    <button type="button" class="btn-reset" id="resetBtn">↩ 重設定位與角度 (回正中央)</button>
    
    <p style="font-size:12px; color:#aaa; margin-top:5px;">💡 提示：除了拉桿，您也可以<b>直接點擊右側圖片</b>來改變文字位置！</p>
    
    <button class="btn-save" id="saveBtn">儲存高品質產出檔 (output.jpg)</button>
</div>

<div class="preview-panel">
    <div class="img-container" id="imgContainer">
        <img id="previewImg" src="" alt="即時預覽載入中...">
    </div>
</div>

<script>
    const textInput = document.getElementById('textInput');
    const sizeInput = document.getElementById('sizeInput');
    const rotInput = document.getElementById('rotInput');
    const xInput = document.getElementById('xInput');
    const yInput = document.getElementById('yInput');
    const previewImg = document.getElementById('previewImg');
    const imgContainer = document.getElementById('imgContainer');
    const saveBtn = document.getElementById('saveBtn');
    const resetBtn = document.getElementById('resetBtn');
    const imageUploader = document.getElementById('imageUploader');

    let nativeW = {{ img_w }};
    let nativeH = {{ img_h }};

    function updatePreview() {
        document.getElementById('sizeVal').innerText = sizeInput.value + " px";
        document.getElementById('rotVal').innerText = rotInput.value + " 度";
        document.getElementById('xVal').innerText = xInput.value + " px";
        document.getElementById('yVal').innerText = yInput.value + " px";

        fetch('/update', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                text: textInput.value || "",
                size: parseInt(sizeInput.value) || 80,
                rotation: parseFloat(rotInput.value) || 0,
                x: parseInt(xInput.value) || Math.round(nativeW/2),
                y: parseInt(yInput.value) || Math.round(nativeH/2)
            })
        })
        .then(res => res.json())
        .then(data => {
            if (data && data.image) {
                previewImg.src = "data:image/jpeg;base64," + data.image;
            }
        })
        .catch(err => console.log("連發請求已安全略過"));
    }

    // 處理上傳新底圖
    imageUploader.addEventListener('change', function(e) {
        const file = e.target.files[0];
        if (!file) return;
        
        const reader = new FileReader();
        reader.onload = function(evt) {
            const base64Data = evt.target.result.split(',')[1];
            
            fetch('/upload_bg', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ image: base64Data })
            })
            .then(res => res.json())
            .then(data => {
                if (data.success) {
                    nativeW = data.width;
                    nativeH = data.height;
                    
                    xInput.max = nativeW;
                    yInput.max = nativeH;
                    xInput.value = Math.round(nativeW / 2);
                    yInput.value = Math.round(nativeH / 2);
                    
                    updatePreview();
                } else {
                    alert("圖片解析失敗");
                }
            });
        };
        reader.readAsDataURL(file);
    });

    imgContainer.addEventListener('click', function(e) {
        const rect = previewImg.getBoundingClientRect();
        if (rect.width === 0 || rect.height === 0) return;
        
        const clickX = e.clientX - rect.left;
        const clickY = e.clientY - rect.top;
        
        const realX = Math.round((clickX / rect.width) * nativeW);
        const realY = Math.round((clickY / rect.height) * nativeH);
        
        xInput.value = Math.max(0, Math.min(nativeW, realX));
        yInput.value = Math.max(0, Math.min(nativeH, realY));
        updatePreview();
    });

    resetBtn.addEventListener('click', function() {
        rotInput.value = 0;
        xInput.value = Math.round(nativeW / 2);
        yInput.value = Math.round(nativeH / 2);
        updatePreview();
    });

    textInput.addEventListener('input', updatePreview);
    sizeInput.addEventListener('input', updatePreview);
    rotInput.addEventListener('input', updatePreview);
    xInput.addEventListener('input', updatePreview);
    yInput.addEventListener('input', updatePreview);

    saveBtn.addEventListener('click', () => {
        saveBtn.disabled = true;
        saveBtn.innerText = "正在儲存圖片中...";
        
        fetch('/save', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                text: textInput.value || "",
                size: parseInt(sizeInput.value) || 80,
                rotation: parseFloat(rotInput.value) || 0,
                x: parseInt(xInput.value) || Math.round(nativeW/2),
                y: parseInt(yInput.value) || Math.round(nativeH/2)
            })
        })
        .then(res => res.json())
        .then(data => {
            if(data.path) {
                alert("成功！高品質圖片已儲存至：\\n" + data.path);
            }
            saveBtn.disabled = false;
            saveBtn.innerText = "儲存高品質產出檔 (output.jpg)";
        })
        .catch(err => {
            alert("儲存失敗");
            saveBtn.disabled = false;
            saveBtn.innerText = "儲存高品質產出檔 (output.jpg)";
        });
    });

    updatePreview();
</script>

</body>
</html>
"""

@app.route('/')
def index():
    base_image = get_current_image()
    w, h = base_image.width, base_image.height
    return render_template_string(
        HTML_TEMPLATE, 
        img_w=w, 
        img_h=h, 
        default_x=w // 2, 
        default_y=h // 2
    )

@app.route('/upload_bg', methods=['POST'])
def upload_bg():
    global CURRENT_BASE_IMAGE
    try:
        data = request.json or {}
        img_data = base64.b64decode(data.get('image', ''))
        uploaded_img = Image.open(BytesIO(img_data)).convert("RGBA")
        CURRENT_BASE_IMAGE = uploaded_img
        return jsonify({
            'success': True,
            'width': uploaded_img.width,
            'height': uploaded_img.height
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/update', methods=['POST'])
def update():
    try:
        data = request.json or {}
        img_b64 = generate_preview_base64(
            data.get('text', ''), 
            data.get('size', 80), 
            data.get('rotation', 0), 
            data.get('x'), 
            data.get('y')
        )
        return jsonify({'image': img_b64})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/save', methods=['POST'])
def save():
    try:
        data = request.json or {}
        output_path = "output.jpg"
        base_image = get_current_image()
            
        px = safe_int(data.get('x'), base_image.width // 2)
        py = safe_int(data.get('y'), base_image.height // 2)
        f_size = safe_int(data.get('size'), 80)
        rot = safe_int(data.get('rotation'), 0)
        
        try:
            font = ImageFont.truetype("C:\\Windows\\Fonts\\msjh.ttc", f_size)
        except Exception:
            font = ImageFont.load_default()
            
        text = str(data.get('text', '')).replace("\\n", "\n")
        
        temp_img = Image.new("RGBA", (1, 1))
        temp_draw = ImageDraw.Draw(temp_img)
        bbox = temp_draw.multiline_textbbox((0, 0), text, font=font, align="center")
        text_w = max(1, bbox[2] - bbox[0])
        text_h = max(1, bbox[3] - bbox[1])
        
        pad = int(max(text_w, text_h) * 0.6) + 150
        text_layer_size = (text_w + pad, text_h + pad)
        text_layer = Image.new("RGBA", text_layer_size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(text_layer)
        
        draw.multiline_text(
            (text_layer_size[0] // 2, text_layer_size[1] // 2),
            text,
            font=font,
            fill=(255, 255, 255, 255),
            align="center",
            anchor="mm"
        )
        
        rotated_text = text_layer.rotate(rot, resample=Image.Resampling.BICUBIC, expand=True)
        
        final_image = Image.new("RGBA", base_image.size)
        final_image.paste(base_image, (0, 0))
        
        paste_x = int(px - (rotated_text.width / 2))
        paste_y = int(py - (rotated_text.height / 2))
        final_image.paste(rotated_text, (paste_x, paste_y), mask=rotated_text)
        
        final_image.convert("RGB").save(output_path, "JPEG", quality=95)
        return jsonify({'path': os.path.abspath(output_path)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    try:
        print("正在啟動本地網頁伺服器...")
        webbrowser.open("http://127.0.0.1:5000/")
        app.run(host='127.0.0.1', port=5000, debug=False)
    except Exception:
        print("\n❌ 網頁伺服器執行失敗：")
        traceback.print_exc()
        input("\n按下 Enter 鍵以關閉視窗...")