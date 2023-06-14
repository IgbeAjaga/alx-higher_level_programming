#!/usr/bin/python3
"""
reads stdin line by line and computes metrics
"""
import sys


def print_stats(total_size, status_codes):
    """Prints the computed statistics"""
    print("File size: {:d}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{:s}: {:d}".format(code, status_codes[code]))

def parse_line(line):
    """Parses a line and extracts relevant information"""
    line_parts = line.split()
    size = int(line_parts[-1])
    code = line_parts[-2]
    return size, code

def compute_metrics():
    """Reads stdin line by line and computes metrics"""
    total_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            size, code = parse_line(line)
            total_size += size

            if code in status_codes:
                status_codes[code] += 1

            if count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

compute_metrics()

