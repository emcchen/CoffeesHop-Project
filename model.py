"""Models for shops"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<User user_id={self.user_id} username={self.username}>'

class Review(db.Model):
    """Shop reviews"""

    __tablename__ = 'reviews'

    review_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    shop_id = db.Column(db.Integer, db.ForeignKey('shops.shop_id'), nullable=True)
    yelp_id = db.Column(db.String(50), nullable=False)
    review = db.Column(db.String(5000), nullable=True)
    img_url = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f'<Review={self.review}>'

#reviews attribute in User and Shop objects that'll return list of Review.
    user = db.relationship('User', backref='reviews')
    shop = db.relationship('Shop', backref='reviews')

class Shop(db.Model):
    """Shop information"""

    __tablename__ = 'shops'

    shop_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    yelp_id = db.Column(db.String(50), nullable=False)
    shop_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Shop Name={self.shop_name}, {self.address}, {self.zip_code}, {self.phone}>'

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