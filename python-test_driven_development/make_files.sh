#!/bin/bash

files=(
0-add_integer.py
0-add_integer.txt
2-matrix_divided.py
2-matrix_divided.txt
3-say_my_name.py
3-say_my_name.txt
4-print_square.py
4-print_square.txt
5-text_indentation.py
5-text_indentation.txt
100-matrix_mul.py
100-matrix_mul.txt
101-lazy_matrix_mul.py
101-lazy_matrix_mul.txt
)

for file in "${files[@]}"; do
    if [[ $file == *.py ]]; then
        if [[ ! -e $file ]]; then
            touch "$file"
            echo '#!/usr/bin/python3' > "$file"
            chmod +x "$file"
        fi
    elif [[ $file == *.txt ]]; then
        touch "tests/$file"
    fi
done

touch 6-max_integer_test.py
chmod +x 6-max_integer_test.py
echo '#!/usr/bin/python3' > 6-max_integer_test.py
