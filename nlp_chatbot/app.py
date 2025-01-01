import subprocess
from flask import Flask, request, jsonify
from chat import get_response

app = Flask(__name__)

@app.get("/")
def index_get():
    subprocess.Popen(["streamlit", "run", "slchatbot.py"])
    return "Streamlit chatbot is running on http://localhost:8501. Please open this URL in your browser."

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
