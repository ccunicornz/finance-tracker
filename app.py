from flask import Flask 

app = Flask(__name__)

@app.get("/")
def home():
    return"Hello from Flask in windows" 

if __name__  == "__main__":
    app.run(debug=True)
