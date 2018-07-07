from app import db


class Gift(db.Model):
    __tablename__ = "gifts"
    id = db.Column(db.Integer)
    nickname = db.Column(db.String(256))
    email = db.Column(db.String(256))
    role = db.Column(db.String(256))
