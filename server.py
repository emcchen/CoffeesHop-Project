"""Server for coffeesHop search project"""

import os
from flask import Flask, request, render_template, redirect, session, flash, jsonify
from model import connect_to_db
from jinja2 import StrictUndefined
import json
import crud
import requests

app = Flask(__name__)
api_key = os.environ['YELP_API_KEY']
# Required to use Flask sessions
app.secret_key = "SECRET"

# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def loginpage():
    """First page that logs users in"""
    return render_template('login.html')
    

@app.route('/register')
def register():
    """Redirect to register new user page"""
    return render_template('register.html')
    

@app.route('/register-user', methods=['POST'])
def register_user():
    """Creates new user"""

    username = request.form.get('username')
    email = request.form.get('email')
    password= request.form.get('password')

    user = crud.get_user_by_username(username)

    if user:
        flash('The username or email has already been registered.')
        return redirect('/register')
    else:
        crud.create_user(username, email, password)
        flash("Account created, please log in")
        return redirect('/')


@app.route('/get-user', methods=["POST"])
def gets_user():
    """Logs users in"""

    username = request.form['username']
    password = request.form['password']

    #Grabs existing users from db
    user = crud.get_user_by_username(username)
    #Checks username and password with db
    if user and user.password == password:
        session['current_user'] = user.username
        flash(f'You\'re logged in, {user.username} :) ')
        return redirect('/home')
    else:
        flash('The email or password you entered was incorrect.')
        return redirect('/')

@app.route('/logout')
def logout():
    """Clears session and returns to homepage"""
    session.clear()
    return redirect('/')


@app.route('/new-shop', methods=["POST"])
def add_shop():
    """ Adds a store to the database """

    shop_name = request.json.get('name')
    address = request.json.get('address')
    zip_code = request.json.get('zip')
    phone = request.json.get('phone')
    yelp_id = request.json.get('id')
    review = request.json.get('review')
    logged_in_user = request.json.get('user')

    shop = crud.get_shop_by_yelp_id(yelp_id)
    user = crud.get_user_by_username(logged_in_user)


    if logged_in_user is None:
        return 'You must log in to leave a review!'
    elif not review:
        return 'You didn\'t leave a review..'
    # user is logged in and leaving review
    else:
        #if shop not in db, create shop and save in db, along with user's review
        #Display associated review in frontend
        if shop is None:
            shop = crud.create_shop(shop_name, address, zip_code, yelp_id, phone)
        crud.create_review(user, shop, yelp_id, review)
        return 'Review created'
        #if shop in db, save user's review in db and display associated reviews in frontend
        #save logged in user's review & display in frontend


@app.route('/home')
def home():
    """ Shows homepage"""
    return render_template('homepage.html')

@app.route('/shop')
def show_shop_form():
    """Show shops search form"""
    return render_template('search-form.html')

@app.route('/users')
def all_users():
    """View all users"""

    users = crud.get_users()
    return render_template('all_users.html', users=users)

@app.route('/users/<user_id>')
def show_user(user_id):
    """Show user details"""

    user = crud.get_user_by_id(user_id)
    user_reviews = user.reviews

    return render_template('user_details.html', user=user, reviews=user_reviews)

@app.route('/shop/search')
def find_shops():
    """Renders search result html page"""
    zipcode = request.args.get('zipcode')
    business_data= yelp_searches(zipcode)

    return render_template('search-results.html',
                            business_data=business_data, zipcode=zipcode)

def yelp_searches(zipcode):
    """Search for shops on YELP"""
    #components of requests
    endpoint = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': f'bearer {api_key}'}
    parameters = {'term': 'coffee',
                  'location': zipcode,
                  'radius': 10000,
                  'limit': 50,
                  'offset':1,
                  'sort_by': 'distance',
                  'categories': 'cafes, coffeeroasteries',
                  'attributes': 'open_to_all,gender_neutral_restrooms'
                  }


    response = requests.get(url = endpoint, params= parameters, headers = headers)
    #convert JSON string to a Dictionary
    business_data = response.json()

    return business_data

@app.route('/map')
def map_data():
    """Returns stores list for google maps using entered zipcode"""
    zipcode = request.args.get('zipcode')
    business_data= yelp_searches(zipcode)

    return jsonify(business_data)


@app.route('/review/<yelp_id>')
def reviews(yelp_id):
    """Search for shops on YELP by id"""
    #components of requests
    endpoint = f'https://api.yelp.com/v3/businesses/{yelp_id}'
    headers = {'Authorization': f'bearer {api_key}'}


    response = requests.get(url = endpoint, headers = headers)
    #convert JSON string to a Dictionary
    business_info = response.json()

    shop_reviews = crud.get_reviews_by_yelp_id(yelp_id)

    return render_template('shop_details.html',
                           business_info=business_info,
                           yelp_id=yelp_id,
                           shop_reviews=shop_reviews,
                           reviews=reviews)



#Connect to database before app.run or Flask won't be able to access db
if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')