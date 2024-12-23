#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

program = []

regA = 0
regB = 0
regC = 0

foo = 0

def combo(c):
    print(regA, regB, regC)
    if c == 4:
        return regA
    elif c == 5:
        return regB
    elif c == 6:
        return regC
    else:
        return c

def run_prg():
    print(foo)
    IP = 0
    try:
        while True:
            opcode = program[IP]
            operand = program[IP+1]
            print("zz", IP, opcode)
            if opcode == 0: # adv
                print(regA)
                regA = regA // (2 ** combo(operand))
                print(regA)
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


with open(in_fn, 'r') as data:
    regA_init = int(data.readline().rstrip('\n').split(" ")[2])
    regB_init = int(data.readline().rstrip('\n').split(" ")[2])
    regC_init = int(data.readline().rstrip('\n').split(" ")[2])
    data.readline()
    programS = data.readline().rstrip('\n')
    program = [int(x) for x in programS.split(" ")[1].split(",")]

print(regA_init, regB_init, regC_init)
regA = 30899381
regB = 0
regC = 0

print(program)

print()
run_prg()


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

