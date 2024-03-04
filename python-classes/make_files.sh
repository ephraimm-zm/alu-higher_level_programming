#!/bin/bash
names=(
    "0-square.py"
    "1-square.py"
    "2-square.py"
    "3-square.py"
    "4-square.py"
    "5-square.py"
    "6-square.py"
    "100-singly_linked_list.py"
    "101-square.py"
    "102-square.py"
    "103-magic_class.py"
)

for name in "${names[@]}"
do
    touch "$name"
    chmod +x "$name"
    echo "#!/usr/bin/python3" >> "$name"
done
