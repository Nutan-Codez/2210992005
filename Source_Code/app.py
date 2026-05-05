from flask import Flask, render_template, request
from model import predict

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    code = request.form["code"]
    label, features = predict(code)
    return render_template("result.html", label=label, features=features)

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)