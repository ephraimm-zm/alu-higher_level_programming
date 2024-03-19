#!/usr/bin/python3
"""
Script reads log entries from stdin and calculates various items
"""


import sys


total_file_size = 0
status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        file_size = int(parts[-1])
        status_code = int(parts[-2])
        total_file_size += file_size

        if status_code in status_codes:
            status_codes[status_code] += 1

        if line_count % 10 == 0:
            print(f"File size: {total_file_size}")
            for code, count in status_codes.items():
                print(f"{code}: {count}")
