from ..utils import db
from datetime import datetime

class Blogs(db.Model):
    __tablename__ = 'Blogs' #untuk ganti nama table
    id = db.Column(db.Integer(), primary_key=True)
    judul = db.Column(db.String(50), nullable=False, unique=True)
    post = db.Column(db.Text, nullable=False)
    datetime = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<blogs {self.judul}>'