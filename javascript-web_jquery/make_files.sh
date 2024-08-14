#!/bin/bash

for i in {0..9}
do
    filename="${i}-script.js"
    touch "$filename"
    chmod +x "$filename"
    echo "#!/usr/bin/node" > "$filename"
done
