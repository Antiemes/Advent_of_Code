#!/usr/bin/python3

import sys

file1 = open(sys.argv[1], 'r')
depth = 0
aim = 0
horiz = 0

line = file1.readline()
ones  = [0]*len(line.strip())
zeros = [0]*len(line.strip())
file1.seek(0)

while True:
    line = file1.readline()
    
    if not line:
        break
#    print("Line{}: {}".format(count, line.strip()))
    line=line.strip()
    for i in range(len(line)):
        match(line[i]):
            case '0':
                zeros[i] += 1
            case '1':
                ones[i] += 1

file1.close()

num1 = 0
num2 = 0

for i in range(len(ones)):
    num1 *= 2
    num1 += 1 if (ones[i] > zeros[i]) else 0
    num2 *= 2
    num2 += 1 if (ones[i] < zeros[i]) else 0

print(num1 * num2)
#print(horiz * depth)

