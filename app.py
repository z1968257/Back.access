from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import requests

load_dotenv()
app = Flask(__name__)
CORS(app)  # ✅ Enable CORS

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route('/send-message', methods=['POST'])
def send_message():
    data = request.get_json()
    message = data.get("message")

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    
    response = requests.post(url, json=payload)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)
