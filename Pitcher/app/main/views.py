from flask import render_template,redirect,url_for,abort,request
from . import main
from flask_login import login_required
from ..models import User,Pickuplines,Promotion,Product,Interview,Pitch
from .forms import UpdateProfile
from .. import db,photos

# Views
@main.route('/')
def home():

    '''
    View root page function that returns the home page and its data
    '''
    return render_template('home.html')

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("Profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('Profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/pickuplines', methods=['GET', 'POST'])
def pickuplines():
    pitch = Pitch.query.filter_by().first()
    pickuppitch = Pitch.query.filter_by(category="pickuppitch")
    return render_template('pickuplines.html', pitch=pitch, pickuppitch=pickuppitch)

@main.route('/product', methods=['GET', 'POST'])
def product():
    pitch = Pitch.query.filter_by().first()
    productpitch= Pitch.query.filter_by(category="productpitch")

    return render_template('product.html', productpitch=productpitch, pitch=pitch)

@main.route('/interview', methods=['GET', 'POST'])
def interview():
    pitch = Pitch.query.filter_by().first()
    interviewpitch = Pitch.query.filter_by(category="interviewpitch")

    return render_template('interview.html', pitch=pitch, interviewpitch=interviewpitch)

@main.route('/promotion', methods=['GET', 'POST'])
def promotion():
    pitch = Pitch.query.filter_by().first()
    promotionpitch = Pitch.query.filter_by(category="promotionpitch")

    return render_template('promotion.html', pitch=pitch, promotionpitch=promotionpitch)
