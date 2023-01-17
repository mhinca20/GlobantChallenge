from flask import jsonify
from app.main.util.db_utils import exec_query_from_file
from app.main.util.config import config

s3_bucket = config().get('DATA','bucket')
sql_path = config().get('DATA','query_path')

def get_hired_employees_by_q():
    result = exec_query_from_file(s3_bucket, sql_path + "hiredemployees2021.sql")
    return jsonify({
            'status': 'success',
            'message': 'Employees hired in 2021',
            'result': [dict(row) for row in result]})

def get_higer_hires_by_dep():
    result = exec_query_from_file(s3_bucket, sql_path + "departmenthires.sql")
    return jsonify({
            'status': 'success',
            'message': 'Hires by deparment',
            'result': [dict(row) for row in result]})