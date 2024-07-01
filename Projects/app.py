from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, Rashid is learning Flask Framework yooo!"


if __name__ == "__main__":
    app.run(debug=True)
