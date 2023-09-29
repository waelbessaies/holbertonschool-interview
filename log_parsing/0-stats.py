#!/usr/bin/python3
"""Write a script that reads stdin line by line and computes metrics:"""

import sys

STATUS_CODES = {'200': 0,
                '301': 0, '400': 0,
                '401': 0, '403': 0,
                '404': 0, '405': 0,
                '500': 0}

total_size = 0
number_of_lines = 0


def print_status_code(total_size):
    print("File size: {:d}".format(total_size))
    for key, value in sorted(STATUS_CODES.items()):
        if value != 0:
            print("{}: {:d}".format(key, value))


try:
    for arg in sys.stdin:
        values = arg.split(" ")
        if len(values) > 2:
            status_code = values[-2]
            file_size = values[-1]

            if status_code in STATUS_CODES:
                STATUS_CODES[status_code] += 1

            total_size += int(file_size)
            number_of_lines += 1

            if number_of_lines == 10:
                print_status_code(total_size)
                number_of_lines = 0

except KeyboardInterrupt:
    pass
finally:
    print_status_code(total_size)
