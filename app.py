from flask import Flask, render_template
from app.database import init_database
from app.routes import api


app = Flask(__name__)

init_database()

app.register_blueprint(api)
@app.route("/tasks")
def tasks_page():
    return render_template("tasks.html")


@app.route("/analytics")
def analytics_page():
    return render_template("analytics.html")

@app.route("/settings")
def settings_page():
    return render_template("settings.html")


@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)