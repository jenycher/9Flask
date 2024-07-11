import flask
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def filsms():
    return render_template("index-b.html")


@app.route("/person/")

def person():
    return render_template("index-p.html")

if __name__ == "__main__":
    app.run()