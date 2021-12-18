"""Models for liked/favorited shops"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    # reviews = a list of Review objects

    def __repr__(self):
        return f'<User user_id={self.user_id} username={self.username}>'


class Review(db.Model):
    """Review and liked shops."""

    __tablename__ = 'reviews'

    fav_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    yelp_id = db.Column(db.String(100), nullable=False)
    shop_id = db.Column(db.Integer, db.ForeignKey('shops.shop_id'), nullable=True)
    review = db.Column(db.String(500))

    def __repr__(self):
        return f'<shop_id={self.shop_id} the review={self.review}>'

#reviews attribute in User and Shop objects that'll return list of Review.
    user = db.relationship('User', backref='reviews')
    shop = db.relationship('Shop', backref='reviews')

class Shop(db.Model):
    """Shop information"""

    __tablename__ = 'shops'

    shop_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    shop_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    
    # reviews = a list of Review objects
    def __repr__(self):
        return f'<Shop shop_id={self.shop_id} shop_name={self.shop_name}>'


def connect_to_db(app, db_uri="postgresql:///stores", echo=True):
    """Connect to database"""

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_ECHO'] = echo
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = app
    db.init_app(app)

    print("Connected to the db!")



if __name__ == '__main__':
    from server import app
    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.
    connect_to_db(app)