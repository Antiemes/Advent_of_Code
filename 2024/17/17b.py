#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

program = []

def combo(c):
    if c == 4:
        return regA
    elif c == 5:
        return regB
    elif c == 6:
        return regC
    else:
        return c

def run_prg():
    global regA
    global regB
    global regC

    regA = regA_init
    regB = regB_init
    regC = regC_init
    
    IP = 0
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
                print(combo(operand) % 8, end=", ")
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


with open(in_fn, 'r') as data:
    regA_init = int(data.readline().rstrip('\n').split(" ")[2])
    regB_init = int(data.readline().rstrip('\n').split(" ")[2])
    regC_init = int(data.readline().rstrip('\n').split(" ")[2])
    data.readline()
    program = [int(x) for x in data.readline().rstrip('\n').split(" ")[1].split(",")]

print(regA_init, regB_init, regC_init)
print("     ", end="")
print(program)

#regA_init = 0b111_000_010_110_100_010_100_101_101_101_111_110_000_000_000_000

for i in range(8):
#                  15  14  13  12  11  10   9   8   7   6   5   4   3   2   1   0
#                                        *100 010                     010        
#                                        -101 101                     111        
#                                         110 110
    regA_init = 0b111_000_010_110_100_010_101_010_011_110_101_001_100_010_111_010
    regA_init += (i << (3 * 0))
    print(f'{i:03b}', end="   ")
    run_prg()


regA_init = 0b111_000_010_110_100_010_101_010_011_110_101_001_100_010_111_010
run_prg()
print(regA_init)

"""

001
110

2, 4   bst b = a % 8
1, 1   bxl b = b xor 1
7, 5   cdv c = a / b
4, 0   bxc b = b xor c
0, 3   adv a = a / 8
1, 6   bxl b = b xor 6
5, 5   out regB % 8-at kiirja
3, 0   jnz

Az A utolso 3 bitjet iratjuk ki, xor 1, xor (a/b), xor 6
a/b utolso bitje?

"""


