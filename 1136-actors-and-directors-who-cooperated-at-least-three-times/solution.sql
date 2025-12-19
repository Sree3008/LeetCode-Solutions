# Write your MySQL query statement below
select actor_id,director_id from 
actordirector 
GROUP BY actor_id, director_id
having 
count(*)>=3;
