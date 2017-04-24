from flask import Blueprint

api = Blueprint('worker', __name__, url_prefix='/worker')


@api.route('/')
def index():
    return 'Worker index'
