from authWebPy import db, app
from authWebPy.models import User


with app.app_context():
    db.create_all()

