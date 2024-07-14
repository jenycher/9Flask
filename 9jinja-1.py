from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")

def films():
    context = {
        "poem": [
            "Сижу за решёткой в темнице сырой.",
            "Вскормленный в неволе орёл молодой,",
            "Мой грустный товарищ, махая крылом,",
            "Кровавую пищу клюёт под окном,",
            "Клюёт, и бросает, и смотрит в окно,",
            "Как будто со мною задумал одно."]
    }
    return render_template("shablon.html", **context)

if __name__ == "__main__":
    app.run()