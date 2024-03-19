#!/usr/bin/python3
"""
Script for task 14
"""

import sys

def process_log(lines):
    """
    Process the log lines and compute totals

    Args:
        lines (list): List of log lines to process.

    Returns:
        tuple: A tuple containing the totals
    """
    total_file_size = 0
    status_counts = {
            '200': 0,
            '301': 0,
            '400': 0,
            '401': 0,
            '403': 0,
            '404': 0,
            '405': 0,
            '500': 0
            }

    for line in lines:
        parts = line.split()
        if len(parts) >= 7:
            file_size = int(parts[-1])
            total_file_size += file_size
            status_code = parts[-2]
            if status_code in status_counts:
                status_counts[status_code] += 1
    
    return total_file_size, status_counts

def print_stats(total_file_size, status_counts):
    """
    Print the statistics including totals.

    Args:
        total_file_size (int): Total size of files.
        status_counts (dict): Dictionary containing totsld
    """
    print(f"File size: {total_file_size}")
    for status_code, count in status_counts.items():
        if count > 0:
            print(f"{status_code}: {count}")

def main():
    """
    Main function to read log lines from standard input, process them, and print statistics.
    """
    total_file_size = 0
    status_counts = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}

    try:
        for line in sys.stdin:
            total_file_size, status_counts = process_log(line.strip(), total_file_size, status_counts)
            if total_file_size > 0:
                print_stats(total_file_size, status_counts)
                total_file_size = 0
                status_counts = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
