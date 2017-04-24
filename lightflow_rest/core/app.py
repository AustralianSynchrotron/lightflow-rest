from flask import Flask
from werkzeug.utils import find_modules, import_string


def register_apis(app):
    for name in find_modules('lightflow_rest.api'):
        mod = import_string(name)
        if hasattr(mod, 'api'):
            app.register_blueprint(mod.api)


def create_app(config):
    app = Flask(__name__)

    register_apis(app)

    return app
