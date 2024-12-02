#!/usr/bin/python3

import sys

class Hit(Exception):
    pass

infile = open(sys.argv[1], 'r')

nums = [int(x) for x in infile.readline().strip().split(',')]

#print(nums)

winscore = 0
winsteps = 0

with infile:
    while True:
        if not infile.readline():
            break
        table = [[]] * 5
        for y in range(5):
            table[y] = [int(x) for x in infile.readline().strip().split()]

        hit = [[0] * 5 for i in range(5)]
        steps = 0
        try:
            for idx, num in enumerate(nums):
                for y in range(5):
                    for x in range(5):
                        if table[y][x] == num:
                            hit[y][x] = 1
                            if all(hit[y][i] == 1 for i in range(5)):
                                print("BINGO", idx, num)
                                raise Hit
                            if all(hit[i][x] == 1 for i in range(5)):
                                print("BINGO", idx, num)
                                raise Hit
                steps += 1
        except Hit:
            if steps > winsteps:
                print("!!")
                winsteps = steps
                winscore = sum([table[y][x] if (hit[y][x] == 0) else 0 for y in range(5) for x in range(5)]) * num
            

print(winscore, winsteps)



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

