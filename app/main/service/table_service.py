from io import TextIOWrapper
from flask import jsonify

import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

from app.main.model.employee import Employee
from app.main.model.department import Department
from app.main.model.job import Job
from app.main import db
from app.main.util.db_utils import save_changes, exec_query
from app.main.util.config import config
from app.main.util.s3_helper import read_file, upload_file, read_file_bytes


s3_bucket = config().get('DATA','bucket')
backup_path = config().get('DATA','avro_backup_path')
schema_path = config().get('DATA','avro_schema_path')

def clean_table(table):
    exec_query("delete from "+ table )
    response_object = {
            'status': 'success',
            'message': f'Data succesfully deleted from table {table}.'
        }
    return response_object

def get_table_count(table):
    result = exec_query("select count(*) as count from "+ table )
    return jsonify({
            'status': 'success',
            'message': f'Data succesfully count from table {table}.',
            table: [dict(row) for row in result]})

def backup_table(table):   
    schema = avro.schema.parse(" ".join(read_file(s3_bucket, schema_path + table +".avsc")))
    writer = DataFileWriter(open(backup_path + table +".avro", "wb"), DatumWriter(), schema)
    result = exec_query("select * from "+ table )
    for row in result:
        writer.append(dict(row))
    writer.close()
    if upload_file(backup_path + table +".avro", s3_bucket, backup_path+ table +".avro"):
        return {
                'status': 'success',
                'message': f'Data succesfully backed up from table {table}.'
            }
    return {
                'status': 'failed',
                'message': f'Data failed backup failed from table {table}.'
            }

def restore_table(table):
    avro_bytes = read_file_bytes(s3_bucket, backup_path+ table +".avro")
    reader = DataFileReader(avro_bytes, DatumReader())
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