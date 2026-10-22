import os
from flask import Flask, request, jsonify

app = Flask(__name__)

VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN", "my_secret_token")

@app.route("/", methods=["GET"])
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    
    if mode and token:
        if mode == "subscribe" and token == VERIFY_TOKEN:
            return challenge, 200
        else:
            return "Verification failed", 403
    return "Mahim UltraNet Bot is Running Live!", 200

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    if data and data.get("object") == "page":
        # Messenger event handling logic
        return "EVENT_RECEIVED", 200
    return "Not Found", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
  
