from app.main import db
from app.main.model.employee import Employee
from app.main.model.department import Department
from app.main.model.job import Job
from app.main.util.s3_helper import read_file

def save_changes(data) -> None:
    db.session.add(data)
    db.session.commit()
    
def exec_query_from_file(bucket, file_name):
    sql = " ".join(read_file(bucket, file_name))
    result = db.engine.execute(sql)
    return result
    
def exec_query(sql):
    result = db.engine.execute(sql)
    return result

def check_job(row):
    return True if db.session.query(Job).filter_by(id=row).count() < 1 else False

def check_emp(row):
    return True if db.session.query(Employee).filter_by(id=row).count() < 1 else False

def check_dep(row):
    return True if db.session.query(Department).filter_by(id=row).count() < 1 else False