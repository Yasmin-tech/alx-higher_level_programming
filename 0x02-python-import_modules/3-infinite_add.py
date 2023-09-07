#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    list_argv = argv[1:]
    sum = 0
    for ar in list_argv:
        sum += int(ar)
    print(sum)
