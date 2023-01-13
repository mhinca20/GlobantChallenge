#!/usr/bin/env python
from flask_restx import Resource

from flask import request
from ..util.dto import UploadDto
from ..service.csv_service import receive_data

api = UploadDto.api

@api.route('/', methods=['POST'])
@api.expect('file-type', 'File type to transfer')
@api.expect('file', 'File to transfer')
@api.expect('batch-size', 'batch size from 1 to 1000')
@api.expect('next-row', 'next row')
class Csv(Resource):
    def post(self):
        """"Receive data from CSV and save it into the database"""
        file_type = request.form.get('file-type')
        csv_file = request.files['file']
        next_row = request.form.get('next-row')
        next_row = 0 if not next_row else next_row
        return receive_data(file_type, csv_file, int(request.form.get('batch-size')), int(next_row))
           