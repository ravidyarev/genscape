import http.client
import json
import requests
import sqlite3

#Create a DB to save movie info
dbname='now_playing_movie_db,sqllite'
conn = sqlite3.connect(str(dbname))
cur=conn.cursor()

#fetch data from TMDb
conn = http.client.HTTPSConnection("api.themoviedb.org")

country_list=['US']#,'UK','IE','AU','CA']

for i in country_list:
  #print(i)

  payload = "{}"

  conn.request("GET", "/3/movie/now_playing?page=1&language=en-US&api_key=bbb0e77b94b09193e6f32d5fac7a3b9c&region="+i, payload)

  res = conn.getresponse()
  now_playing_data = res.read()

  now_playing_parsed = json.loads(now_playing_data)
  
  #to get director info
  payload = "{}"
  conn.request("GET", "/3/movie/320288/credits?api_key=bbb0e77b94b09193e6f32d5fac7a3b9c", payload)

  res = conn.getresponse()
  credits_data = res.read()

  credits_parsed = json.loads(credits_data)

  #print(json.dumps(parsed, indent=4, sort_keys=True))

  #with open('data'+i+'.json', 'w') as outfile:
  #  json.dump(parsed, outfile)

#print(parsed['results'][0]['id'])
#Create DB with sqllite


# Goes through the json dataset and extracts information if it is available
if parsed['results'][0]['id']!='N/A':
    movie_id = int(now_playing_parsed['results'][0]['id'])
    movie_title = now_playing_parsed['results'][0]['title']
    movie_genre = now_playing_parsed['results'][0]['genre_ids']

print(movie_genre)
# SQL commands
cur.execute('''DROP TABLE Movie_List''')

cur.execute('''CREATE TABLE IF NOT EXISTS Movie_List 
(Movie_Id INTEGER, Movie_Title Text )''')

cur.execute('SELECT Movie_Id,Movie_Title FROM Movie_List WHERE Movie_Id = ? ', (movie_id,))
row = cur.fetchone()

if row is None:
    cur.execute('''INSERT INTO Movie_List (Movie_Id,Movie_Title)
            VALUES (?,?)''', (movie_id,movie_title,))
else:
    print("Record already found. No update made.")

cur.execute('SELECT Movie_Id,Movie_Title FROM Movie_List WHERE Movie_Id = ? ', (movie_id,))
print(cur.fetchone())
