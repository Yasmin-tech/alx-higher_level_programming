#!/usr/bin/python3
count = 0
for i in range(122, 96, -1):
    is_odd = count % 2
    print("{:c}".format(i - 32 if is_odd else i), end="")
    count += 1
