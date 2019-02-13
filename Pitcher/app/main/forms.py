from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField,RadioField, SelectField
from wtforms.validators import Required,Email,EqualTo
from ..models import User,Pitch,Comment

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    category = SelectField('Select category', choices=[('pickuppitch', 'Pick Up Lines'), ('techpitch', 'Technology'), ('businesspitch', 'Business'),('interviewpitch','Interview')])
    title = StringField('Title of your Pitch')
    description = TextAreaField('Type in your pitch')
    submit = SubmitField('Add Pitch')

class CommentForm(FlaskForm):
    description = TextAreaField('Add comment',validators=[Required()])
    submit = SubmitField()
