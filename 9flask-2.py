from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/<name>/")
def hello_world(name="незнакомец"):
    return f"Привет, {name}"

if __name__ == "__main__"
    app.run()