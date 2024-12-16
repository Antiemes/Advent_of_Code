#!/usr/bin/python3

import sys
import re

class Hit(Exception):
    pass

infile = open(sys.argv[1], 'r')

ages = [int(x) for x in infile.readline().strip().split(',')]

#print(nums)

for day in range(1, 80 + 1):
    num = len(ages)
    for i in range(num):
        if ages[i] == 0:
            ages[i] = 6
            ages.append(8)
        else:
            ages[i] -= 1
    #print(f'After {day} days:', end=" ")
    for age in ages:
        pass
        #print(age, end=",")
    #print()

ans = len(ages)
print(ans)
