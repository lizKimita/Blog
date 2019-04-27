from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, DateField, SelectField
from wtforms.validators import Required

class PostForm(FlaskForm):
    post_title = StringField('Post title',validators=[Required()])
    post = TextAreaField('Post Content', validators=[Required()])
    submit = SubmitField('Submit')

class CommentsForm(FlaskForm):
    title = StringField('Post title',validators=[Required()])
    comment = TextAreaField('Comment',validators=[Required()])
    author = StringField('Your Name',validators = [Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')