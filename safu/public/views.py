# -*- coding: utf-8 -*-
import json
import random
from flask import Blueprint, render_template, request
import sqlalchemy
from ..extensions import db
from ..models.models import Address, Transaction, Report

blueprint = Blueprint('public', __name__)


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload


@blueprint.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


@blueprint.route('/api/address/<ids>', methods=['GET'])
def get_address(ids):
    addresses = Address.query.filter(Address.id.in_(ids.split(','))).all()
    return json.dumps({ 'addresses': [ address.to_dict() for address in addresses] })
    

@blueprint.route('/api/transaction/<id>', methods=['GET'])
def get_transactions(id):
    trans = Transaction.query.filter_by(sender_id=id).all()
    return json.dumps({ 'transactions': [t.to_dict() for t in trans] })


@blueprint.route('/api/submit', methods=['POST'])
def outdated():
    content = request.get_json()
    report = Report(address_id=content['address_id'], reporter_id=content['reporter_id'])
    db.session.merge(report)
    db.session.commit()
    return json.dumps({'success': True}), 200, {'ContentType':'application/json'} 
