# 💬 Joi - Offline Voice AI Companion

Joi is an offline voice AI companion that allows you to interact with an AI through both voice and text. She uses Ollama for intelligent responses and your system's text-to-speech for voice output, all running locally for privacy and offline capability.

## ✨ Features

- **Voice Interaction**: Speak to Joi and she'll respond with voice
- **Text Chat**: Type messages for instant responses
- **Offline Operation**: No internet required after initial setup
- **Multiple AI Models**: Automatically selects the best available Ollama model
- **Beautiful UI**: Modern glassmorphism design with background video
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 🛠️ Prerequisites

- **Python 3.7+**
- **Ollama** installed and running locally
- **Modern web browser** with Web Speech API support (Chrome recommended)
- **Node.js** (optional, for development)

## 📦 Installation

1. **Clone or download this repository**

2. **Install Python dependencies:**
   ```bash
   pip install flask pyttsx3
   ```

3. **Install and setup Ollama:**
   - Download Ollama from [ollama.ai](https://ollama.ai)
   - Install at least one model:
     ```bash
     ollama pull llama3.2
     # Or other preferred models like qwen3:8b, deepseek-r1:8b, gemma3:4b
     ```

4. **Ensure joi.mp4 video file is in the same directory as index.html**

## 🚀 Usage

1. **Start the voice server:**
   ```bash
   python voice_server.py
   ```
   This starts the text-to-speech server on port 5005.

2. **Start the main server (if needed):**
   ```bash
   python server.py
   ```
   Check what this server does - it might be for additional functionality.

3. **Open index.html in your browser:**
   - Double-click the file or serve it via a local server
   - For better experience, use a local server:
     ```bash
     python -m http.server 8000
     ```
     Then visit `http://localhost:8000`

4. **Interact with Joi:**
   - Click "🎙️ Start Listening" to speak
   - Or type in the text input and press Enter or click "📤 Send Text"
   - Joi will respond both in text and voice

## 🔧 Configuration

### Voice Settings
Run `check_voices.py` to see available voices on your system:
```bash
python check_voices.py
```

### Ollama Models
The app automatically prioritizes models in this order:
1. qwen3:8b
2. deepseek-r1:8b
3. llama3.2
4. gemma3:4b
5. gemma3:1b

Add more models to Ollama as needed.

## 🏗️ How It Works

- **Frontend (index.html)**: Web interface with speech recognition and text input
- **Voice Server (voice_server.py)**: Flask server handling text-to-speech using pyttsx3
- **Ollama Integration**: Local AI model for generating responses
- **Web Speech API**: Browser-based speech recognition

## 📁 Project Structure

```
├── index.html          # Main web interface
├── voice_server.py     # Text-to-speech server
├── server.py           # Additional server (check functionality)
├── check_voices.py     # Voice checking utility
├── joi.mp4            # Background video
└── README.md          # This file
```

## 🐛 Troubleshooting

- **Voice not working**: Ensure voice_server.py is running and accessible
- **Ollama connection failed**: Check if Ollama is running (`ollama serve`)
- **Speech recognition not working**: Use Chrome browser and allow microphone permissions
- **Video not playing**: Ensure joi.mp4 is in the correct location

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests!

## 📄 License

This project is open source. Feel free to use and modify as needed.

---

Made with ❤️ for offline AI companions
