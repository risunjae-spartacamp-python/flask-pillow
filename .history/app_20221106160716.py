from flask import Flask
from flask import render_template
from flask import request

from PIL im

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["uploadFile"]
    return "Hello Upload"


if __name__ == "__main__":
    app.run(debug=True)
