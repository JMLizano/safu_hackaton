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

# # TODO: Make this an association object, and add amount column
# transaction = db.Table('transactions',
#     db.Column('sender_id', db.String(80), db.ForeignKey('address.id'), primary_key=True),
#     db.Column('receiver_id', db.String(80), db.ForeignKey('address.id'), primary_key=True)
# )

class Address(db.Model):
    __tablename__ = 'address'
    id = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    compromised = db.Column(db.Boolean)
    # sended_to = db.relationship("Transaction", back_populates="receiver")
    # received_from = db.relationship("Transaction", back_populates="parsenderent")
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
        data["compromised"] = self.compromised
        return data