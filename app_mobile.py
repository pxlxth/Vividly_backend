from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "API funcionando"

@app.route("/validation/validate-face", methods=["POST"])
def validate_face():
    return jsonify({"success": True})

@app.route("/validation/generate-video", methods=["POST"])
def generate_video():
    return jsonify({
        "success": True,
        "video_url": "http://34.148.106.142:8000/video.mp4"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
