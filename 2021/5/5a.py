#!/usr/bin/python3

import sys
import re

class Hit(Exception):
    pass

class D(Exception):
    print("Error")
    pass

infile = open(sys.argv[1], 'r')

#nums = [int(x) for x in infile.readline().strip().split(',')]

#print(nums)

field = [[0] * 1000 for i in range(1000)]

with infile:
    while True:
        row = infile.readline().strip()
        if not row:
            break
        parsed = re.search('(\d+),(\d+) -> (\d+),(\d+)' ,row)
        x1 = int(parsed.group(1))
        y1 = int(parsed.group(2))
        x2 = int(parsed.group(3))
        y2 = int(parsed.group(4))
        print(x1, y1, x2, y2)
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                field[y][x1] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                field[y1][x] += 1
        else:
            pass
            #raise D

ans = sum([1 if field[y][x] >= 2 else 0 for y in range(1000) for x in range(1000)])

for y in range(10):
    for x in range(10):
        print(field[y][x], end = "")
    print()

print(ans)



#data1 = [line.strip() for line in open(sys.argv[1], 'r')]
#data0 = data1.copy()
#
#idx = 0
#while len(data1) > 1:
#    ones  = len([num[idx] for num in data1 if num[idx] == "1"])
#    zeros = len([num[idx] for num in data1 if num[idx] == "0"])
#    data1 = list(filter(lambda x: x[idx] == ("1" if ones >= zeros else "0"), data1))
#    idx += 1
#
#idx = 0
#while len(data0) > 1:
#    ones  = len([num[idx] for num in data0 if num[idx] == "1"])
#    zeros = len([num[idx] for num in data0 if num[idx] == "0"])
#    data0 = list(filter(lambda x: x[idx] == ("0" if zeros <= ones else "1"), data0))
#    idx += 1
#
#print(int(data0[0], 2) * int(data1[0], 2))

