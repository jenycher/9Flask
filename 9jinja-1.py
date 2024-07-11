import flask
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")

def filsms():
    context={
        "caption": "Фильмы про Гарри",
        "user": "Нина",
        "num": 1
    }
    return render_template("shablon.html", **context)


@app.route("/shablon/")
def films2():
    context = {
        "caption": "Гарри Поттер",
        "link": "Перейти в кинотеатр"
    }
    return render_template("index-bb.html", **context)

@app.route("/person/")

def person():
    return render_template("index-p.html")



if __name__ == "__main__":
    app.run()