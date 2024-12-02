#!/usr/bin/python3

import sys

file1 = open(sys.argv[1], 'r')
depth = 0
aim = 0
horiz = 0
while True:
    line = file1.readline()
    
    if not line:
        break
#    print("Line{}: {}".format(count, line.strip()))
    [direction, value] = line.split()
    value=int(value)
    match(direction):
        case 'down':
            aim += value
    match(direction):
        case 'up':
            aim -= value
    match(direction):
        case 'forward':
            horiz += value
            depth += value * aim

file1.close()
print(horiz * depth)

