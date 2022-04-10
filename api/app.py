#!/usr/bin/env python
from io import TextIOWrapper
import csv
import os
import sys

from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../data/database.db'
db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    datetime = db.Column(db.String)
    department_id = db.Column(db.Integer)
    job_id = db.Column(db.Integer)
    
    def __repr__(self):
        return "<Employee: {}>".format(self.name)

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String)
    
    def __repr__(self):
        return "<Department: {}>".format(self.department)

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job = db.Column(db.String)
    
    def __repr__(self):
        return "<Job: {}>".format(self.job)

@app.route('/', methods=['GET', 'POST'])
def upload_csv():
    if request.method == 'POST':
        file_type = request.form.get('file-name')
        csv_file = request.files['file']
        if file_type in csv_file.filename: 
            csv_file = TextIOWrapper(csv_file, encoding='utf-8')
            csv_reader = csv.reader(csv_file, delimiter=',')
            if "employee" == file_type:
                for row in csv_reader:
                    row = Employee(id=row[0], name=row[1], datetime=row[2], department_id=row[3], job_id=row[4])
                    db.session.add(row)
                    db.session.commit()
            elif "department" == file_type:
                for row in csv_reader:
                    row = Department(id=row[0], department=row[1])
                    db.session.add(row)
                    db.session.commit()
            elif "job" == file_type:
                for row in csv_reader:
                    row = Job(id=row[0], job=row[1])
                    db.session.add(row)
                    db.session.commit()
            else:
                pass
            return redirect(url_for('upload_csv'))
    return """
            <form method='post' action='/' enctype='multipart/form-data'>
              Upload a csv file: <input type='file' name='file'>
              <label for="file-names">Choose file type:</label>
              <select name="file-name" id="file-names">
              <option value="employee">Employee</option>
              <option value="job">Job</option>
              <option value="department">Department</option>
              </select>
              <input type='submit' value='Upload'>
              <br>
            </form>
           """
           
    @app.route('/backup', methods=['POST'])
    def backuptable():
        pass

if __name__ == '__main__':
    db.create_all()
    if os.environ.get('PORT') is not None:
        app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT'))
    else:
        app.run(debug=True, host='0.0.0.0') 

