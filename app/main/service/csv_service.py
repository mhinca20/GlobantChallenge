from io import TextIOWrapper
from datetime import datetime
import logging

from app.main.model.employee import Employee
from app.main.model.department import Department
from app.main.model.job import Job
from app.main.util.db_utils import save_changes



from app.main import db
import csv 
import sys

logging.basicConfig(filename=f'logs/data_upload_{datetime.now().strftime("%Y_%m_%d_%H_%M")}.log',
                    filemode='a',
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s: %(message)s')

logger = logging.getLogger('Globant challenge')
logger.setLevel(logging.ERROR)

def receive_data(file_type, csv_file, batch, next_row):
    response_object = None
    if file_type in csv_file.filename: 
        if batch >= 1 and batch <= 1000 :
            csv_file = TextIOWrapper(csv_file, encoding='utf-8')
            csv_reader = list(csv.reader(csv_file, delimiter=','))
            for row in filter_csv(csv_reader, next_row, batch):
                if "employee" == file_type:
                    row = Employee(id=row[0], name=row[1], datetime=row[2], department_id=row[3], job_id=row[4])
                elif "department" == file_type:
                    row = Department(id=row[0], department=row[1])
                else:
                    row = Job(id=row[0], job=row[1])
                save_changes(row)
            response_object = {
                'status': 'success',
                'message': 'Data succesfully loaded.',
                'inserted_rows': str(batch),
                'next_row': str(next_row + batch )
            },201
        else:
            response_object = {
            'status': 'fail',
            'message': 'Batch size should be between 1 and 1000'
        }      
    else:
        response_object = {
            'status': 'fail',
            'message': 'File type not corresponding with the given file'
        }
    return response_object

def filter_csv(csv_reader, next_row, batch):
    for row in range(next_row, next_row + batch ):
        if '' in csv_reader[row]:
            logging.info("The following row is not going to be inserted, it contains empty values "+str(csv_reader[row]))
        else:
            yield csv_reader[row]
    