# genscape
genscape_movie_db_assignment

Step 1 : 
Objective : Create DDL script to create the required to save all the details fecthed from TMDb APIs
Code/Script : Table_DDL_and_Select_Queries.sql
Descripton : The PART 1 of the script lists the DDL staements for the tables required to meet the requirements of the asked queries. 
Have follwed the normalized forms, these tables can be combined to achieve performance if required.


Step 2 :  
Objective : Get details from API and save to DB, ETL process to save the Movie details into a DB for analytics
Code/Script : now_playing_movie.py
Description : The python (python 3) script connects to the API and fetches the data and saves it to the sqlite DB.
The code currently demonstrates the basic steps required to fetch data from APIs and save to the DB.
More API fetches need to be added to get details - example credit details, get popular etc


Step 3 :
Objective : Sample queries for the questions asked
Code/Script : Table_DDL_and_Select_Queries.sql
Descripton : The PART 2 of the script lists SQL queries for the asked questions
