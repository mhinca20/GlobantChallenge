from io import TextIOWrapper
from datetime import datetime
import logging

from app.main.model.employee import Employee
from app.main.model.department import Department
from app.main.model.job import Job
from app.main.util.db_utils import save_changes, check_job, check_emp, check_dep
from app.main.util.s3_helper import read_file

import csv 

logging.basicConfig(filename=f'logs/data_upload_{datetime.now().strftime("%Y_%m_%d_%H_%M")}.log',
                    filemode='a',
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s: %(message)s')

logger = logging.getLogger('Globant challenge')
logger.setLevel(logging.ERROR)

def receive_data(table_name, bucket, key, batch, next_row):
    response_object = None
    if batch >= 1 and batch <= 1000 :
        csv_file = read_file(bucket, key)
        csv_reader = list(csv.reader(csv_file, delimiter=','))
        limit = next_row + batch
        limit = limit if limit <= len(csv_reader) else len(csv_reader)
        for row in filter_csv(csv_reader, next_row, limit):
            if "employee" == table_name:
                if check_emp(row[0]):
                    row = Employee(id=row[0], name=row[1], datetime=row[2], department_id=row[3], job_id=row[4])
                    save_changes(row)
            elif "department" == table_name:
                if check_dep(row[0]):
                    row = Department(id=row[0], department=row[1])
                    save_changes(row)
            elif "job" == table_name:
                if check_job(row[0]):
                    row = Job(id=row[0], job=row[1])
                    save_changes(row)
        response_object = {
            'status': 'success',
            'message': 'Data succesfully loaded.',
            'next_row': limit if limit < len(csv_reader) else None
        },201
    else:
        response_object = {
        'status': 'fail',
        'message': 'Batch size should be between 1 and 1000'
    }      
    return response_object

def filter_csv(csv_reader, next_row, limit):
    
    for row in range(next_row, limit):
        if '' in csv_reader[row]:
            logging.info("The following row is not going to be inserted, it contains empty values "+str(csv_reader[row]))
        else:
            yield csv_reader[row]
    