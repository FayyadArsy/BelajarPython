from ..utils import db

class Pengunjung(db.Model):
    __tablename__ = 'pengunjung'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    peminjaman = db.Column(db.String(50), nullable=False)
    tanggal = db.Column(db.Datetime(), nullable=False)

    # def __init__(self,datetime_now):
    #     self.datetime = datetime_now
    def __repr__(self):
        return f'<users {self.username}>'