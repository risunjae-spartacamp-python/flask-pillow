from flask import Flask
from flask import render_templates

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Flask Pillow"

if __name__ == "__main__"
