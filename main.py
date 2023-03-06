#from flask import Flask, render_template
import pyrebase

config = {'apiKey': "AIzaSyBOEC9f4jecnYZLVoyXM_KdqZTH22ttLmY",
  'authDomain': "genius-hour-63711.firebaseapp.com",
  'databaseURL' : "https://genius-hour-63711-default-rtdb.europe-west1.firebasedatabase.app",
  'projectId': "genius-hour-63711",
  'storageBucket': "genius-hour-63711.appspot.com",
  'messagingSenderId': "122155670178",
  'appId': "1:122155670178:web:176c93895c0a79d3f455fb",
  'measurementId': "G-6PJM9XVNL8"}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

email = 'dummy@account.com'
password = '123456'
try:
    auth.sign_in_with_email_and_password(email, password)
    print("signed in!")
except:
    print('Invalid email or password')

'''
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
'''