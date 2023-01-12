#!/usr/bin/env python
from flask_restx import Resource

from flask import request
from ..util.dto import UploadDto
from ..service.csv_service import receive_data

api = UploadDto.api

#TODO add las ingested and batch size validation
@api.route('/', methods=['GET', 'POST'])
@api.expect('file-type', 'File type to transfer')
@api.expect('file', 'File to transfer')
@api.expect('batch-size', 'batch size from 1 to 1000')
class Csv(Resource):
    def post(self):
        """"Receive data from CSV and save it into the database"""
        file_type = request.form.get('file-type')
        csv_file = request.files['file']
        return receive_data(file_type,csv_file)
           