from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from flask import request
from flask import render_template
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
import sqlite3
# engine = create_engine('sqlite:///tutorial.db', echo=True)
app = Flask(__name__)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
 

# @app.route('/signup', methods=['POST'])
# def do_admin_signup():
    #db = sqlite3.connect("Untitled\\users\\Meenereem\\desktop\\database.db")
#     cursor = db.cursor()
#     cursor.execute('SELECT * from users')
#     if request.method == 'POST':
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
            if request.form['username'] == row[1] and request.form['password'] == row[2]:
                exist = True
        if exist == False:
            cursor.execute('''INSERT INTO users(email, password)
            VALUES(?,?)''', (request.form['username'], request.form['password']))
            print('user inserted')
            # cursor.execute('''INSERT INTO users(email, password)
            # VALUES(?,?)''', [request.form['username'], request.form['password']])
            db.commit()
            return render_template('login.html')
        else:
            return render_template('signup.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
    # POST_USERNAME = str(request.form['username'])
    # POST_PASSWORD = str(request.form['password'])
    # Session = sessionmaker(bind=engine)
    # s = Session()
    # query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    # result = query.first()
    # print(result)
    db = sqlite3.connect("Untitled\\users\\Meenereem\\desktop\\database.db")
    cursor = db.cursor()
    cursor.execute('SELECT * from users')
    if request.method == 'POST':
        for row in cursor:
            print(row)
            if request.form['username'] == row[1] and request.form['password'] == row[2]:
                session['username'] = request.form['username']
                session['password'] = request.form['password']
                return render_template('index.html', email = row[1])
    else:
        error = 'Invalid Credentials. Please try again.'
    # if result:
    #     session['logged_in'] = True
    # else:
    #     flash('wrong password!')
    return home()
 
@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()
 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)