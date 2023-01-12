from io import TextIOWrapper
from datetime import datetime
import logging

from app.main.model.employee import Employee
from app.main.model.department import Department
from app.main.model.job import Job


from app.main import db
import csv 
import sys

logging.basicConfig(filename=f'logs/data_upload_{datetime.now().strftime("%Y_%m_%d_%H_%M")}.log',
                    filemode='a',
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s: %(message)s')

logger = logging.getLogger('Globant challenge')
logger.setLevel(logging.ERROR)

def receive_data(file_type, csv_file):
    response_object = None
    if file_type in csv_file.filename: 
        csv_file = TextIOWrapper(csv_file, encoding='utf-8')
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in filter_csv(csv_reader):
            if "employee" == file_type:
                row = Employee(id=row[0], name=row[1], datetime=row[2], department_id=row[3], job_id=row[4])
            elif "department" == file_type:
                row = Department(id=row[0], department=row[1])
            else:
                row = Job(id=row[0], job=row[1])
            save_changes(row)
        response_object = {
            'status': 'success',
            'message': 'Data succesfully loaded.'
        },201
    else:
        response_object = {
            'status': 'fail',
            'message': 'File type not corresponding with the given file'
        }
    return response_object

def filter_csv(csv_reader):
    for row in csv_reader:
        if '' in row:
            logging.info("The following row is not going to be inserted, it contains empty values "+str(row))
        else:
            yield row
    
        
def save_changes(data) -> None:
    db.session.add(data)
    db.session.commit()