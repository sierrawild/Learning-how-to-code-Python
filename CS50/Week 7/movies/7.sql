-- 7. All movies and ratings from 2010, in decreasing order by rating (alphabetical for those with same rating)
select movies.title, ratings.rating from movies join ratings on movies.id = ratings.movie_id where movies.year = 2010 order by ratings.rating desc,  movies.title;
