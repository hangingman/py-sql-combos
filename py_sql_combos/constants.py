# -*- coding: utf-8 -*-

SAMPLE_QUERY = """SELECT
e.name AS employee_name
, e.email AS employee_email
, e.name AS department_name
FROM employee e

LEFT JOIN department d
ON e.id = d.employee_id;"""
