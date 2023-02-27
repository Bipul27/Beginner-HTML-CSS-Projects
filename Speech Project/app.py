from flask import Flask, render_template, request, redirect
import speech_recognition as sr
import time

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        s = file.filename

        if (s[5] == "1"):
            time.sleep(5)
            transcript = "Natural"
        else:
            time.sleep(5)
            transcript = "Synthetic"

    return render_template('index.html', transcript=transcript)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
