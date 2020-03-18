from flask import Flask
from flask_restplus import Api, Resource


def create_app(config):
    api = Api()
    app = Flask(__name__)
    api.init_app(app)

    @api.route('/hello')
    class HelloWorld(Resource):
        def get(self):
            return {'hello': 'world'}

    return app



