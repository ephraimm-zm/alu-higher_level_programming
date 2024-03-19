#!/usr/bin/python3
"""
Script for task 14
"""

import sys

def process_log(lines):
    """
    Process the log lines and compute total file size and status code counts for a batch.

    Args:
        lines (list): List of log lines to process.

    Returns:
        tuple: A tuple containing the total file size and a dictionary of status code counts for the batch.
    """
    total_file_size = 0
    status_counts = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}

    for line in lines:
        parts = line.split()
        if len(parts) >= 7:
            file_size = int(parts[-1])
            total_file_size += file_size
            status_code = parts[-2]
            if status_code in status_counts:
                status_counts[status_code] += 1
    

def print_stats(total_file_size, status_counts):
    """
    Print the statistics for status codes with counts greater than 0.

    Args:
        total_file_size (int): Total size of files.
        status_counts (dict): Dictionary containing counts of different status codes.
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
    lines = []

    try:
        for line in sys.stdin:
            lines.append(line.strip())
            if len(lines) == 10:
                total_file_size, status_counts = process_log(lines)
                print_stats(total_file_size, status_counts)
                lines = []
    except KeyboardInterrupt:
        pass

    # Print statistics for the remaining lines if there are any
    if lines:
        total_file_size, status_counts = process_log(lines)
        print_stats(total_file_size, status_counts)

if __name__ == "__main__":
    main()
