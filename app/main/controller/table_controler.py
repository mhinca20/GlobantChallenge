#!/usr/bin/env python
from flask_restx import Resource

from flask import request
from ..util.dto import TableDto
from ..service.table_service import clean_table, get_table_count

api = TableDto.api
tbl = TableDto.tbl
      
@api.route('/cleanTable', methods=['POST'])
@api.expect(tbl, validate=True)
class CleanTable(Resource):
    def post(self):
        """"Receive table name and delete all data from the database"""
        post_data = request.json
        return clean_table(post_data.get('table-name'))
            
@api.route('/<table_name>', methods=['GET'])
@api.param('table_name', 'Table name')
class CountTable(Resource):
    def get(self, table_name):
        """"Receive table name and get count from the database"""
        return get_table_count(table_name)

           
