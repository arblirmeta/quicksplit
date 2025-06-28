from flask import Flask, render_template
from database import init_database

app = Flask(__name__)

# Datenbank beim Start initialisieren
init_database()

@app.route("/")
def index():
    return render_template("index.html")

# 404 Error Handler für unsere schöne 404-Seite
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)