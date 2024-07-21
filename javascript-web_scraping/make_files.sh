#!/usr/bin/bash

files=(
"0-readme.js"
"1-writeme.js"
"2-statuscode.js"
"3-starwars_title.js"
"4-starwars_count.js"
"5-request_store.js"
"6-completed_tasks.js"
"100-starwars_characters.js"
"101-starwars_characters.js"
)

for file in "${files[@]}"
do
  touch "$file"
  chmod +x "$file"
  echo '#!/usr/bin/node' > "$file"
done

