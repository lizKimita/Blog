from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, DateField, SelectField
from wtforms.validators import Required

class PostForm(FlaskForm):
    post_title = StringField('Post title',validators=[Required()])
    post = TextAreaField('Post Content')
    submit = SubmitField('Submit')

class CommentsForm(FlaskForm):
    author = StringField('Your Name',validators = [Required()])
    comment = TextAreaField('Comment')
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class UpdatePost(FlaskForm):
    post_title = StringField('Post title',validators=[Required()])
    post = TextAreaField('Edit your post here',validators = [Required()])
    submit = SubmitField('Submit')

class EmailForm(FlaskForm):
    name = StringField('Name',validators=[Required()])
    email = StringField('Email Address',validators=[Required()])
    subscribe = SubmitField('Subscribe')