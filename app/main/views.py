from flask import render_template, redirect, url_for, abort, request
from flask_login import login_required
from ..models import User, Pickuplines, Promotion, Product, Interview, Pitch
from .forms import UpdateProfile
from .. import db
from . import main
from .forms import PitchForm


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


@main.route('/pickuplines/pitches', methods=['GET', 'POST'])
def pickuplines():
    pitches = Pitch.get_pitches('pickuplines')

    return render_template('pickuplines.html', pitches=pitches)


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
