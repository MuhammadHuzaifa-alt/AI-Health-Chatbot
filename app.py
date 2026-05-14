from flask import Flask, render_template, request, jsonify
from groq import Groq

from config import DANGEROUS_KEYWORDS, GROQ_API_KEY, MODEL_NAME, TEMPERATURE, MAX_TOKENS

app = Flask(__name__)
client = Groq(api_key=GROQ_API_KEY)

# Safety filter
def is_safe_query(query):
    for word in DANGEROUS_KEYWORDS:
        if word in query.lower():
            return False
    return True

# Chat function
def get_response(user_query):
    system_prompt = """
    You are a friendly medical assistant.
    - Give general health advice only
    - Do NOT diagnose
    - Do NOT prescribe medication
    - Suggest consulting a doctor when needed
    - Keep answers simple
    """

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query}
        ],
        temperature=0.5,
        max_tokens=200
    )

    return response.choices[0].message.content

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json(silent=True) or {}
        user_input = data.get("message", "")

        if not user_input:
            return jsonify({"reply": "No message provided."}), 400

        if not is_safe_query(user_input):
            return jsonify({"reply": "Please consult a doctor for this query."})

        bot_reply = get_response(user_input)
        return jsonify({"reply": bot_reply})

    except Exception as e:
        return jsonify({"reply": f"Server error: {type(e).__name__}: {e}"}), 500

if __name__ == "__main__":
    app.run(debug=True)