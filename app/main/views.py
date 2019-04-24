from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = "Learn cool things from others"
    return render_template('index.html', title = title)

@app.route('/post/')
def post():

    '''
    View post page function that returns the post details page and its data
    '''
    return render_template('post.html')