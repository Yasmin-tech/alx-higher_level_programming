#!/usr/bin/python3
""" a script that reads stdin line by line and for each 10 lines computes:

Total file size: File size: <total size>
        where is the sum of all previous (see input format above)
Number of lines by status code:
        possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear, don’t print anything for this status code
format: <status code>: <number>
status codes are printed in ascending order
"""

import sys

counter = 0
file_size = 0
list_valid_codes = [200, 301, 400, 401, 403, 404, 405, 500]
dict_status_code = {}
try:
    for line in sys.stdin:
        counter += 1

        list_logs = line.split()
        file_size += int(list_logs[-1])
        dict_status_code[list_logs[-2]] = counter

        if counter == 10:
            print("File size: {}".format(file_size))
            for k, v in sorted(dict_status_code.items()):
                if int(k) in list_valid_codes:
                    print("{}: {}".format(k, v))
            counter = 0
            file_size = 0
            dict_status_code = {}
except KeyboardInterrupt:
    print("File size: {}".format(file_size))
    for k, v in sorted(dict_status_code.items()):
        if int(k) in list_valid_codes:
            print("{}: {}".format(k, v), flush=True)
    raise
