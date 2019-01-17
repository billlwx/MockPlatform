import ConfigParser

from flask import Flask
from flask import redirect
from flask import request
from flask import session
from flask import url_for
from re import escape

app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

conf = ConfigParser.SafeConfigParser()
conf.read("../conf/apps.ini")
# set the secret key.  keep this really secret:
app.secret_key = conf.get("apps", "secretKey")

if __name__ == '__main__':
    app.run(debug=True)