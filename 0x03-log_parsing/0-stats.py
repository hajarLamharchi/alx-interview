#!/usr/bin/python3
"""This script reads lines from stdin in this format
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
and after every 10 lines or keyboard interruption
it prints File size: <total size>
<status code>: <number> for every status code"""

from sys import stdin
"""import re


def valid_format(line):"""
"""This function checks if the input line matches the pattern"""
"""L = re.compile(
        r'^(\d+\.\d+\.\d+\.\d+) - '
        r'\[([^\]]+)\] "GET /projects/260 HTTP/1\.1" '
        r'(\d+) (\d+)$'
        )
    matches = L.match(line)
    if matches:
        return True
    return False"""


try:
    my_dict = {}
    total_size = 0
    for i, line in enumerate(stdin, start=1):
        line = line.strip()
        """if not valid_format(line):
            continue"""
        parts = line.split(" ")
        total_size += int(parts[-1])
        if parts[-2] not in my_dict:
            my_dict[parts[-2]] = 1
        else:
            my_dict[parts[-2]] += 1
        my_dict = dict(sorted(my_dict.items()))
        if i % 10 == 0:
            print("File size: {}".format(total_size))
            for key, val in my_dict.items():
                print("{}: {}".format(key, val))
except Exception as e:
    pass
finally:
    print("File size: {}".format(total_size))
    for key, val in my_dict.items():
        print("{}: {}".format(key, val))
