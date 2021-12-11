""" Seed the database """
#https://fellowship.hackbrightacademy.com/materials/serft9/exercises/ratings-v2/index-2.html

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

