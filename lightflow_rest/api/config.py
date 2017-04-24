from flask import Blueprint

api = Blueprint('config', __name__, url_prefix='/config')


@api.route('/')
def index():
    return 'Config index'
