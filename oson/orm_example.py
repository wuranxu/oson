from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from oson.pson import Pson
from datetime import datetime

app = Flask(__name__)
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    date = db.Column(db.DATETIME)

    def __init__(self, username, email, date):
        self.username = username
        self.email = email
        self.date = date

    def __repr__(self):
        return '<User %r>' % self.username


if __name__ == "__main__":
    u = User("wuranxu", "619434176@qq.com", datetime.now())
    result = Pson.dumps({"class": [u, {"cls": u}, u]})
    # old = Pson.loads(result)
    print(result)
