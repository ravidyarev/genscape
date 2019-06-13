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

Step 4 : 
Objective : A job to appended a table with the count of different movies that were playing during the previous month per country
Code/Script : Table_DDL_and_Select_Queries.sql
Description : The PART 3 of the script has the SP to update the table with movie count details for previous month. The SP takes in the build month/year as input. The input gives the flexibilty to run it for any month at any point.
