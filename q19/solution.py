from flask import Flask, send_file
from PIL import Image
from io import BytesIO
import os

app = Flask(__name__)

@app.route("/")
def generate_image():
    img = Image.new("RGB", (300, 100), "white")

    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return send_file(buffer, mimetype="image/png")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
