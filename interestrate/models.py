from . import db

class InterestRate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(100), nullable=False)
    interest_rate = db.Column(db.String(100), nullable=False)

