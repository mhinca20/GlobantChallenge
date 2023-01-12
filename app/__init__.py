from flask_restx import Api
from flask import Blueprint

from .main.controller.upload_csv import api as upload_csv
from .main.controller.table_controler import api as table

blueprint = Blueprint('api', __name__)


api = Api(
    blueprint,
    title='Globant Challenge',
    version='1.0',
    description='Globant challenge'
)

api.add_namespace(upload_csv)
api.add_namespace(table)

