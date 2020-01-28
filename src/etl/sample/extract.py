#
import os
import csv
from db.connections import Relational

# Uncomment
# conn_string = os.getenv('ANALYTICS')
conn_string = 'sqlite:///sample.db'
data_file = os.path.dirname(__file__).replace('/src/etl/', '/data/') + '.csv'
qry_file = os.path.dirname(__file__) + '/customers.sql'

def customer_data():
    with open(data_file, 'w+') as raw:
        out = csv.writer(raw)
        with open(qry_file) as sql:
            with Relational(conn_string) as db:
                data = db.query(sql.read())
                out.writerows(data)