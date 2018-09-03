import os.path
from envparse import env
from flask import Flask, json, make_response
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_rest_jsonapi.exceptions import JsonApiException
from flask_rest_jsonapi.errors import jsonapi_errors
from flask_cors import CORS

from app.models import db


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
env.read_envfile()


class ReverseProxied(object):

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        scheme = environ.get('HTTP_X_FORWARDED_PROTO')
        if scheme:
            environ['wsgi.url_scheme'] = scheme
        if os.getenv('FORCE_SSL', 'no') == 'yes':
            environ['wsgi.url_scheme'] = 'https'
        return self.app(environ, start_response)


app.wsgi_app = ReverseProxied(app.wsgi_app)

app_created = False


def create_app():
    global app_created
    Migrate(app, db)

    app.config.from_object(env('APP_CONFIG',
                           default='config.ProductionConfig'))
    db.init_app(app)
    _manager = Manager(app)
    _manager.add_command('db', MigrateCommand)

    CORS(app, resources={r"/*": {"origins": "*"}})

    # APIs
    with app.app_context():
        from app.api.bootstrap import general

        app.register_blueprint(general)

    app_created = True
    return app, _manager, db


current_app, manager, database = create_app()


@app.errorhandler(500)
def internal_server_error(error):
    exc = JsonApiException({'pointer': ''}, 'Unknown error')
    return make_response(
               json.dumps(jsonapi_errors([exc.to_dict()])),
               exc.status, {'Content-Type': 'application/vnd.api+json'}
           )


if __name__ == '__main__':
    current_app.run()
