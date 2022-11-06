from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    return ""



if __name__ == "__main__":
    app.run(debug=True)
    
    
