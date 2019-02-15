import time

import mysql.connector
from flask import Flask
import os

app = Flask(__name__)

retries = 30
while retries >= 0:
    try:
        db = mysql.connector.connect(
          host = os.environ['DB_HOST'],
          user = os.environ['MYSQL_USER'],
          passwd = os.environ['MYSQL_PASSWORD'],
          database  = os.environ['MYSQL_DATABASE']
        )
        break
    except mysql.connector.errors.InterfaceError as exc:
        if retries == 0:
            raise exc
        retries -= 1
        time.sleep(2)
    except Exception as e:
        print("type error: " + str(e))
        raise e



def get_db_date():
    cursor = db.cursor()
    cursor.execute("SELECT now()")
    return cursor.fetchall()

@app.route('/')
def hello():
    date = get_db_date()
    return 'Hello World! Database says is {} now.\n'.format(date[0][0])

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
