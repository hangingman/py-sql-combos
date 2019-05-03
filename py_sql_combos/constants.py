# -*- coding: utf-8 -*-

SAMPLE_QUERY = """SELECT d.dept_name AS 'Dept',
CONCAT(em.last_name, ' ', em.first_name) AS 'Manager last, first',
CONCAT(e.last_name,' ', e.first_name, ' ', t.title) AS 'Employee last, first (title)'
FROM dept_manager AS dm

LEFT JOIN dept_emp AS de ON de.dept_no = dm.dept_no
LEFT JOIN departments AS d ON d.dept_no = dm.dept_no
LEFT JOIN employees AS e ON e.emp_no = de.emp_no
LEFT JOIN employees AS em ON em.emp_no = dm.emp_no
LEFT JOIN titles AS t ON t.emp_no = e.emp_no

WHERE
dm.emp_no = e.emp_no
AND
dept_name = 'Sales'
OR
dept_name = 'Marketing'
AND
dm.to_date >= '2012-05-07'
AND
t.to_date > '2012-05-07'
AND
de.to_date > '2012-05-07'

ORDER BY e.last_name, e.first_name

limit 1000
;"""
