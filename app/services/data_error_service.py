import os
from flask import Flask, jsonify, make_response

from app.model_auth.model import db

from app.api.app import api


def create_app(config_module=None):

    app = Flask(__name__)
    app.config.from_object(config_module or os.environ.get('Flask_Config') or 'config')
    db.init_app(app)

    app.register_blueprint(api)

    @app.route('/')
    def index():
        response = make_response('Suade Challenge')
        response.headers['Content-Type'] = 'text/plan'
        return response

    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({'error_code': 404, 'error_desc': 'Not Found'}), 404

    @app.errorhandler(500)
    def not_found_error(error):
        return jsonify({'error_code': 500, 'error_desc': 'Internal Server Error'}), 500

    return app




