# CoffeesHop
CoffeesHop is a full-stack web application built to locate coffee shops and cafes that distinguish themselves as a safe and welcoming space to everyone, with gender neutral restrooms inside! Users can search for shops by entering in a location and view business names, along with customized markers on a map. An optional section to leave a review with an attached photo lets users leave their experience with the shop and also scroll through other reviews.

## Table of Contents
* [Tech Stack](#technologiesused)
* [Installation](#installation)
* [Features](#features)
* [Future](#future)

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

![alt-text](https://github.com/emcchen/CoffeesHop-Project/blob/main/static/img/gifs/zip_search.gif) 


**Search results** <br>
Can use the map location button to pan the maps to where you want.
~~~~~~~~~~~~~~~~~~

View shop results listed out
~~~~~~~~~~~~~~~~~~

View a particular shop's details, with an option to leave a review.
~~~~~~~~~~~~~~~~~~

Write your own review with a photo
~~~~~~~~~~~~~~~~~~

**Profiles** <br>
View your reviewed shops
~~~~~~~~~~~~~~~~~~

View other profiles
~~~~~~~~~~~~~~~~~~



## <a name="future"></a>Future