from flask import Flask, request, jsonify, render_template
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

app = Flask(__name__)

MODEL_NAME = "facebook/blenderbot-400M-distill"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"reply": "Please send a message."})

    inputs = tokenizer(user_message, return_tensors="pt")

    outputs = model.generate(
        **inputs,
        max_new_tokens=60,
        do_sample=True,
        temperature=0.7
    )

    reply = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
