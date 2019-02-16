#!/usr/bin/python
"""
Interview Challenge APP
"""

import os
import datetime
import mysql.connector
from flask import Flask, render_template

app = Flask(__name__)

class Db:
    """ Database class """
    def __init__(self):
        self.conn = mysql.connector.connect(
            host=os.environ['DB_HOST'],
            user=os.environ['MYSQL_USER'],
            passwd=os.environ['MYSQL_PASSWORD'],
            database=os.environ['MYSQL_DATABASE']
        )
        self.cur = self.conn.cursor()
    def select(self, query):
        """ Execute select query and returns a cursor """
        self.conn.ping(reconnect=True, attempts=3, delay=0.2)
        self.cur.execute(query)
        return self.cur

def get_db_date():
    """ Returns the current date/time from the DB """
    database = Db()
    return database.select("SELECT now()").fetchall()

@app.route('/')
def hello():
    """ Hello world that test the DB connection """
    date = get_db_date()
    return 'Hello World! Database says is {} now.\n'.format(date[0][0])

@app.route('/employees/custom_list')
def custom_list():
    """ Custom endpoint that solves the challenge in an ad-hoc way """
    database = Db()
    max_hire_date = datetime.date(1990, 1, 1)

    employees = database.select("""select * from employees where gender = "M" and
			  hire_date > "%s" order by first_name, last_name
			  limit 10""" % max_hire_date)
    result = {}
    result['table_name'] = "Employees"
    result['headers'] = employees.column_names
    result['table'] = employees.fetchall()

    return render_template('employees.html', result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
