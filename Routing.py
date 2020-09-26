from Imports import *
from App_Settings import *
from Routing import *
from Database import *
from Auth import *


# Payload.max_decode_packets = 50000

Messages = 'Please create an account or Signin to an existing account in order to proceed further!'

@app.route('/')
def index():
    """Render the app"""
    # form = LoginForms()
    # username = current_user.Username
    # print(username)
    # return render_template('Forms/Register.html')
    return redirect('register')

@app.route('/index2')
def index2():
    """Render the app"""
    # form = LoginForms()
    # username = current_user.Username
    # print(username)
    # users = BIO.query.all()
    # posts = Posts.query.all()
    return render_template('index.html')

@app.route('/Shop_Details')
def Shop_Details():
    """Render the app"""
    # form = LoginForms()
    # username = current_user.Username
    # print(username)
    # users = BIO.query.all()
    # posts = Posts.query.all()
    return render_template('Shop-Details.html')
