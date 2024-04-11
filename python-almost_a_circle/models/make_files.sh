#!/bin/bash

models_files=(
base.py
__init__.py
rectangle.py
square.py
)

for file in "${models_files[@]}"; do
    touch "$file"
    chmod +x "$file"
    echo "#!/usr/bin/python3" >> "$file"
done
