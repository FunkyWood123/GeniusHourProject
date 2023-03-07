from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
import pyrebase
login_manager = LoginManager()

config = {'apiKey': "AIzaSyBOEC9f4jecnYZLVoyXM_KdqZTH22ttLmY",
  'authDomain': "genius-hour-63711.firebaseapp.com",
  'databaseURL' : "https://genius-hour-63711-default-rtdb.europe-west1.firebasedatabase.app",
  'projectId': "genius-hour-63711",
  'storageBucket': "genius-hour-63711.appspot.com",
  'messagingSenderId': "122155670178",
  'appId': "1:122155670178:web:176c93895c0a79d3f455fb",
  'measurementId': "G-6PJM9XVNL8"}

firebase = pyrebase.initialize_app(config)

# Define a Flask-Login user class
class User(UserMixin):
    def __init__(self, user_id, email, token):
        self.id = user_id
        self.email = email
        self.token = token

# Define a Flask-Login user loader function
@login_manager.user_loader
def load_user(user_id):
    return User(user_id, None, None)

# Define a login function that authenticates users with Firebase
def login(email, password):
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password(email, password)
    if user:
        user_id = user['localId']
        user_email = user['email']
        user_token = user['idToken']
        user = User(user_id, user_email, user_token)
        login_user(user)
        return True
    else:
        return False

# Define a logout function that logs out users with Flask-Login and Firebase
def logout():
    logout_user()