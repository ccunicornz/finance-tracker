from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from datetime import date


app = Flask(__name__)
app .config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()


@app.get("/")
def home():
    return"Hello from Flask in windows" 

if __name__  == "__main__":
    app.run(debug=True)
