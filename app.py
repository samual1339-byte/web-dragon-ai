from flask import Flask, request, jsonify, render_template
from twilio.twiml.messaging_response import MessagingResponse
from agent import dragon_agent

app = Flask(__name__)

# =========================
# 1️⃣ WHATSAPP ROUTE
# =========================
@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get("Body", "").strip()
    user_number = request.values.get("From", "user")

    reply = dragon_agent(incoming_msg, user_number)

    resp = MessagingResponse()
    resp.message(reply)
    return str(resp)

# =========================
# 2️⃣ BROWSER HOME PAGE
# =========================
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# =========================
# 3️⃣ BROWSER CHAT API
# =========================
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}

    module = data.get("module", "")
    service = data.get("service", "")
    query = data.get("query", "")

    user_input = f"{module} {service} {query}".strip()

    reply = dragon_agent(user_input, "browser_user")

    return jsonify({
        "status": "success",
        "reply": reply
    }), 200

# =========================
# 4️⃣ RUN SERVER (LAST)
# =========================
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

