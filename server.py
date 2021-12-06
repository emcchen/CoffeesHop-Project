from flask import Flask, request, render_template, redirect, flash, session
import jinja2

app = Flask(__name__)

# Required to use Flask sessions
app.secret_key = "DEV"

# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.
app.jinja_env.undefined = jinja2.StrictUndefined


@app.route('/')
def loginpage():
    """Log users in"""
    return render_template('login.html')

@app.route('/get-user', methods=["POST"])
def get_my_form():
    #Get user and pass from request.form
    email = request.form['email']
    password = request.form['password']
    session['user'] = email
    session['pass'] = password

    return redirect ('/home')

@app.route('/home')
def homepage():
    """Returns homepage"""
    return render_template('homepage.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')