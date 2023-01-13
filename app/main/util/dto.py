from flask_restx import Namespace, fields


class UploadDto:
    api = Namespace('upload', description='upload related operations')
    
class AnalyticsDto:
    api = Namespace('analytics', description='analytics related operations')
    
class TableDto:
    api = Namespace('table', description='table related operations')
    tbl = api.model('table', {
        'table-name': fields.String(required=True, description='table name used in the operation'),
    })

class EmployeeDto:
    api = Namespace('employee', description='employee related operations')
    emp = api.model('employee', {
        'id': fields.String(required=True, description='employee id'),
        'name': fields.String(required=True, description='employee name'),
        'datetime': fields.String(required=True, description='employee hire datetime'),
        'department_id': fields.String(description='employee department_id'),
        'job_id': fields.String(description='employee job_id')
    })
    
class DepartmentDto:
    api = Namespace('department', description='department related operations')
    dep = api.model('department', {
        'id': fields.String(required=True, description='department id'),
        'department': fields.String(required=True, description='department name')
    })

class JobDto:
    api = Namespace('job', description='job related operations')
    job = api.model('job', {
        'id': fields.String(required=True, description='job id'),
        'job': fields.String(required=True, description='job name')
    })
