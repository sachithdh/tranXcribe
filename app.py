from flask import Flask, render_template, redirect, url_for, session, request
from main.main import transcribe

app = Flask(__name__)
app.secret_key = "key"

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/generate", methods=["POST", "GET"])
def generate():
    if request.method == "POST":
        audio_file = request.files["audio"]
        audio_file.save("new.mp3")

        audio = open("new.mp3", "rb")
        transcript = transcribe(audio)
        
        return render_template("index.html", text = transcript)
    
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()
