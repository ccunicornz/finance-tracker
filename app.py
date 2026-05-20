from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from datetime import date


app = Flask(__name__)
app .config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(120), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, default=date.today)

with app.app_context():
    db.create_all()


@app.get("/")
def home():
    return"Hello from Flask in windows" 

if __name__  == "__main__":
    app.run(debug=True)
