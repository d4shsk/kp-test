from flask import Flask, send_file
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route("/image")
def get_image():
    img = Image.new("RGB", (300, 100), "white")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return send_file(buffer, mimetype="image/png")

if __name__ == "__main__":
    app.run()
