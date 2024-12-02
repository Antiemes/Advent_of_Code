#!/usr/bin/python3

import sys

data1 = [line.strip() for line in open(sys.argv[1], 'r')]
data0 = data1.copy()

idx = 0
while len(data1) > 1:
    ones  = len([num[idx] for num in data1 if num[idx] == "1"])
    zeros = len([num[idx] for num in data1 if num[idx] == "0"])
    data1 = list(filter(lambda x: x[idx] == ("1" if ones >= zeros else "0"), data1))
    idx += 1

idx = 0
while len(data0) > 1:
    ones  = len([num[idx] for num in data0 if num[idx] == "1"])
    zeros = len([num[idx] for num in data0 if num[idx] == "0"])
    data0 = list(filter(lambda x: x[idx] == ("0" if zeros <= ones else "1"), data0))
    idx += 1

print(int(data0[0], 2) * int(data1[0], 2))

