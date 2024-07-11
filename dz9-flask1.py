from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def show_time():
    current_time = datetime.now()
    time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
    return f"Текущие дата и время: {time_string}"

if __name__ == "__main__":
     app.run(debug=True)