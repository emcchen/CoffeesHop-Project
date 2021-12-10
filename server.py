"""Server for coffeesHop search project"""


from flask import Flask, request, render_template, redirect, session
import json
import jinja2
import os, model, crud
import requests

app = Flask(__name__)
api_key = os.environ['YELP_API_KEY']

# Required to use Flask sessions
app.secret_key = "SECRET"

# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.
app.jinja_env.undefined = jinja2.StrictUndefined



@app.route('/')
def loginpage():
    """Log users in"""
    return render_template('login.html')

@app.route('/register')
def register():
    """Register new users"""
    return render_template('register.html')

#@app.route('/register-user', methods=["POST"])
#def register_user():
#    email = request.form['email']
#    password= request.form['password']
#    user = get_user_by_email(email)
#    if user:
#        return 'A user already exists with that email.'
#    else:
#        create_user(email, password)

#        return redirect('login-form.html')

@app.route('/reviews')
def reviews():
    """Shows individual reviews page"""

    return render_template('reviews.html')



@app.route('/get-user', methods=["POST"])
def get_form():
    """Get user and pass from request.form"""
    email = request.form['email']
    password = request.form['password']
    session['user'] = email
    session['pass'] = password

    return redirect ('/home')

@app.route('/home')
def homepage():
    """Returns homepage"""
    return render_template('homepage.html')

@app.route('/shop')
def show_shop_form():
    """Show shops search form"""
    return render_template('search-form.html')


@app.route('/shop/search')
def find_shops():
    """Search for shops on YELP"""
    #components of requests
    api_key = os.environ['YELP_API_KEY']
    endpoint = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': 'bearer %s' % api_key}
    zipcode = request.args.get('zipcode')
    parameters = {'term': 'coffee',
                  'location': zipcode,
                  'radius': 10000,
                  'limit': 50,
                  'offset':50,
                  'sort_by': 'distance',
                  'categories': 'coffeeshops,coffee,coffeeroasteries, cafes',
                  'attributes': 'open_to_all,gender_neutral_restrooms'
                  }


    response = requests.get(url = endpoint, params= parameters, headers = headers)
    #convert JSON string to a Dictionary
    business_data = response.json()

    return render_template('search-results.html',
                            business_data=business_data)





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')