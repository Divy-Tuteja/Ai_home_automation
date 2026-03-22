from flask import Flask, request, jsonify

app = Flask(__name__)

# store latest command
latest_command = "NONE"

@app.route("/")
def home():
    return "Server is running"

@app.route("/send", methods=["POST"])
def send_command():
    global latest_command
    data = request.json
    latest_command = data.get("command", "NONE")
    return jsonify({"status": "command received"})

@app.route("/get", methods=["GET"])
def get_command():
    global latest_command
    return jsonify({"command": latest_command})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)