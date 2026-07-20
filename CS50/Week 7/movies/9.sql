-- 9. Names of all people who starred in a movie released in 2004, ordered by birth year
select people.name from people join stars on people.id = stars.person_id join movies on movies.id = stars.movie_id where movies.year = '2004';
