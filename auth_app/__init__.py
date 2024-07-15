from flask import Flask

#создаёт экземпляр класса Flask (переменную dz_app)
app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key'
from app import routes