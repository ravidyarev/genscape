import http.client
import json
import requests
import sqlite3
#import pandas as pd

#Create a DB to save movie info
dbname='now_playing_movie_db,sqllite'
dbconn = sqlite3.connect(str(dbname))
cur=dbconn.cursor()
#cur.execute('''DROP TABLE Movie_List ''')
cur.execute('''CREATE TABLE IF NOT EXISTS Movie_List 
(Movie_Id INTEGER, Movie_Title Text, Release_Country Text )''')

#fetch data from TMDb
conn = http.client.HTTPSConnection("api.themoviedb.org")

country_list=['US','UK','IE','AU','CA']

for i in country_list:
  #fetch currently playing movies
  payload = "{}"
  conn.request("GET", "/3/movie/now_playing?page=1&language=en-US&api_key=bbb0e77b94b09193e6f32d5fac7a3b9c&region="+i, payload)
  res = conn.getresponse()
  now_playing_data = res.read()
  now_playing_parsed = json.loads(now_playing_data)
  
  #Save the fetched data to DB
  j=0
  for k in now_playing_parsed['results']:
    if now_playing_parsed['results'][j]['id']!='N/A':
      movie_id = int(now_playing_parsed['results'][j]['id'])
    if now_playing_parsed['results'][j]['title']!='N/A':
      movie_title = now_playing_parsed['results'][j]['title'] 
    j=j+1
  
    cur.execute('SELECT Movie_Id,Movie_Title,Release_Country FROM Movie_List WHERE Movie_Id = ?', (movie_id,))
    row = cur.fetchone()

    if row is None:
      cur.execute('''INSERT INTO Movie_List (Movie_Id,Movie_Title,Release_Country)
            VALUES (?,?,?)''', (movie_id,movie_title,str(i)))
 

#Validate results save
cur.execute('SELECT Movie_Id,Movie_Title,Release_Country FROM Movie_List')
print(cur.fetchall())

#print (pd.read_sql_query("SELECT * FROM Movie_List", dbconn))

dbconn.commit()
dbconn.close()
