#!/usr/bin/env python
from io import TextIOWrapper
import csv
import os
import sys
from flask import Flask, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../data/database.db'
db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    datetime = db.Column(db.String, nullable=False)
    department_id = db.Column(db.Integer, nullable=False)
    job_id = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return "<Employee: {}>".format(self.name)

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    department = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return "<Department: {}>".format(self.department)

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    job = db.Column(db.String, nullable=False)
    
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

@app.route('/employeesbyq', methods=['GET'])
def employeesbyq():
    with open("../data/hiredemployees2021.sql") as file:
        sql = file.read().rstrip()
        print(sql,file=sys.stderr)
        result = db.engine.execute(sql)
        print(result,file=sys.stderr)
        return jsonify({'result': [dict(row) for row in result]})
           
    
@app.route('/higerhiresdep', methods=['GET'])
def higerhiresdep():
    with open("../data/departmenthires.sql") as file:
        sql = file.read().rstrip()
        print(sql,file=sys.stderr)
        result = db.engine.execute(sql)
        print(result,file=sys.stderr)
        return jsonify({'result': [dict(row) for row in result]})

if __name__ == '__main__':
    db.create_all()
    if os.environ.get('PORT') is not None:
        app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT'))
    else:
        app.run(debug=True, host='0.0.0.0') 

