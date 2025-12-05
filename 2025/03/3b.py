#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

pos = 50
zeros = 0

ans = 0

with open(in_fn, 'r') as data:
    for line in data:
        line = [int(x) for x in line.rstrip("\n")]
        left = 0
        num = ""
        for i in range(12):
            st = line[left:len(line) - (11 - i)]
            x = max(st)
            ix = st.index(x) + left
            left = ix + 1
            #print(f'{x}', end="")
            num += str(x)

        print(num)
        ans += int(num, 10)

print(ans)
