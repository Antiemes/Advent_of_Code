#!/usr/bin/env python3

import sys
import string
import re

files = {}
dirs = set()

act_dir = ""

in_fn = sys.argv[1]

data = open(in_fn, 'r')

for line in data:
    line = line.rstrip("\n")
    if line.startswith("$ cd "):
        _, _, directory = line.partition("$ cd ")
        if directory == "/":
            act_dir = ""
        elif directory == "..":
            act_dir = act_dir.rsplit("/", 1)[0]
        else:
            act_dir += ("/" + directory)
            dirs.add(act_dir)
        #print(act_dir)
    elif line == "$ ls":
        pass
    else:
        #print(act_dir)
        size, fn = line.split(" ")
        #print(line)
        #print(" " + size + ", " + fn)
        if size == "dir":
            pass
        else:
            files[act_dir + "/" + fn] = int(size)

#for fn, size in files.items():
#    print(fn, size)

ans = 0

for directory in dirs:
    s = 0
    print(directory)
    for file, size in files.items():
        if file.startswith(directory + "/"):
            s += size
    print("    " + str(s))
    if s <= 100000:
        ans += s

print(ans)

