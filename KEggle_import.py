import psycopg2
import csv
import decimal
import matplotlib.pyplot as plt
import numpy as np

import re
qurery_create = """
CREate TABLE player(
   player_id integer ,
   player_name text,
   player_position text  



);




CREate TABLE statistic(
 stat_id integer , 
 player_id integer,
 total_games integer , 
 total_points integer, 
 field_goals integer
);

ALTer TABLE player
ADD CONSTRAINT player_id   primary KEY (player_id);

ALTer TABLE statistic
ADD CONSTRAINT stat_id primary KEY  (stat_id) , 
ADD CONstraint player_id FOREIGN KEY(player_id )  REFERENCES player(player_id);

"""

query_drop ="""
DROP TABLE player CASCADE;
DROP TABLE statistic CASCADE;

"""

def create_table():

 conn = psycopg2.connect(user="user1", password="123321", dbname="lr2")

 with conn:
    cur = conn.cursor()
    cur.execute(query_drop)
    cur.execute(qurery_create)
    INPUT_CSV_FILE = r"C:\Users\boda1\PycharmProjects\db_Lab_2\venv\nba.csv"
    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf)
        values_of_players =  []
        values_of_player_position = [ ]

        values_of_total_games  =  [ ]
        values_of_total_points = []
        values_of_field_goals = [ ]
        for idx, row in enumerate(reader):

            values_of_players.append(row['player'])
            values_of_player_position.append(row['position'])
            values_of_total_games.append(row["total_games"])
            values_of_total_points.append(row["total_points"])
            values_of_field_goals.append(row["field_goals"])


        person_id = [i+1 for i in range(len(values_of_players))]
        print(person_id)
        staistic_id = np.array([i+101 for i in range(len(values_of_players))])
        print(cur.execute("select* from statistic"))
        sql3 = "insert Into player  VALUES"
        sql4 = f"insert Into statistic VALUES "
        for i in person_id:

            name = values_of_players[i-1].replace("'", "")
            sql3 += (f"({i} ,\' {name } \' , \'{ values_of_player_position[i-1]} \') ,")
            sql4 +=  f"({staistic_id[i-1]} , {i} ,{values_of_total_games[i-1]} , {values_of_total_points[i-1]} , {values_of_field_goals[i-1]}) ,"

        sql3 = sql3.rstrip(sql3[-1])
        sql3 +=";"
        sql4 = sql4.rstrip(sql4[-1])
        sql3 += ";"
        print(sql4)
        cur.execute(sql3)
        cur.execute(sql4)




create_table()

