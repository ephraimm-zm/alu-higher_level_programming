#!/bin/bash

# Define array of file names
files=(
0-privileges.sql
1-create_user.sql
2-create_read_user.sql
3-force_name.sql
4-never_empty.sql
5-unique_id.sql
6-states.sql
7-cities.sql
8-cities_of_california_subquery.sql
9-cities_by_state_join.sql
10-genre_id_by_show.sql
11-genre_id_all_shows.sql
12-no_genre.sql
13-count_shows_by_genre.sql
14-my_genres.sql
15-comedy_only.sql
16-shows_by_genre.sql
100-not_my_genres.sql
101-not_a_comedy.sql
102-rating_shows.sql
103-rating_genres.sql
)

# Loop through the array and create files
for file in "${files[@]}"
do
    touch "$file"  # Create empty file
    echo "--" > "$file"  # Add comment to the file
done

