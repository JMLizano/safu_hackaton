import datetime
from ..extensions import db


class Transaction(db.Model):
    __tablename__ = 'transactions'
    sender_id = db.Column(db.String(80), db.ForeignKey('address.id'), primary_key=True)
    receiver_id = db.Column(db.String(80), db.ForeignKey('address.id'), primary_key=True)
    extra_data = db.Column(db.String(80))

    def to_dict(self):
        data = {}
        data["sender_id"] = self.sender_id
        data["receiver_id"] = self.receiver_id
        data["extra"] = self.extra_data
        return data


class Address(db.Model):
    __tablename__ = 'address'
    id = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    score = db.Column(db.Float)
    in_trans = db.Column(db.Integer)
    out_trans = db.Column(db.Integer)
    compromised = db.Column(db.Boolean)
    sended_to = db.relationship('Address', 
        secondary='transactions',
        primaryjoin=('transactions.c.sender_id == Address.id'),
        secondaryjoin=('transactions.c.receiver_id == Address.id'),
        backref=db.backref('received_from', lazy='dynamic'), lazy='dynamic')

    def __repr__(self):
        return "<ID: {}>".format(self.id)

    def to_dict(self):
        data = {}
        data["id"] = self.id
        data["score"] = self.score
        data["in_trans"] = self.in_trans
        data["out_trans"] = self.out_trans
        data["compromised"] = self.compromised
        return data


class Report(db.Model):
    __tablename__ = 'report'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address_id = db.Column(db.String(80), db.ForeignKey('address.id'))
    reporter_id = db.Column(db.String(80), db.ForeignKey('address.id'))
    created_date = db.Column(db.DateTime)

    def to_dict(self):
        data = {}
        data["id"] = self.id
        data["address_id"] = self.address_id
        data["reporter_id"] = self.reporter_id
        return data
