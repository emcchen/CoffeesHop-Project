"""CRUD operations - Create, Read, Update, Delete :) """

from model import db, User, Likes, Shops, connect_to_db


def create_user(username, lname, email, password):
    """Create and return a new user"""
    new_user= User(username=username,
                   email=email,
                   password=password)

    db.session.add(new_user)
    db.session.commit()

    return new_user

def create_favorite(user, shop):
    """Create and return favorite shop"""
    fav = Likes(user=user, shop=shop)

    db.session.add(fav)
    db.session.commit()

    return fav


def create_shop(shop_name, address, zip_code, phone):
    """Create shop info database"""
    shop_info= Shops(shop_name=shop_name, address=address, zip_code=zip_code, phone=phone)
    db.session.add(shop_info)
    db.session.commit()

    return shop_info

#def check_db_for_email():
    """"Checks if email is in database"""









if __name__ == '__main__':
    from server import app
    connect_to_db(app)