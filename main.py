from  Data_analis import Vizualisation
import psycopg2
conn = psycopg2.connect(user="user1", password="123321", dbname="lr2")
cur = conn.cursor()

if __name__ == '__main__':
   conn = psycopg2.connect(user="user1", password="123321", dbname="lr2")
   cur = conn.cursor()
   with conn:
      cur = conn.cursor()
      cur.execute("""DROP view player_n;
DROP view player_stats;
DROP view player_field_goals;""")
      cur.execute("CREATE VIEW player_n AS  SELECT player_name FROM player  ;")
      cur.execute("""CREATE VIEW player_stats AS 
SELECT total_points FROM statistic;""")
      cur.execute("""CREATE VIEW player_field_goals AS 
SELECT field_goals FROM statistic;""")
   data1 = Vizualisation.Get_visualisation(user_name="user1", database_name="lr2", password  ="123321", host  ="localhost", port ="5432")
   print(data1.get_column_gistogram( " select total_points FROM statistic"  ," select trim(player_name) FROM player"))
   print(data1.get_circle_gistogram("  select total_points  FROM statistic "  ,  "   select trim(player_name) FROM player"))
   print(data1.dependency_graphick("  select field_goals  FROM statistic " , "  select total_points  FROM statistic "))
