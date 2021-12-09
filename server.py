from flask import Flask, request, render_template, redirect, session
import json
from pprint import pformat
import jinja2
import os
import requests

app = Flask(__name__)

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
#def new_user_form():


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
    parameters = {'term': 'coffee & tea',
                  'location': zipcode,
                  'radius': 10000,
                  'limit': 50,
                  'offset':50,
                  'attribute': 'open_to_all, gender_neutral_restrooms'}


    response = requests.get(url = endpoint, params= parameters, headers = headers)
    #convert JSON string to a Dictionary
    business_data = response.json()

    return render_template('search-results.html',
                            business_data=business_data)



    

















#API_KEY = os.environ['YELP_API_KEY']
#ENDPOINT = 'https://api.yelp.com/v3/categories/coffee'
#HEADERS = {'Authorization': 'bearer %s' % API_KEY}

#make request to the API
#response = requests.get(url = ENDPOINT, headers = HEADERS)

#convert JSON string into dictionary
#business_data = response.json()

#loop through response to get each category.
#for item in business_data['category']:
#    print(item['title'])


#print(json.dumps(business_data, indent=3))








if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')