from flask_restx import Namespace, fields


class UploadDto:
    api = Namespace('upload', description='upload related operations')
    up = api.model('upload', {
        'table-name':  fields.String(required=True, description='table name (employee, department, job)'),
        'bucket':  fields.String(required=True, description='bucket name'),
        'key':  fields.String(required=True, description='key or file name inside the bucket'),
        'batch-size':  fields.Integer(required=True, description='batch size to load'),
        'next-row':  fields.Integer(required=True, description='id of next row to be inserted')
    })
    
class AnalyticsDto:
    api = Namespace('analytics', description='analytics related operations')
    
class TableDto:
    api = Namespace('table', description='table related operations')
    tbl = api.model('table', {
        'table-name': fields.String(required=True, description='table name used in the operation')
    })
