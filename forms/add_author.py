from flask_wtf import FlaskForm
from wtforms import SelectField, StringField,  SubmitField
from wtforms.validators import DataRequired
from app.models import Author, AgeCategory


class AddAuthorForm(FlaskForm):
    name = StringField('Author Name', validators=[DataRequired()])
    submit = SubmitField('Add Author')