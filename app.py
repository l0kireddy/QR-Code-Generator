from flask import Flask, request, send_file
from flask_cors import CORS
import qrcode
import io

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "QR Backend Running ✅"

@app.route("/api/generate", methods=["POST"])
def generate_qr():
    data = request.get_json() or {}
    text = data.get("text", "").strip()

    if not text:
        return {"error": "Text/URL required"}, 400

    img = qrcode.make(text)

    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    return send_file(img_bytes, mimetype="image/png")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
