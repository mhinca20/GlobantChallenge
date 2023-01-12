from .. import db

class Employee(db.Model):
    """ Employee Model for storing employee data """
    __tablename__ = "employee"
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    datetime = db.Column(db.String, nullable=False)
    department_id = db.Column(db.Integer, nullable=False)
    job_id = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return "<Employee: {}>".format(self.name)
