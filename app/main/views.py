from flask import render_template, request, redirect,url_for,abort
from . import main
from ..models import Post, User
from .forms import PostForm, CommentsForm
from flask_login import login_required, current_user
from .. import db,photos
import markdown2 

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = "Learn cool things from others"
    return render_template('index.html', title = title)

@main.route('/post/')
def post():

    '''
    View post page function that returns the post details page and its data
    '''
    return render_template('post.html')

@main.route('/post/new', methods = ['GET','POST'])
def new_post():
    form = PostForm()
    new_post = None

    if form.validate_on_submit():
        post_title = form.post_title.data
        post = form.post.data

        new_post = Post(title = post_title, post = post)

        new_post.save_post()

        return redirect(url_for('.index'))

    title = 'New Post'
    return render_template('new_post.html', title = title, post_form = form, new_post = new_post)

