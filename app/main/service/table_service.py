from io import TextIOWrapper
from flask import jsonify

from app.main.model.employee import Employee
from app.main.model.department import Department
from app.main.model.job import Job

from app.main import db
import csv 
import sys


def clean_table(table):
    db.engine.execute("delete from "+ table )
    response_object = {
            'status': 'success',
            'message': f'Data succesfully deleted from table {table}.'
        }
    return response_object

def get_table_count(table):
    result = db.engine.execute("select count(*) as count from "+ table )
    return jsonify({
            'status': 'success',
            'message': f'Data succesfully count from table {table}.',
            table: [dict(row) for row in result]})