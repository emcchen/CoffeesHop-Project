""" Script to seed database """

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server


os.system('dropdb stores')
os.system('createdb stores')

model.connect_to_db(server.app)
model.db.create_all()

#Load shop data from JSON file
with open('data/shops.json') as f:
    shops_data = json.loads(f.read())

#Create shops, store them in list so we can
#use them to create fake reviews
shops_in_db=[]
for shop in shops_data:
    shop_name, address, zip_code, yelp_id, phone = (
      shop['shop_name'],
      shop['address'],
      shop['zip_code'],
      shop['yelp_id'],
      shop['phone']
    )

    db_shop = crud.create_shop(shop_name, address, zip_code, yelp_id, phone)
    shops_in_db.append(db_shop)

#Create 10 users.
#Each user will make 10 reviews
for n in range(10):
    username = f'username{n}'
    email = f'user{n}@testemail.com'
    password = 'test'

    user = crud.create_user(username, email, password)
    
    # for _ in range(2):
    #   random_shop = choice(shops_in_db)
    #   review = 'This is a review for a test'
    #   yelp_id = 'aKMxYmJxom1ZeYHpLgGy2g'
      
    #   crud.create_review(user, random_shop, yelp_id, review)