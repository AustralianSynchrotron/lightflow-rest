from flask import Blueprint

api = Blueprint('workflow', __name__, url_prefix='/workflow')


@api.route('/')
def index():
    return 'Workflow index'
