"""Server for coffeesHop search project"""

import os
from flask import Flask, request, render_template, redirect, session, flash, jsonify
from model import connect_to_db
from jinja2 import StrictUndefined
import json
import crud
import requests
import cloudinary.uploader

app = Flask(__name__)
api_key = os.environ['YELP_API_KEY']
CLOUDINARY_KEY = os.environ['CLOUDINARY_KEY']
CLOUDINARY_SECRET = os.environ['CLOUDINARY_SECRET']
CLOUD_NAME = "emcchen"
app.secret_key = "SECRET"

app.jinja_env.undefined = StrictUndefined


@app.route('/')
def loginpage():
    """Login page"""
    return render_template('login.html')

@app.route('/register')
def register():
    """Registers new user"""
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
        flash('The email or password you entered was incorrect. Please try again. ')
        return redirect('/')

@app.route('/logout')
def logout():
    """Clears session and returns to login page"""
    session.clear()
    flash('Successfully logged out. See you next time!')
    return redirect('/')

@app.route('/new-shop', methods=["POST"])
def add_shop():
    """Adds a shop and review to the database"""

    shop_name = request.form.get('name')
    address = request.form.get('address')
    zip_code = request.form.get('zip')
    phone = request.form.get('phone')
    yelp_id = request.form.get('id')
    review = request.form.get('review')
    logged_in_user = request.form.get('user')
   
    #Variable for route to access uploaded file
    my_file = request.files['img']

    #Save uploaded file to Cloudinary by API request
    result = cloudinary.uploader.upload(my_file,
                                        api_key=CLOUDINARY_KEY,
                                        api_secret=CLOUDINARY_SECRET,
                                        cloud_name=CLOUD_NAME)
    #save generated url to database
    img_url = result['secure_url']

    shop = crud.get_shop_by_yelp_id(yelp_id)
    user = crud.get_user_by_username(logged_in_user)

    if logged_in_user is None:
        return 'You must log in to leave a review'
    elif not review:
        return 'No review..'
    # user is logged in and leaving review
    else:
        #if shop not in db, create shop and save in db, along with user's review
        #Display associated review in frontend
        if shop is None:
            shop = crud.create_shop(shop_name, address, zip_code, yelp_id, phone)
        crud.create_review(user, shop, yelp_id, review, img_url)
        return 'Review created'

@app.route('/home')
def home():
    """Shows homepage"""
    return render_template('homepage.html')

@app.route('/profile')
def user_reviewed():
    """Shows current user's profile"""

    username = session['current_user']
    user = crud.get_user_by_username(username)
    user_reviews = crud.get_reviews_by_user_id(user.user_id)

    return render_template('profile.html',
                            user_reviews=user_reviews,
                            user=user)

@app.route('/users')
def all_users():
    """Views all users"""

    users = crud.get_users()
    return render_template('all_users.html', users=users)

@app.route('/users/<user_id>')
def show_user(user_id):
    """Shows another user's profile"""

    user = crud.get_user_by_id(user_id)
    user_reviews = crud.get_reviews_by_user_id(user_id)

    return render_template('user_details.html',
                            user=user,
                            reviews=user_reviews)

@app.route('/shop/search')
def find_shops():
    """Shop results"""
    zipcode = request.args.get('zipcode')
    business_data= yelp_searches(zipcode)

    return render_template('search-results.html',
                            business_data=business_data,
                            zipcode=zipcode)

def yelp_searches(zipcode):
    """Search for shops on YELP"""
    #components of requests
    endpoint = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': f'bearer {api_key}'}
    parameters = {'term': 'coffee',
                  'location': zipcode,
                  'radius': 16000,
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
    """Returns shops list on google maps"""
    zipcode = request.args.get('zipcode')
    business_data= yelp_searches(zipcode)

    return jsonify(business_data)

@app.route('/review/<yelp_id>')
def reviews(yelp_id):
    """Search for shops on YELP by yelp id"""
    #components of requests
    endpoint = f'https://api.yelp.com/v3/businesses/{yelp_id}'
    headers = {'Authorization': f'bearer {api_key}'}


    response = requests.get(url = endpoint, headers = headers)
    #convert JSON string to a Dictionary
    business_info = response.json()

    shop_reviews = crud.get_reviews_by_yelp_id(yelp_id)
    shop_info = crud.get_reviews_combined_table(yelp_id)

    return render_template('shop_details.html',
                           business_info=business_info,
                           yelp_id=yelp_id,
                           shop_reviews=shop_reviews,
                           shop_info=shop_info)

#Connect to database before app.run or Flask won't be able to access db
if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')