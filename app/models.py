from . import db
from sqlalchemy.sql import func
from enum import Enum
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(
        db.String(100),
        nullable=False,
        unique=True,
        index=True
    )
    password_hash = db.Column(db.String(100), nullable=False)

    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password) 

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def save_to_db(self):  # ✅ Ensure this method exists
        db.session.add(self)
        db.session.commit()


class AgeCategory(Enum):
    UNDER_8 = "under 8"
    AGE_8_15 = "8-15"
    ADULTS = "adults"

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    publish_date = db.Column(db.String(100), nullable=False)
    add_to_site_at = db.Column(db.DateTime, nullable=False, default=func.now())
    price = db.Column(db.Float, nullable=False)
    age_category = db.Column(db.Enum(AgeCategory), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    image_url = db.Column(db.String(100), nullable=True)



class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)


# -- Create the Book table
# CREATE TABLE book (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name VARCHAR(100) NOT NULL,
#     publish_date VARCHAR(100) NOT NULL,
#     add_to_site_at VARCHAR(100) NOT NULL,
#     price FLOAT NOT NULL,
#     age_category VARCHAR(20) NOT NULL,  -- Store Enum as string
#     author_id INTEGER NOT NULL,
#     FOREIGN KEY (author_id) REFERENCES author(id)
# );


# INSERT INTO book (name, publish_date, price, age_category, author_id)
# VALUES ('The Hobbit', '1937-09-21', 15.99, '8-15', 1);

# INSERT INTO book(name, publish_date, price, age_category, author_id)
# VALUES ('1984', '1949-06-08', 12.50, 'adults', 2);

# -- Books by J.K. Rowling (id: 1)
# INSERT INTO book (name, publish_date, price, age_category, author_id)
# VALUES ('Harry Potter and the Sorcerers Stone', '1997-06-26', 20.00, '8-15', 1);

# INSERT INTO book(name, publish_date, price, age_category, author_id)
# VALUES ('Harry Potter and the Chamber of Secrets', '1998-07-02', 22.50, '8-15', 1);

# -- Books by George Orwell (id: 2)
# INSERT INTO book(name, publish_date, price, age_category, author_id)
# VALUES ('1984', '1949-06-08', 12.50, 'adults', 2);

# INSERT INTO book (name, publish_date, price, age_category, author_id)
# VALUES ('Animal Farm', '1945-08-17', 10.00, 'adults', 2);

# -- Books by Jane Austen (id: 3)
# INSERT INTO book (name, publish_date, price, age_category, author_id)
# VALUES ('Pride and Prejudice', '1813-01-28', 18.75, 'adults', 3);

# INSERT INTO book(name, publish_date, price, age_category, author_id)
# VALUES ('Sense and Sensibility', '1811-10-30', 16.00, 'adults', 3);









