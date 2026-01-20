from flask import Flask, render_template, request
import os
from utils.steganography import hide_char, extract_char
from utils.tts import speak_text

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
OUTPUT_FOLDER = "static/output"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    uploaded_image = None
    stego_image = None
    hidden_char = ""
    extracted_char = ""

    if request.method == "POST":
        image = request.files["image"]
        char = request.form.get("char")

        image_path = os.path.join(UPLOAD_FOLDER, image.filename)
        image.save(image_path)
        uploaded_image = image_path

        if "hide" in request.form:
            stego_path = os.path.join(OUTPUT_FOLDER, "stego.png")
            hide_char(image_path, char, stego_path)
            stego_image = stego_path
            hidden_char = char

        if "extract" in request.form:
            extracted_char = extract_char(image_path)
            speak_text(extracted_char)

    return render_template(
        "index.html",
        uploaded_image=uploaded_image,
        stego_image=stego_image,
        hidden_char=hidden_char,
        extracted_char=extracted_char
    )

if __name__ == "__main__":
    app.run(debug=True)
