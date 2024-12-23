#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

regA = 0
regB = 0
regC = 0
program = []
IP = 0

def combo(c):
    if c == 4:
        return regA
    elif c == 5:
        return regB
    elif c == 6:
        return regC
    else:
        return c

with open(in_fn, 'r') as data:
    regA = int(data.readline().rstrip('\n').split(" ")[2])
    regB = int(data.readline().rstrip('\n').split(" ")[2])
    regC = int(data.readline().rstrip('\n').split(" ")[2])
    data.readline()
    program = [int(x) for x in data.readline().rstrip('\n').split(" ")[1].split(",")]


print(regA, regB, regC)
print(program)

try:
    while True:
        opcode = program[IP]
        operand = program[IP+1]
        if opcode == 0: # adv
            regA = regA // (2 ** combo(operand))
            IP += 2
        elif opcode == 1: #bxl
            regB = regB ^ operand
            IP += 2
        elif opcode == 2: #bst
            regB = combo(operand) % 8
            IP += 2
        elif opcode == 3: #jnz
            if regA == 0:
                IP += 2
            else:
                IP = operand
        elif opcode == 4: #bxc
            regB = regB ^ regC
            IP += 2
        elif opcode == 5: #out
            print(combo(operand) % 8, end=",")
            IP += 2
        elif opcode == 6: #bdv
            regB = regA // (2 ** combo(operand))
            IP += 2
        elif opcode == 7: #cdv
            regC = regA // (2 ** combo(operand))
            IP += 2
except IndexError:
    pass

print()

"""
2, 4   bst
1, 1   bxl
7, 5   cdv
4, 0   bxc
0, 3   adv
1, 6   bxl
5, 5   out
3, 0   jnz
"""

