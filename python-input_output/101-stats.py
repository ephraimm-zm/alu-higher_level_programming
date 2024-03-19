#!/usr/bin/bash
import sys
from collections import defaultdict

def compute_metrics(lines):
    """
    Compute metrics from a list of log lines.

    Args:
        lines (list): List of log lines.

    Returns:
        tuple: A tuple containing total file size and status code counts.
    """
    total_file_size = 0
    status_counts = defaultdict(int)

    for line in lines:
        parts = line.split()
        if len(parts) >= 9:
            status_code = parts[8]
            total_file_size += int(parts[9])
            status_counts[status_code] += 1

    return total_file_size, status_counts

def print_metrics(total_file_size, status_counts):
    """
    Print computed metrics.

    Args:
        total_file_size (int): Total file size.
        status_counts (dict): Counts of status codes.
    """
    print("Total file size:", total_file_size)
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")

def main():
    """
    Main function to read input, compute metrics, and print them.
    """
    lines = []
    try:
        for line in sys.stdin:
            lines.append(line.strip())
            if len(lines) % 10 == 0:
                total_file_size, status_counts = compute_metrics(lines)
                print_metrics(total_file_size, status_counts)
                lines = []
    except KeyboardInterrupt:
        total_file_size, status_counts = compute_metrics(lines)
        print_metrics(total_file_size, status_counts)

if __name__ == "__main__":
    main()
