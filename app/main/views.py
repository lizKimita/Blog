from flask import render_template, request, redirect,url_for,abort
from . import main
from ..models import Post, User
from .forms import PostForm, CommentsForm, UpdateProfile
from flask_login import login_required, current_user
from .. import db, photos
import markdown2 

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    post_list = Post.query.order_by(Post.posted.desc()).all()

    title = "Learn cool things from others"
    return render_template('index.html', title = title, post_data = post_list)

@main.route('/latest_post')
def latestpost():

    '''
    view function that returns the latest single blog post
    '''

    post_latest = Post.query.order_by(Post.id.desc()).first()


    return render_template('latest.html',post_latest = post_latest)


@main.route('/post/<int:id>', methods = ['GET'])
def post(id):
    id=id
    my_post = Post.query.get(id)

    if id is None:
        abort(404)

    full_post = Post.query.filter_by(id=id).all()

    return render_template('post.html', post_data = my_post, id=id, full_post = full_post)

@main.route('/post/new', methods = ['GET','POST'])
@login_required
def new_post():
    form = PostForm()
    new_post = None

    if form.validate_on_submit():
        post_title = form.post_title.data
        post = form.post.data

        new_post = Post(title = post_title, post = post, user = current_user)

        new_post.save_post()

        return redirect(url_for('.index'))

    title = 'New Post'
    return render_template('new_post.html', title = title, post_form = form, new_post = new_post)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


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

    return render_template('profile/update.html',form =form)

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

