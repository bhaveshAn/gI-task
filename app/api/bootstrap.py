from flask import current_app as app, Blueprint
from flask_rest_jsonapi import Api

general = Blueprint('v1', __name__, url_prefix='')
api = Api(app, general)
