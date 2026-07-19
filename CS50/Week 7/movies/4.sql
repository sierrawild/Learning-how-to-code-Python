-- 4. Number of movies with a 10.0 rating
select title from movies where id in (select movie_id from ratings where rating = "10.0");
