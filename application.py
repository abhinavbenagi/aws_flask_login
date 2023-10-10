import functools
from flask import Flask, render_template, session, redirect
from functools import wraps
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
application = Flask(__name__)
application.secret_key = b'\xcd\xbf(+=\t\xdc\xd9u\xfa\xd6Znh \xc5'

#Decoraters page

def login_required(f):
  @wraps(f)
  def wrap(*args , **kwargs):
    if 'logged_in' in session:
        return f(*args, **kwargs)
    else:
        return redirect('/')
  return wrap
      


from user.models import User

# Routes
# from user import routes

@application.route('/')
def home():
  return render_template('home.html')

@application.route('/dashboard/')
@login_required
def dashboard():
  return render_template('dashboard.html')


@application.route('/user/signup', methods=['POST'])
def signup():
  return User().signup()

@application.route('/user/signout')
def signout():
   return User().signout()

@application.route('/user/login', methods=['POST'])
def login():
   return User().login()

if __name__=="__main__":
    application.run(debug=True)