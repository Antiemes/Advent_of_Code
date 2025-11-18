#!/usr/bin/env python3

import sys
import string
import re

monkeys = []

in_fn = sys.argv[1]

data = open(in_fn, 'r')

megadiv = 1

for line in data:
    line = line.rstrip("\n")
    if match := re.search(r'^Monkey (\d+):$', line):
        beh = {}
        #print(match.group(1))
        
        match = re.search(r'Starting items: (.*)$', data.readline().rstrip("\n"))
        beh["items"] = [int(x) for x in match.group(1).split(", ")]

        match = re.search(r'Operation: new = old (.) (\w+)$', data.readline().rstrip("\n"))
        beh["op"] = match.group(1)
        beh["opb"] = match.group(2)

        match = re.search(r'Test: divisible by (\d+)$', data.readline().rstrip("\n"))
        beh["div"] = int(match.group(1))
        megadiv *= beh["div"]

        match = re.search(r'If true: throw to monkey (\d+)$', data.readline().rstrip("\n"))
        beh["true"] = int(match.group(1))
        
        match = re.search(r'If false: throw to monkey (\d+)$', data.readline().rstrip("\n"))
        beh["false"] = int(match.group(1))
        
        beh["inspected"] = 0

        monkeys.append(beh)

#for i, monkey in enumerate(monkeys):
#    print(f'Monkey {i}: ' + ", ".join([str(x) for x in monkey["items"]]))
#print()

for round in range(10000):
    for i, monkey in enumerate(monkeys):
        #print(f'Monkey {i}')
        items = monkey.pop("items")
        monkey["items"] = []
        for item in items:
            monkey["inspected"] += 1
            opb = monkey["opb"]
            if opb == "old":
                opb = str(item)
            res = eval(str(item) + monkey["op"] + opb)
            res %= megadiv
            if res % monkey["div"] == 0:
                target = monkey["true"]
            else:
                target = monkey["false"]
    
            monkeys[target]["items"].append(res)
            #print(f'{item} : {res} -> {target}')

insp = []
for i, monkey in enumerate(monkeys):
    #print(f'Monkey {i}: ' + ", ".join([str(x) for x in monkey["items"]]))
    print(f'Monkey {i}: {monkey["inspected"]}')
    insp.append(monkey["inspected"])

insp.sort()
print(insp[-1] * insp[-2])

