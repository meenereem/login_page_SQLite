from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from flask import request
from flask import render_template
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
import sqlite3
import bcrypt
# engine = create_engine('sqlite:///tutorial.db', echo=True)
app = Flask(__name__)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
 
@app.route('/signup', methods=['GET', 'POST'])
def do_admin_signup():
    if request.method == 'GET':
        return render_template('signup.html')
    db = sqlite3.connect("Untitled\\users\\Meenereem\\desktop\\database.db")
    cursor = db.cursor()
    exist = False
    cursor.execute('SELECT * from users')
    if request.method == 'POST':
        print('we are posting')
        for row in cursor:
            password = request.form['password']
            hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(10))
            if request.form['username'] == row[1] and bcrypt.checkpw(password.encode('utf-8'), hashed):
                exist = True
        if exist == False:
            password = request.form['password']
            hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(10))
            cursor.execute('''INSERT INTO users(email, password)
            VALUES(?,?)''', (request.form['username'], hashed))
            print('user inserted')
            db.commit()
            return render_template('login.html')
        else:
            return render_template('signup.html', message = "username or password already exists")
            print('already exists')

@app.route('/login', methods=['POST'])
def do_admin_login():
    db = sqlite3.connect("Untitled\\users\\Meenereem\\desktop\\database.db")
    cursor = db.cursor()
    cursor.execute('SELECT * from users')
    if request.method == 'POST':
        password = request.form['password']
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(10))
        for row in cursor:
            if request.form['username'] == row[1] and bcrypt.checkpw(password.encode('utf-8'), hashed):
                session['username'] = request.form['username']
                session['password'] = request.form['password']
                return render_template('index.html', email = row[1])
    else:
        error = 'Invalid Credentials. Please try again.'
    return home()
 
@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()
 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)