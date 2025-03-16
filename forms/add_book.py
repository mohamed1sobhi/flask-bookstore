from flask_wtf import FlaskForm
from wtforms import SelectField, StringField,  SubmitField
from wtforms.validators import DataRequired
from app.models import Author, AgeCategory


class AddBookForm(FlaskForm):
    name = StringField('Book Name', validators=[DataRequired()])
    publish_date = StringField('Publish Date', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    age_category = SelectField('Age Category', choices=[
        ('UNDER_8', 'Under 8'),
        ('AGE_8_15', '8-15'),
        ('ADULTS', 'Adults')
    ], validators=[DataRequired()])
    author = SelectField('Author', coerce=int, validators=[DataRequired()])
    image_url = StringField('Image URL')
    submit = SubmitField('Add Book')