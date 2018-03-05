from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from flask import request
from flask import render_template
import os
from sqlalchemy.orm import sessionmaker
from users import *
from database import *
import bcrypt
from flask import g
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
 
@app.route('/signup', methods=['GET', 'POST'])
def do_admin_signup():
    if request.method == 'GET':
        return render_template('signup.html')
    if is_email_already_taken(db, request.form['username']) == False:
        password = request.form['password']
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(10))
        create(db, request.form['username'], hashed)
        return render_template('login.html')
    else:
        return render_template('signup.html', message = "username or password already exists")

@app.route('/login', methods=['POST'])
def do_admin_login():
    password = request.form['password']
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(10))
    if is_email_already_taken(db, request.form['username']) == True:
        obj = get_one_by_email(db, request.form['username'])
        if bcrypt.checkpw(password.encode('utf-8'), obj.password) == True: 
            session['username'] = request.form['username']
            session['password'] = request.form['password']
            return render_template('index.html', email = obj.email)
    return render_template('login.html')

 
@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()
 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)