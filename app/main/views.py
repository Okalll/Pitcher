from flask import render_template, redirect, url_for, abort, request
from flask_login import login_required
from ..models import User, Pickuplines, Promotion, School, Interview, Pitch
from .forms import UpdateProfile, PitchForm
from .. import db
from . import main


@main.route('/')
def index():
    '''
    View root page function that returns the home page and its data
    '''
    return render_template('index.html')


@main.route('/user/<name>')
def profile(name):
    user = User.query.filter_by(username=name).first()

    if user is None:
        abort(404)

    return render_template("Profile/profile.html", user=user)


@main.route('/user/<name>/update', methods=['GET', 'POST'])
@login_required
def update_profile(name):
    user = User.query.filter_by(username=name).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', name=user.username))

    return render_template('Profile/update.html', form=form)


@main.route('/user/<name>/update/pic', methods=['POST'])
@login_required
def update_pic(name):
    user = User.query.filter_by(username=name).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', name=name))


@main.route('/pitch/new/', methods=['GET', 'POST'])
@login_required
def new_pitch():
    '''
    Function that creates new pitches
    '''
    form = PitchForm()

    if category is None:
        abort(404)

    if form.validate_on_submit():
        pitch = form.content.data
        category_id = form.category_id.data
        new_pitch = Pitch(pitch=pitch, category_id=category_id)

        new_pitch.save_pitch()
        return redirect(url_for('main.index'))

    return render_template('new_pitch.html', new_pitch_form=form, category=category)


@main.route('/pickuplines', methods=['GET', 'POST'])
def pickuplines():
    # pitch = Pitch.query.filter_by.first()
    pickuppitch = Pitch.query.filter_by(category="pickuppitch")

    return render_template('pickuplines.html')


@main.route('/school/pitches/', methods=['GET', 'POST'])
def school():
    pitches = Pitch.get_pitches('school')

    return render_template('school.html', pitches=pitches)


@main.route('/interview/pitches/', methods=['GET', 'POST'])
def interview():
    pitches = Pitch.get_pitches('interview')

    return render_template('interview.html', pitches=pitches)


@main.route('/promotion/pitches/', methods=['GET', 'POST'])
def promotion():
    pitches = Pitch.get_pitches('promotion')

    return render_template('promotion.html', pitches=pitches)
