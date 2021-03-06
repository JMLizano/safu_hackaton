# -*- coding: utf-8 -*-
import json
import random
from flask import Blueprint, render_template, request
import sqlalchemy
from ..extensions import db
from ..models.models import Address

blueprint = Blueprint('public', __name__)


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload


@blueprint.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    return render_template('home.html', error=True, error_message=error.message), error.status_code


@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


@blueprint.route('/', methods=['GET', 'POST'])
def home():
    """Home page."""
    outgoing_transactions = []
    incoming_transactions = []
    address = None
    if request.method == 'POST':
        address_id = request.form.get('address', None)
        if address_id is None:
            raise InvalidUsage("You must provide an address", status_code=400)
        address = Address.query.filter_by(id=address_id).first()
        if address is not None:
            outgoing_transactions = address.sended_to
            incoming_transactions = address.received_from
    return render_template("home.html")

@blueprint.route('/api/address/<id>', methods=['GET'])
def get_address(id):
    """Home page."""
    outgoing_transactions = []
    incoming_transactions = []
    address = Address.query.filter_by(id=id).first()
    if address is not None:
        outgoing_transactions = address.sended_to
        incoming_transactions = address.received_from
    return json.dumps({ 'origin': address.to_dict(), 
                        'score': random.randint(0, 100),
                        'outgoing_transactions': [address.to_dict() for address in outgoing_transactions], 
                        'incoming_transactions': [address.to_dict() for address in incoming_transactions]
                      })


@blueprint.route('/submit', methods=['GET', 'POST'])
def outdated():
    """Outdated page."""
    if request.method == 'POST':
        address_id =request.form.get('address', None)
        if address_id is None:
            raise InvalidUsage("You must provide an address", status_code=400)
        address = Address(id=address_id, compromised=True)
        db.session.merge(address)
        db.session.commit()
    return render_template("submit.html")
