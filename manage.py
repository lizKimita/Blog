from app import create_app, db
from app.models import User

def make_shell_context():
    return dict(app = app,db = db,User = User, Role = Role )

if __name__ == '__main__':
    manager.run()