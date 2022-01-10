"""CRUD operations - Create, Read, Update, Delete :) """

from model import db, User, Review, Shop, connect_to_db


#################### USER ####################

def create_user(username, email, password):
    """Create and return a new user"""
    new_user= User(username=username,
                   email=email,
                   password=password)

    db.session.add(new_user)
    db.session.commit()

    return new_user

def get_users():
    """Returns all users"""

    return User.query.all()

def get_user_by_username(username):
    """Returns a user by their username"""
    return User.query.filter(User.username==username).first()

def get_user_by_id(user_id):
    """Returns a user by user id"""
    return User.query.filter(User.user_id==user_id).first()

#################### REVIEW ####################

def create_review(user, shop, yelp_id, review, img_url):
    """Create new review"""
    new_review = Review(user=user,
                        shop=shop,
                        yelp_id=yelp_id,
                        review=review,
                        img_url=img_url)

    db.session.add(new_review)
    db.session.commit()

    return new_review

def get_reviews_by_yelp_id(yelp_id):
    """ Returns all reviews by yelp_id """
    return Review.query.filter(Review.yelp_id == yelp_id).all()

def get_reviews_by_user_id(user_id):
    """ Returns reviews by a user's id"""
    return Review.query.filter(Review.user_id == user_id).options(db.joinedload('shop')).all()

def get_reviews_combined_table(yelp_id):
    """ Returns reviews by a yelp's id"""
    return Review.query.filter(Review.yelp_id == yelp_id).options(db.joinedload('user')).all()

############### SHOP ###############

def create_shop(shop_name, address, zip_code, yelp_id, phone):
    """Create shop info database"""
    shop_info= Shop(shop_name=shop_name,
                    address=address,
                    zip_code=zip_code,
                    yelp_id=yelp_id,
                    phone=phone)

    db.session.add(shop_info)
    db.session.commit()

    return shop_info

def get_shop_by_yelp_id(yelp_id):
    """ Check if there is a shop matching the yelp_id"""
    return Shop.query.filter(Shop.yelp_id == yelp_id).first()

def get_shop_by_id(shop_id):
    """Returns a shop by shop id"""
    return Shop.query.filter(Shop.shop_id==shop_id).first()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)