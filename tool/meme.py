# v7 路西法智庫梗圖產生器 - 保持核心架構，僅更名與優化預設詞
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

# 全域暫存使用者選擇的底圖物件
CURRENT_BASE_IMAGE = None

def hex_to_rgb(hex_color):
    """將網頁十六進位顏色 (#RRGGBB) 轉換為 RGB 元組"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

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
    """安全轉換為整數"""
    if value is None:
        return default
    try:
        return int(round(float(value)))
    except (ValueError, TypeError):
        return default

def generate_preview_base64(text, font_size, rotation, pos_x, pos_y, color_hex):
    """根據參數生成圖片 base64"""
    base_image = get_current_image()
        
    px = safe_int(pos_x, base_image.width // 2)
    py = safe_int(pos_y, base_image.height // 2)
    f_size = safe_int(font_size, 80)
    rot = safe_int(rotation, 0)
    rgb_color = hex_to_rgb(color_hex or "#ffffff")

    try:
        # 嘗試加載微軟正黑體，若失敗則使用預設字體
        font = ImageFont.truetype("C:\\Windows\\Fonts\\msjh.ttc", f_size)
    except Exception:
        font = ImageFont.load_default()
        
    safe_text = str(text or "").replace("\\n", "\n")
    
    # 計算文字尺寸
    temp_img = Image.new("RGBA", (1, 1))
    temp_draw = ImageDraw.Draw(temp_img)
    bbox = temp_draw.multiline_textbbox((0, 0), safe_text, font=font, align="center")
    text_w = max(1, bbox[2] - bbox[0])
    text_h = max(1, bbox[3] - bbox[1])
    
    # 建立文字圖層 (增加緩衝空間避免旋轉裁切)
    pad = int(max(text_w, text_h) * 0.6) + 150
    text_layer_size = (text_w + pad, text_h + pad)
    text_layer = Image.new("RGBA", text_layer_size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(text_layer)
    
    draw.multiline_text(
        (text_layer_size[0] // 2, text_layer_size[1] // 2),
        safe_text,
        font=font,
        fill=rgb_color + (255,), # 加入 Alpha 通道
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
    <title>路西法智庫梗圖產生器 v7</title>
    <meta charset="utf-8">
    <style>
        body { font-family: 'Segoe UI', "微軟正黑體", sans-serif; background: #1a1a1a; color: #fff; margin: 0; padding: 20px; display: flex; }
        .control-panel { width: 360px; background: #2d2d2d; padding: 20px; border-radius: 12px; box-shadow: 0 8px 20px rgba(0,0,0,0.5); flex-shrink: 0; }
        .preview-panel { flex-grow: 1; margin-left: 20px; display: flex; justify-content: center; align-items: center; background: #111; border-radius: 12px; border: 2px solid #333; padding: 10px; min-height: 500px; position: relative; overflow: auto; }
        
        h2 { margin-top: 0; margin-bottom: 2px; color: #64ffda; }
        .version-tag { color: #888; font-size: 13px; margin-bottom: 15px; padding-bottom: 10px; border-bottom: 1px solid #444; font-weight: bold; }
        
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 8px; font-weight: bold; font-size: 14px; color: #bbb; }
        
        .upload-box { background: #3d3d3d; border: 2px dashed #555; padding: 15px; border-radius: 8px; margin-bottom: 20px; text-align: center; }
        .upload-box input { margin-top: 5px; width: 100%; color: #fff; cursor: pointer; }
        
        input[type="text"] { width: 93%; padding: 10px; background: #3d3d3d; border: 1px solid #555; color: #fff; border-radius: 6px; }
        input[type="range"] { width: 100%; margin-top: 8px; cursor: pointer; }
        input[type="color"] { width: 100%; height: 40px; border: none; border-radius: 6px; cursor: pointer; background: #3d3d3d; padding: 5px; }
        
        .val-display { float: right; color: #64ffda; font-family: monospace; }
        
        button { width: 100%; padding: 14px; border: none; font-size: 16px; font-weight: bold; border-radius: 6px; cursor: pointer; margin-top: 10px; transition: 0.3s; }
        .btn-save { background: #64ffda; color: #000; }
        .btn-save:hover { background: #52d1b2; transform: translateY(-2px); }
        .btn-save:disabled { background: #555; cursor: not-allowed; }
        
        .btn-reset { background: #ff5252; color: white; font-size: 14px; padding: 8px; margin-top: 5px; width: 100%; }
        .btn-reset:hover { background: #e53935; }
        
        .img-container { position: relative; cursor: crosshair; }
        img { max-width: 100%; max-height: 85vh; box-shadow: 0 4px 25px rgba(0,0,0,0.8); display: block; user-select: none; }
    </style>
</head>
<body>

<div class="control-panel">
    <h2>路西法智庫梗圖產生器</h2>
    <div class="version-tag">版本號：v7 旗艦梗圖版</div>
    
    <div class="upload-box">
        <label style="color: #64ffda;">🖼️ 自選梗圖底圖 (不限尺寸):</label>
        <input type="file" id="imageUploader" accept="image/*">
    </div>
    
    <div class="form-group">
        <label>梗圖文字內容:</label>
        <input type="text" id="textInput" value="路西法智庫 v7">
        <small style="color:#666;">(換行請輸入 \\n)</small>
    </div>

    <div class="form-group">
        <label>文字顏色:</label>
        <input type="color" id="colorInput" value="#ffffff">
    </div>
    
    <div class="form-group">
        <label>字體大小: <span class="val-display" id="sizeVal">80 px</span></label>
        <input type="range" id="sizeInput" min="10" max="500" value="80">
    </div>
    
    <div class="form-group">
        <label>旋轉角度: <span class="val-display" id="rotVal">0 度</span></label>
        <input type="range" id="rotInput" min="-180" max="180" value="0">
    </div>
    
    <div class="form-group">
        <label>水平位置 (X): <span class="val-display" id="xVal">0 px</span></label>
        <input type="range" id="xInput" min="0" max="{{ img_w }}" value="{{ default_x }}">
    </div>
    
    <div class="form-group">
        <label>垂直位置 (Y): <span class="val-display" id="yVal">0 px</span></label>
        <input type="range" id="yInput" min="0" max="{{ img_h }}" value="{{ default_y }}">
    </div>
    
    <button type="button" class="btn-reset" id="resetBtn">↩ 重設位置與角度</button>
    
    <p style="font-size:12px; color:#777; margin-top:15px; border-top: 1px solid #444; padding-top: 10px;">
        💡 密技：直接<b>點擊右側預覽圖</b>可快速定位文字位置！
    </p>
    
    <button class="btn-save" id="saveBtn">儲存高品質梗圖檔 (output.jpg)</button>
</div>

<div class="preview-panel">
    <div class="img-container" id="imgContainer">
        <img id="previewImg" src="" alt="預覽圖載入中...">
    </div>
</div>

<script>
    const textInput = document.getElementById('textInput');
    const colorInput = document.getElementById('colorInput');
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
                color: colorInput.value,
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
        });
    }

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
                }
            });
        };
        reader.readAsDataURL(file);
    });

    imgContainer.addEventListener('click', function(e) {
        const rect = previewImg.getBoundingClientRect();
        const realX = Math.round(((e.clientX - rect.left) / rect.width) * nativeW);
        const realY = Math.round(((e.clientY - rect.top) / rect.height) * nativeH);
        xInput.value = realX;
        yInput.value = realY;
        updatePreview();
    });

    resetBtn.addEventListener('click', function() {
        rotInput.value = 0;
        xInput.value = Math.round(nativeW / 2);
        yInput.value = Math.round(nativeH / 2);
        updatePreview();
    });

    [textInput, colorInput, sizeInput, rotInput, xInput, yInput].forEach(el => {
        el.addEventListener('input', updatePreview);
    });

    saveBtn.addEventListener('click', () => {
        saveBtn.disabled = true;
        saveBtn.innerText = "儲存中...";
        fetch('/save', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                text: textInput.value || "",
                color: colorInput.value,
                size: parseInt(sizeInput.value) || 80,
                rotation: parseFloat(rotInput.value) || 0,
                x: parseInt(xInput.value) || Math.round(nativeW/2),
                y: parseInt(yInput.value) || Math.round(nativeH/2)
            })
        })
        .then(res => res.json())
        .then(data => {
            alert("成功！高品質梗圖已儲存至：\\n" + data.path);
            saveBtn.disabled = false;
            saveBtn.innerText = "儲存高品質梗圖檔 (output.jpg)";
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
    return render_template_string(HTML_TEMPLATE, img_w=base_image.width, img_h=base_image.height, default_x=base_image.width // 2, default_y=base_image.height // 2)

@app.route('/upload_bg', methods=['POST'])
def upload_bg():
    global CURRENT_BASE_IMAGE
    try:
        data = request.json or {}
        img_data = base64.b64decode(data.get('image', ''))
        CURRENT_BASE_IMAGE = Image.open(BytesIO(img_data)).convert("RGBA")
        return jsonify({'success': True, 'width': CURRENT_BASE_IMAGE.width, 'height': CURRENT_BASE_IMAGE.height})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/update', methods=['POST'])
def update():
    data = request.json or {}
    img_b64 = generate_preview_base64(data.get('text', ''), data.get('size', 80), data.get('rotation', 0), data.get('x'), data.get('y'), data.get('color'))
    return jsonify({'image': img_b64})

@app.route('/save', methods=['POST'])
def save():
    data = request.json or {}
    base_image = get_current_image()
    rgb_color = hex_to_rgb(data.get('color', '#ffffff'))
    f_size = safe_int(data.get('size'), 80)
    
    try:
        font = ImageFont.truetype("C:\\Windows\\Fonts\\msjh.ttc", f_size)
    except Exception:
        font = ImageFont.load_default()
        
    text = str(data.get('text', '')).replace("\\n", "\n")
    temp_draw = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    bbox = temp_draw.multiline_textbbox((0, 0), text, font=font, align="center")
    
    pad = int(max(bbox[2]-bbox[0], bbox[3]-bbox[1]) * 0.6) + 150
    text_layer = Image.new("RGBA", (bbox[2]-bbox[0]+pad, bbox[3]-bbox[1]+pad), (0,0,0,0))
    ImageDraw.Draw(text_layer).multiline_text((text_layer.width//2, text_layer.height//2), text, font=font, fill=rgb_color+(255,), align="center", anchor="mm")
    
    rotated = text_layer.rotate(safe_int(data.get('rotation'), 0), resample=Image.Resampling.BICUBIC, expand=True)
    final = Image.new("RGBA", base_image.size)
    final.paste(base_image, (0, 0))
    final.paste(rotated, (int(safe_int(data.get('x'),0)-rotated.width/2), int(safe_int(data.get('y'),0)-rotated.height/2)), mask=rotated)
    
    output_path = "output.jpg"
    final.convert("RGB").save(output_path, "JPEG", quality=95)
    return jsonify({'path': os.path.abspath(output_path)})

if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:5000/")
    app.run(host='127.0.0.1', port=5000, debug=False)