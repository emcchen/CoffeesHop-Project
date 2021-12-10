"""Models for liked/favorited shops"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(20), nullable=False)
    lname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<User user_id={self.user_id} fname={self.fname}>'


class Likes(db.Model):
    """Favorite shops."""

    __tablename__ = 'favorites'

    fav_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    shop_id = db.Column(db.Integer, db.ForeignKey('shops.shop_id'), nullable=False)

    def __repr__(self):
        return f'<Favorite fav_id={self.fav_id} shop={self.shop}'

    user = db.relationship('User', backref='favorites')
    shop = db.relationship('Shops', backref='favorites')

class Shops(db.Model):
    """Shop information"""

    __tablename__ = 'shops'

    shop_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    shop_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    
    def __repr__(self):
        return f'<Shop shop_id={self.shop_id} address={self.address}>'


def connect_to_db(flask_app, db_uri="postgresql:///favorites", echo=True):
    """Connect to database"""
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_ECHO'] = echo
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")



if __name__ == '__main__':
    from server import app
    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.
    connect_to_db(app)