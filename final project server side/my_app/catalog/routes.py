from flask import request, jsonify, Blueprint
catalog = Blueprint('catalog', __name__)

@catalog.route('/')
@catalog.route('/index')
def index():
    return "Hello world!"
