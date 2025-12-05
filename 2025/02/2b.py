#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

arr = []
invalids = set()

def check(start, end):
    #start = '113'
    #end = '345345236'
    
    """
    113-999
    1000-9999
    10000-99999
    100000-999999
    1000000-9999999
    10000000-99999999
    100000000-345345236
    """
    
    for l in range(len(start), len(end) + 1):
        if l == len(start):
            b = start
        else:
            b = '1' + '0' * (l - 1)
        if l == len(end):
            e = end
        else:
            e = '9' * l
        print(b, e)
        for hl in range(1, len(b) // 2 + 1):
            if len(b) % hl != 0:
                continue
            divisor = len(b) // hl
            for n in range(int(b[:hl]), int(e[:hl]) + 1):
                m = str(n) * divisor
                if int (m) >= int(start) and int(m) <= int(end):
                    invalids.add(int(m))
                    print(f'  {m}, {divisor}, {hl}')


data = open(in_fn, 'r')
line = data.readline().rstrip("\n")
intervals = [tuple(i.split("-")) for i in line.split(",")]
ans = 0
for (start, end) in intervals:
    check(start, end)
    #print(start, end)


print(sum(invalids))

