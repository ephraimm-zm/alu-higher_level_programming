#!/bin/bash

files=(
0-select_states.py
1-filter_states.py
2-my_filter_states.py
3-my_safe_filter_states.py
4-cities_by_state.py
5-filter_cities.py
model_state.py
7-model_state_fetch_all.py
8-model_state_fetch_first.py
9-model_state_filter_a.py
10-model_state_my_get.py
11-model_state_insert.py
12-model_state_update_id_2.py
13-model_state_delete_a.py
14-model_city_fetch_by_state.py
relationship_city.py
relationship_state.py
100-relationship_states_cities.py
101-relationship_states_cities_list.py
102-relationship_cities_states_list.py
)

for file in "${files[@]}"; do
    touch "$file"
    echo "$file created"
    chmod +x "$file"
    echo "$file given execute permissions"
    echo "#!/usr/bin/python3" >> "$file"
    echo "Added shebang to $file"
done


