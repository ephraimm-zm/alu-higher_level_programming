#!/usr/bin/bash

# Define the array of filenames
files=(
"0-rectangle.js"
"1-rectangle.js"
"2-rectangle.js"
"3-rectangle.js"
"4-rectangle.js"
"5-square.js"
"6-square.js"
"7-occurrences.js"
"8-esrever.js"
"9-logme.js"
"10-converter.js"
"100-map.js"
"101-sorted.js"
"102-concat.js"
)

# Loop through each file in the array
for file in "${files[@]}"
do
  # Create an empty file
  touch "$file"
  # Write the shebang line to the file
  echo "#!/usr/bin/node" > "$file"
  # Make the file executable
  chmod +x "$file"
done

