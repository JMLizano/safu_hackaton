from ..extensions import db


# TODO: Make this an association object, and add amount column
transaction = db.Table('transactions',
    db.Column('sender_id', db.String(80), db.ForeignKey('address.id'), primary_key=True),
    db.Column('receiver_id', db.String(80), db.ForeignKey('address.id'), primary_key=True)
)

class Address(db.Model):
    __tablename__ = 'address'
    id = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    compromised = db.Column(db.Boolean)
    sended_to = db.relationship('Address', 
        secondary=transaction,
        primaryjoin=(transaction.c.sender_id == id),
        secondaryjoin=(transaction.c.receiver_id == id),
        backref=db.backref('received_from', lazy='dynamic'), lazy='dynamic')

    def __repr__(self):
        return "<ID: {}>".format(self.title)