#!/usr/bin/env python
from flask_restx import Resource

from flask import request
from ..util.dto import AnalyticsDto
from ..service.analytics_service import get_hired_employees_by_q, get_higer_hires_by_dep

api = AnalyticsDto.api

@api.route('/employeesbyq', methods=['GET'])
class EmployeeByQ(Resource):
    def get(self):
        """Get the numbers of employees hired by department and job in the different Qs in 2021"""
        return get_hired_employees_by_q()

@api.route('/higerhiresdep', methods=['GET'])
class HiresByDep(Resource):
    def get(self):
        """Get number of hires by department in 2021 where the number of hires is more than the mean of all departments in 2021"""
        return get_higer_hires_by_dep()