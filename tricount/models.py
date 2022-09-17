from tricount import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpeg')
    password = db.Column(db.String(60), nullable=False)
    groups = db.relationship('Group', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Group(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(100), nullable=False)
        description = db.Column(db.String(250), nullable=False)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
        bills = db.relationship('Bill', backref='group', lazy=True)
        def __repr__(self):
            return f"Group('{self.title}')"

class Bill(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        description = db.Column(db.String(100), nullable=False)
        amount = db.Column(db.Integer, nullable=False)
        group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
        
        def __repr__(self):
            return f"Bill('{self.description}', {self.amount})"
