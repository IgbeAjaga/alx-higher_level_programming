#!/usr/bin/python3
"""
reads stdin line by line and computes metrics
"""
import sys


def print_metrics(file_size, status_codes):
    """
    printing the file
    """
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

def parse_line(line, file_size, status_codes):
    """
    parsing the file
    """
    tokens = line.split()
    if len(tokens) > 2:
        file_size += int(tokens[-1])
        status_code = tokens[-2]
        if status_code in status_codes:
            status_codes[status_code] += 1
        else:
            status_codes[status_code] = 1
    return file_size, status_codes

def main():
    """
    main codes
    """
    file_size = 0
    status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            file_size, status_codes = parse_line(line, file_size, status_codes)
            if line_count % 10 == 0:
                print_metrics(file_size, status_codes)
    except KeyboardInterrupt:
        print_metrics(file_size, status_codes)
        raise

if __name__ == "__main__":
    main()
