🏠 AI Home Automation System
A smart home automation system built using ESP32, Web Server, and Mobile App with Voice Control.
Control your home appliances from anywhere using an app or voice commands.

🚀 Features
📱 Mobile app control (MIT App Inventor)
🎤 Voice control (Speech Recognition)
🌐 Cloud-based control (works from anywhere)
⚡ Real-time device switching
🔌 Relay-based appliance control
🔄 Continuous command syncing with server


🧠 How It Works

User (App / Voice)
        ↓
   Web Server (Render)
        ↓
      ESP32
        ↓
      Relay
        ↓
   Appliance (Light)
App sends command → Server
ESP32 continuously checks server
ESP32 receives command → controls relay
🛠️ Tech Stack
ESP32 (Arduino / PlatformIO)
Python (Flask Server)
MIT App Inventor (Android App)
HTTP API Communication
Speech Recognition


📂 Project Structure

ai-home-automation/
│
├── ai-home-server/     # Flask backend
│   ├── app.py
│   └── requirements.txt
│
├── ai-home-esp32/      # ESP32 code
│   ├── src/main.cpp
│   └── platformio.ini
│
└── mobile-app/         # MIT App Inventor project


⚙️ Setup Instructions:

1️⃣ ESP32 Setup
Upload code using PlatformIO
Connect relay to GPIO 23
Update WiFi credentials in code
2️⃣ Server Setup
Deploy Flask server (Render)
Endpoints:
/send → receive commands
/get → ESP fetches command
3️⃣ Mobile App
Build using MIT App Inventor
Button / Voice sends:
{"command":"LIGHT_ON"}
🎤 Voice Commands
“Turn on light”
“Turn off light”
🔌 Hardware Used
ESP32
Relay Module (1 channel / 4 channel)
Power Supply
Light / Appliance


💡 Future Improvements

Google Assistant integration
Multiple device control
AI-based automation
Scheduling system
Mobile app UI improvements

🙌 Author
Divy Tuteja
