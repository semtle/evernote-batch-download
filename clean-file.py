#!/usr/bin/python3

import sys
import os

def good_name_fn(name, badlist):
    for badname in badlist:
        if badname in name or name == "" or name == "\n":
            return False
    return True

def main():
    print("In main.")
    install_dir = os.path.expanduser('~')
    out_filename = install_dir + '/evernote/notebooks.txt'
    in_filename = install_dir + '/evernote/notebooks-dirty.txt'

    badline_list = ["spawn geeknote notebook-list",
                    "Total found:",
                    "Connect to Evernote...",
                    "-- More --",]

    with open(out_filename, 'w') as outfile:
        print("Opened outfile.")
        with open(in_filename, 'r') as infile:
            print("Opened infile.")
            for name in infile.readlines():
                stripped = name.rstrip()
                if good_name_fn(stripped, badline_list):
                    indx = stripped.find(':')
                    indx += 2
                    outname = stripped[indx:]
                    if "/" in outname:
                        outname = outname.replace("/", "-")
                    print("Writing " + outname + " to file.")
                    outfile.write(outname + "\n")


if __name__ == '__main__':
    print("Under if.")
    main()
