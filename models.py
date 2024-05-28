"""Models for Adoption Agency"""
from flask_sqlalchemy import SQLAlchemy

DEFAULT_IMAGE = "https://i0.wp.com/www.maisonette.gr/wp-content/uploads/2018/01/pet-icon.png?ssl=1"

db = SQLAlchemy()



class Pet (db.Model):

    __tablename__ = 'pets'


    id = db.Column(db.Integer,
                   autoincrement = True,
                   primary_key = True)
    
    name = db.Column(db.Text,
                     nullable = False)
    
    species = db.Column(db.Text,
                        nullable = False)
    
    photo_url = db.Column(db.Text)

    age = db.Column(db.Integer)

    notes = db.Column(db.Text)

    available = db.Column(db.Boolean,
                          nullable = False,
                          default = True)
    
    def image_url(self):
        """Return pet image or default image"""

        return self.photo_url or DEFAULT_IMAGE


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

