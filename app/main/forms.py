from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, RadioField, SelectField
from wtforms.validators import Required, Email, EqualTo
from ..models import *


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')


class PitchForm(FlaskForm):
    category_id = SelectField('Select Category', choices=[('interviewpitch', 'Interview'), ('pickuppitch', 'Pick Up Lines'), ('promotionpitch', 'Promotion'),('schoolpitch','School')])
    content = TextAreaField('YOUR PITCH')
    submit = SubmitField('Create Pitch')

# class CommentForm(FlaskForm):
#     description = TextAreaField('Add comment', validators=[Required()])
#     submit = SubmitField()
