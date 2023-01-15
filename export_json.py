import json
import psycopg2
import os



conn = psycopg2.connect(user="user1", password="123321", dbname="lr2" )

data = {}

os.remove("all_data.json")

with conn:
    cur = conn.cursor()

    for table in ('player', 'statistic', 'team_year'):
        cur.execute('SELECT * FROM ' + table)
        rows = []
        fields = [x[0] for x in cur.description]

        for row in cur:
            rows.append(dict(zip(fields, row)))

        data[table] = rows

with open('all_data.json', 'w') as outf:
    json.dump(data, outf, default=str)