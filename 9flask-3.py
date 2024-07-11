import flask
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")

def hello_world(password=None):
    #html="""
    #<h1>Тестовый запуск программы</h1>
    #<p>Это просто текст</p>
    #"""
    #return html
    return render_template("index4.html")



if __name__ == "__main__":
    app.run()