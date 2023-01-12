from .. import db

class Department(db.Model):
    """ Department Model for storing department data """
    __tablename__ = "department"
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    department = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return "<Department: {}>".format(self.department)
