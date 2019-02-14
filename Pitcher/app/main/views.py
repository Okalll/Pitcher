from flask import render_template
from .forms import PitchForm
from ..models import Pitch
from . import main

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to To The Pitch Clinic'
    return render_template('index.html', title = title)

@main.route('/pitch/new', methods = ['GET','POST'])
def new_pitch():
    form = pitchForm()

    if form.validate_on_submit():
        title = form.title.data
        pitch = form.pitch.data
        new_pitch = pitch(title,pitch)
        new_pitch.save_pitch()
        return redirect(url_for('pitch.html'))

    title = f'{movie.title} pitch'
    return render_template('pitch.html',title = title, pitch_form=form)

@main.route('/pitch')
def pitch(title):

    '''
    View movie page function that returns the pitch details page and its data
    '''
    title = f'{pitch.title}'
    pitches = Pitch.get_pitches(pitch.title)

    return render_template('index.html',title = title,pitches = pitches)
