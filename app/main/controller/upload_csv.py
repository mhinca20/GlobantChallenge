#!/usr/bin/env python
from flask_restx import Resource

from flask import request
from ..util.dto import UploadDto
from ..service.csv_service import receive_data

api = UploadDto.api
up = UploadDto.up

@api.route('/', methods=['POST'])
@api.expect(up, validate=True)
class Csv(Resource):
    def post(self):
        """"Receive data from CSV and save it into the database"""
        file_type = request.json.get('table-name')
        csv_file = request.json.get('file')
        next_row = request.json.get('next-row')
        next_row = 0 if not next_row else next_row
        return receive_data(file_type, csv_file, int(request.json.get('batch-size')), int(next_row))
           