from flask import Flask, request, jsonify, send_from_directory
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("AIzaSyCbXRCNVfGHvfrVfXpaRKZ2nO7Vg6sRiTg")
)

model = genai.GenerativeModel("gemini-2.5-flash")

app = Flask(__name__, static_folder=".")

@app.route("/")
def home():
    return send_from_directory(".", "index.html")


@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json.get("message")

    try:

        response = model.generate_content(user_message)

        return jsonify({
            "reply": response.text
        })

    except Exception as e:

        return jsonify({
            "reply": str(e)
        })


if __name__ == "__main__":
    app.run(port=3000, debug=True)