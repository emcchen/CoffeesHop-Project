"""CRUD operations - Create, Read, Update, Delete :) """

from model import db, User, Review, Shop, connect_to_db


def create_user(username, email, password):
    """Create and return a new user"""
    new_user= User(username=username,
                   email=email,
                   password=password)

    db.session.add(new_user)
    db.session.commit()

    return new_user

def create_favorite(user, shop, review):
    """Create and return new favorite and review shop"""
    new_review_and_fav = Review(user=user, shop=shop, review=review)

    db.session.add(new_review_and_fav)
    db.session.commit()

    return new_review_and_fav


def create_shop(shop_name, address, zip_code, phone):
    """Create shop info database"""
    shop_info= Shop(shop_name=shop_name, address=address, zip_code=zip_code, phone=phone)
    db.session.add(shop_info)
    db.session.commit()

    return shop_info

def get_user_by_username(username):
    """Gets a user by their username"""
    return User.query.filter_by(User.username==username)













#def check_email_in_db(email):
#    """"Checks if email is in database"""

#    return User.query.filter

#def check_username_in_db(username):
#    """Checks if username is in database"""






if __name__ == '__main__':
    from server import app
    connect_to_db(app)