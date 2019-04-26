from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

    
class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    pass_secure = db.Column(db.String(255))

    posts = db.relationship('Post', backref = 'user', lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

   
class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))

    users = db.relationship('User', backref = 'role', lazy = "dynamic")
    

    def __repr__(self):
        return f'User {self.name}'


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    post = db.Column(db.String())
    posted = db.Column(db.DateTime,default=datetime.utcnow)

    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))



    def save_post(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_posts(cls):
        Post.all_posts.clear()

    @classmethod
    def get_posts(cls,title):
        posts = Post.query.filter_by(title = title).all()
        return posts

    @classmethod
    def get_post(cls,id):
        post = Post.query.filter_by(id=id).first()

        return post  