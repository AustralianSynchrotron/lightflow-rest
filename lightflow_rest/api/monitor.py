from flask import Blueprint

api = Blueprint('monitor', __name__, url_prefix='/monitor')


@api.route('/')
def index():
    return 'Monitor index'
