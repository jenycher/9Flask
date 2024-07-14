from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def films():
    context = {
        "link": "Перейти в кинотеатр"
    }
    return render_template("ind1.html", **context)

@app.route("/person/")
def person():
    context = {
        "link": "Перейти в кинотеатр"
    }
    return render_template("ind2.html", **context)

if __name__ == "__main__":
    app.run()