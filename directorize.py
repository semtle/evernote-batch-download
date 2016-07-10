#!/usr/bin/python3

import sys

def main(args):
    string = args[1]
    if '/' in string:
        string = string.replace('/', '-')
    sys.stdout.write(string)
    sys.exit(0)

if __name__ == "__main__":
    main(sys.argv)
