-- 10. Names of all directors who have directed a movie that got a rating of at least 9.0
select people.name from people
join directors on directors.person_id = people.id
join movies on movies.id = directors.movie_id
join ratings on movies.id = ratings.movie_id
where ratings.rating >= '9.0' order by ratings.rating;