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

# class UpdatePost(FlaskForm):
#     post = TextAreaField('Tell us about you.',validators = [Required()])
#     submit = SubmitField('Submit')