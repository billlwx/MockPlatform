#! /usr/bin/env python
# _*_ coding: utf-8 _*_
# __author__ = 'bill'
# create on 2019/1/18

from flask import Flask, flash, redirect, render_template, \
     request, url_for

# app = Flask(__name__)
app = Flask(__name__, template_folder='../templates',static_folder="../static/css",static_url_path="")
app.secret_key = 'some_secret'

@app.route('/')
def index():
    return render_template('flashindex.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

if __name__ == "__main__":
    # app.run()
    app.run(debug=True)