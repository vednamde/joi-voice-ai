from flask import Flask, request, jsonify
from flask_cors import CORS
import pyttsx3
import time
import re

app = Flask(__name__)
CORS(app)  # ✅ Allow browser requests from port 8080

# Initialize pyttsx3
engine = pyttsx3.init()

time.sleep(0.5)
voices = engine.getProperty("voices")

# Force Zira female voice by name
zira_name = "Microsoft Zira Desktop - English (United States)"
zira_found = False
for voice in voices:
    if voice.name == zira_name:
        engine.setProperty("voice", voice.id)
        print(f"✅ Using Zira voice: {voice.id}")
        zira_found = True
        break
if not zira_found:
    print("⚠️ Zira not found, using default voice.")
    engine.setProperty("voice", voices[0].id if voices else None)

engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)

@app.route("/speak", methods=["POST"])
def speak():
    data = request.get_json()
    text = data.get("text", "")
    if not text.strip():
        return jsonify({"error": "No text provided"}), 400

    # Clean text for TTS
    text = re.sub(r'[^\w\s.,!?]', '', text)  # Remove emojis and special chars

    try:
        current_voice = engine.getProperty('voice')
        print(f"💬 Speaking: {text} with voice: {current_voice}")
        engine.say(text)
        engine.runAndWait()
        return jsonify({"status": "ok", "voice": current_voice})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print("🎙️ Joi Voice Server running on http://127.0.0.1:5005")
    app.run(port=5005)
