#!/usr/bin/python3

import sys
import re

class Hit(Exception):
    pass

infile = open(sys.argv[1], 'r')

agesl = [int(x) for x in infile.readline().strip().split(',')]

ages = {i : len([age for age in agesl if age == i]) for i in range(8 + 1)}

for day in range(1, 256 + 1):
    cur = ages.copy()
    for i in range(7 + 1):
        ages[i] = cur[i + 1]
    ages[6] += cur[0]
    ages[8] = cur[0]
    #print(f'After {day} days:', end=" ")
    for age, x in ages.items():
        pass
        #print(f'{age}: {x}', end=",")
    #print()

ans = sum(ages.values())
print(ans)
