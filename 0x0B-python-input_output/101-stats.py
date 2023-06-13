#!/usr/bin/python3
import sys

def print_metrics(file_size, status_code_counts):
    """Prints the metrics"""
    print("File size: {}".format(file_size))
    for status_code, count in sorted(status_code_counts.items()):
        print("{}: {}".format(status_code, count))

file_size = 0
status_code_counts = {}

try:
    for index, line in enumerate(sys.stdin, start=1):
        tokens = line.split()
        if len(tokens) >= 7:
            status_code = tokens[-2]
            try:
                file_size += int(tokens[-1])
                status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1
            except ValueError:
                pass

        if index % 10 == 0:
            print_metrics(file_size, status_code_counts)

except KeyboardInterrupt:
    print_metrics(file_size, status_code_counts)
