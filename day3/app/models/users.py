from ..utils import db

class Users(db.Model):
    __tablename__ = 'users' #untuk ganti nama table
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)

    blogs = db.relationship('Blogs', backref='user', lazy=True)

    def __repr__(self):
        return f'<users {self.username}>'