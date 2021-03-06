# CoffeesHop
CoffeesHop is a full-stack web application built to locate and display nondiscriminatory coffee shops and cafes with gender neutral restrooms inside! Users can search for shops by entering in a location and view business names, along with customized markers on a map. An optional section to leave a review with an attached photo lets users leave their experience with the shop and also scroll through other reviews.

## Table of Contents
* [Tech Stack](#technologiesused)
* [Installation](#installation)
* [Features](#features)
* [Future Implementations](#future)

## <a name="technologiesused"></a>Tech Stack

* Python
* Flask
* Jinja
* Javascript
* HTML
* CSS
* SQLAlchemy
* PostgreSQL
* Bootstrap

## <a name="installation"></a>Installation

To run CoffeesHop:

Sign up and get API keys for:
* [Yelp](https://www.yelp.com/developers/documentation/v3/business_search)
* [Google Maps Javascript](https://developers.google.com/maps/documentation/javascript/tutorial)
* [Geocoding](https://developers.google.com/maps/documentation/geocoding/overview)
* [Cloudinary](https://cloudinary.com/)

Create a file called <kbd>secrets.sh</kbd> and save your API keys in it:
```
export YELP_API_KEY="YOUR_API_KEY"
export CLOUDINARY_KEY="YOUR_API_KEY"
export CLOUDINARY_SECRET="YOUR_API_SECRET"
```

Clone the CoffeesHop repository:
```
https://github.com/emcchen/CoffeesHop-Project.git
```

Create and activate a virtual environment in the directory:
```
$ virtualenv env
$ source env/bin/activate
```

Install dependencies:
```
$ pip3 install -r requirements.txt
```

Create database:
```
$ createdb stores
```

Run `seed_database.py` to create the database:
```
$ python3 seed_database.py
```

Source your keys from `secrets.sh` into environment:
```
source secrets.sh
```

Run the app:
```
python3 server.py
```

Open [http://localhost:5000](http://localhost:5000) in your browser.


## <a name="features"></a>Features
**Login/Registration** <br>
Users need to create an account if they haven't already.

Search for a shop by zipcode.

![alt-text](https://github.com/emcchen/CoffeesHop-Project/blob/main/static/img/gifs/zip.gif) 


**Search results** <br>
Can use the map location button to pan the maps to where you want.

![alt-text](https://github.com/emcchen/CoffeesHop-Project/blob/main/static/img/gifs/geocode.gif)

View shop results listed out.

![alt-text](https://github.com/emcchen/CoffeesHop-Project/blob/main/static/img/gifs/shop_list.gif)

View a particular shop's details, with an option to leave a review.

![alt-text](https://github.com/emcchen/CoffeesHop-Project/blob/main/static/img/gifs/particular_shop.gif)

Write your own review with a photo

![alt-text](https://github.com/emcchen/CoffeesHop-Project/blob/main/static/img/gifs/review.gif)

**Profiles** <br>
View your reviewed shops

![alt-text](https://github.com/emcchen/CoffeesHop-Project/blob/main/static/img/gifs/profile.gif)

View other profiles

![alt-text](https://github.com/emcchen/CoffeesHop-Project/blob/main/static/img/gifs/user_profiles.gif)


## <a name="future"></a>Future Implementations

* Add 5-star rating feature
* Allow users to friend other users
* Have an activity feed of friend's activities
* Give a radius option in search options
