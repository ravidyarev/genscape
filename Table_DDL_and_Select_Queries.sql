PART 1 - DDLs

--Master table for country information
create table country_master (country_cd varchar(5) NOT NULL PRIMARY KEY, country_name varchar(45))

--Master table for film crew
create table movie_crew_master (crew_id int AUTO INCREMENT NOT NULL PRIMARY KEY, first_name varchar(30), last_name varchar(30))

--Master table for film crew roles -  actor, director
create table movie_role_master (role_id int AUTO INCREMENT NOT NULL PRIMARY KEY, role_name varchar(30))

--master table for all movies
create table movie_master (movie_id int NOT NULL PRIMARY KEY, movie_title varchar(50), origin_country_cd varchar(5), movie_genre varchar(30),
FOREIGN KEY ( origin_country_cd ) REFERENCES  country_master (country_cd   ));

--master table for list review authors
create table review_author_master (review_author_id   int AUTO INCREMENT NOT NULL PRIMARY KEY ,review_author_name varchar(50)) 

--transaction table for movie release details
create table movie_release_info (release_id int AUTO INCREMENT NOT NULL PRIMARY KEY, movie_id int ,release_country_cd varchar(5), release_start_dt datetime, release_end_dt datetime,review_author_id int,
FOREIGN KEY ( movie_id ) REFERENCES  movie_master (movie_id   ),
FOREIGN KEY ( release_country_cd ) REFERENCES  country_master (country_cd   ),
FOREIGN KEY ( review_author_id ) REFERENCES  review_author_master  (review_author_id      ))

--transaction table for movie popularity details
create table movie_popularity_details(movie_popularity_id int AUTO INCREMENT NOT NULL PRIMARY KEY, movie_id int, record_date datetime,vote_count int, FOREIGN KEY ( movie_id ) REFERENCES  movie_master (movie_id   )
)

--transaction table for movie credits
create table movie_credits(movie_id int, movie_crew_id int, movie_role_id int,
FOREIGN KEY ( movie_id ) REFERENCES  movie_master (movie_id   ),
FOREIGN KEY ( movie_crew_id ) REFERENCES  movie_crew_master (crew_id ),
FOREIGN KEY ( movie_role_id ) REFERENCES  movie_role_master ( role_id ))

PART 2 : Queries:
1. Which movies were playing on a particular date in a particular country?
select mm.movie_title from movie_release_info mr join movie_master mm on (mr.movie_id=mm.movie_id) where <filter_date> between release_start_dt and release_end_date and movie_release_country_cd = <filter_country_cd>

2.Which movies are directed by a particular director?
select mm.movie_title from movie_credits mc 
join movie_master mm on (mr.movie_id=mm.movie_id) 
join movie_role_master mr on (mr.role_id=mc.movie_role_id ) 
join movie_crew_master mcm on (mcm.crew_id=mc.movie_crew_id ) 
where mr.role_name='DIRECTOR'
and mcm.first_name = <filter_director_first_name>
and mcm.last_name = <filter_director_last_name>


3. How many movies of a particular genre are now playing in a particular country?
select count(*) from movie_master mm 
join movie_release_info mr on (mr.movie_id=mm.movie_id) 
join country_master cc on (cc.country_cd=mr.release_country_cd)
where mm.genre = <filter_genre>
and cc.country_name = <filter_country_name>

4.Which review authors write the most reviews per country?
select country_name,review_author_name,count(movie_id)  from  movie_release_info mr 
join country_master cc on (cc.country_cd=mr.release_country_cd)
join review_author_master ra on (ra.review_author_id  = mr.review_author_id)
group by country_name,review_author_name order by count(movie_id)  desc

5. In which country are most movies produced?
select country_name,count(*) from movie_master mm 
join country_master cc on (cc.country_cd=mm.orgin_country_cd)
group by country_name order by count(*) desc

6. What was the popularity of a particular movie on a particular date?
select mm.movie_title ,mp.vote_count from movie_popularity_details mp
join movie_master mm on (mp.movie_id=mm.movie_id)
where mm.movie_title = <filter_movie_title>
and mp.record_date = <filter_record_date>

