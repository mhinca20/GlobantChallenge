from app.main import db

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