from app.main import db
from app.main.model.employee import Employee
from app.main.model.department import Department
from app.main.model.job import Job

def save_changes(data) -> None:
    db.session.add(data)
    db.session.commit()
    
def exec_query_from_file(file_name):
    with open(file_name) as file:
        sql = file.read().rstrip()
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