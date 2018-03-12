from flask import Flask, flash, redirect, render_template, request, session, abort
from flask import request
from flask import render_template
import os
from users import *
from database import *
from sessions import *
import bcrypt
from flask import g
from postmarker.core import PostmarkClient
# engine = create_engine('sqlite:///tutorial.db', echo=True)
app = Flask(__name__)

@app.before_request
def before_request():
    g.db = sqlite3.connect("Untitled\\users\\Meenereem\\desktop\\database.db",  check_same_thread=False)

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    if not session.get('logged_in'):
        return redirect('/login')
    else:
        return render_template('index.html')
 
@app.route('/signup', methods=['GET', 'POST'])
def do_admin_signup():
    if request.method == 'GET':
        return render_template('signup.html')
    if is_email_already_taken(db, request.form['username']) == False:
        password = request.form['password']
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(10))
        create_user_account(db, request.form['username'], hashed)
        return redirect('/login')
    else:
        return render_template('signup.html', message = "username or password already exists")


@app.route('/email', methods=['POST'])
def send_result_email():
        postmark = PostmarkClient(server_token='7547cae9-c42f-4c62-8886-86f034db9fce')
        postmark.emails.send(
        From='fkuusisto@morgridge.org',
        To=request.form['email'],
        Subject='Message',
        HtmlBody=request.form['message'])

@app.route('/logout', methods=['POST'])
def logout():
        
        session['logged_in'] = False
        return home()

@app.route('/login', methods=['GET', 'POST'])
def do_admin_login():
    if request.method == 'GET':
        return render_template('login.html')
    password = request.form['password']
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(10))
    if is_email_already_taken(db, request.form['username']) == True:
        obj = get_one_by_email(db, request.form['username'])
        if bcrypt.checkpw(password.encode('utf-8'), obj.password) == True:
            create_session_token(db, request.form['username'])
            # if session['token'] == obj2.token:
            return render_template('index.html', email = obj.email)
    return home()
 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)