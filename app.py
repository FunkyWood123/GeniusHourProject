from flask import Flask, render_template, request, redirect, session, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from auth import login_manager, login, logout, signup
import pyrebase
from flask_socketio import SocketIO, send


config = {'apiKey': "AIzaSyBOEC9f4jecnYZLVoyXM_KdqZTH22ttLmY",
  'authDomain': "genius-hour-63711.firebaseapp.com",
  'databaseURL' : "https://genius-hour-63711-default-rtdb.europe-west1.firebasedatabase.app",
  'projectId': "genius-hour-63711",
  'storageBucket': "genius-hour-63711.appspot.com",
  'messagingSenderId': "122155670178",
  'appId': "1:122155670178:web:176c93895c0a79d3f455fb",
  'measurementId': "G-6PJM9XVNL8"}

firebase = pyrebase.initialize_app(config)

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key_here"
login_manager.init_app(app)
socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.on('message')
def handleMessage(msg):
    print('Message ' + msg)
    send(msg, broadcast=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form.get('password')
        if login(email, password):
            return redirect("/chat")
        else:
            return render_template("index.html", error="Invalid email or password")
    return render_template('index.html', error="nothing to worry about!")


@app.route('/chat')
@login_required
def chat():
    db = firebase.database()
    return render_template('chat.html')
@app.route('/logout')
@login_required
def logoutuser():
    logout()
    return redirect('/')


@app.route('/signup', methods=["GET", "POST"])
def signuppage():
    auth = firebase.auth()
    if request.method == "POST":
        email = request.form["email"]
        password = request.form.get('password')
        try:
            auth.create_user_with_email_and_password(email, password)
            login(email, password)
            return redirect('/safe')
        except:
            return "your account sucks"
    return render_template('signup.html')


if __name__ == '__main__':
    socketio.run(app)
