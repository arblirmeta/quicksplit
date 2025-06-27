from flask import Flask, render_template
from database import init_database

app = Flask(__name__)

# Datenbank beim Start initialisieren
init_database()

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)