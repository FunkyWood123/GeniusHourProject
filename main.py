from flask import Flask, render_template, request, redirect, session, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from auth import login_manager, login, logout

config = {'apiKey': "AIzaSyBOEC9f4jecnYZLVoyXM_KdqZTH22ttLmY",
  'authDomain': "genius-hour-63711.firebaseapp.com",
  'databaseURL' : "https://genius-hour-63711-default-rtdb.europe-west1.firebasedatabase.app",
  'projectId': "genius-hour-63711",
  'storageBucket': "genius-hour-63711.appspot.com",
  'messagingSenderId': "122155670178",
  'appId': "1:122155670178:web:176c93895c0a79d3f455fb",
  'measurementId': "G-6PJM9XVNL8"}


app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key_here"
login_manager.init_app(app)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form.get('password')
        if login(email, password):
            print("yay")
        else:
            return render_template("index.html", error="Invalid email or password")
    return render_template('index.html', error="nothing to worry about!")

if __name__ == '__main__':
    app.run(debug=True)


@app.route("/safe")
@login_required
def safe():
    return "safe!"