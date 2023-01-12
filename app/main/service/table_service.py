from io import TextIOWrapper
from flask import jsonify

import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

from app.main.model.employee import Employee
from app.main.model.department import Department
from app.main.model.job import Job
from app.main import db
from app.main.util.db_utils import save_changes


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

def backup_table(table):   
    schema = avro.schema.parse(open("data/avro/schemas/"+ table +".avsc", "r").read())
    writer = DataFileWriter(open("data/avro/backup/"+ table +".avro", "wb"), DatumWriter(), schema)
    result = db.engine.execute("select * from "+ table )
    for row in result:
        writer.append(dict(row))
    writer.close()
    response_object = {
            'status': 'success',
            'message': f'Data succesfully backed up from table {table}.'
        }
    return response_object

def restore_table(table):
    reader = DataFileReader(open("data/avro/backup/"+table+".avro", "rb"), DatumReader())
    if "employee" == table:
        for row in reader:
            row = Employee(id=row['id'], name=row['name'], datetime=row['datetime'], department_id=row['department_id'], job_id=row['job_id'])
            save_changes(row)
    elif "department" == table:
        for row in reader:
            row = Department(id=row['id'], department=row['department'])
            save_changes(row)
    elif "job" == table:
        for row in reader:
            row = Job(id=row['id'], job=row['job'])
            save_changes(row)
    reader.close()
    response_object = {
            'status': 'success',
            'message': f'Data succesfully restored from avro file fro table {table}.'
        }
    return response_object