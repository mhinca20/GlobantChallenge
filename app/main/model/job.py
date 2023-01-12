from .. import db

class Job(db.Model):
    """ Job Model for storing job data """
    __tablename__ = "job"
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    job = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return "<Job: {}>".format(self.job)
