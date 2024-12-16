#!/usr/bin/env python3

import sys

def add_to_dict(d, k, v):
    try:
        d[k] += v
    except KeyError:
        d[k] = v

in_fn = sys.argv[1]

with open(in_fn, 'r') as data:
    for line in data:
        stonesa = [int(x) for x in list(line.rstrip("\n").split(" "))]

stonesd = {}

for stone in stonesa:
    try:
        stonesd[stone] += 1
    except KeyError:
        stonesd[stone] = 1

for it in range(1, 76):
    print()
    print(f"After {it} blinks:")
    stones_c = stonesd.copy()
    for stone in stones_c.keys():
        sstone = str(stone)
        lstone = len(sstone)
        nstone = stones_c[stone]
        if nstone:
            if stone == 0:
                add_to_dict(stonesd, 1, nstone)
                stonesd[0] -= nstone
            elif lstone % 2 == 0:
                a = int(sstone[:lstone // 2])
                b = int(sstone[lstone // 2:])
                stonesd[stone] -= nstone
                add_to_dict(stonesd, a, nstone)
                add_to_dict(stonesd, b, nstone)
                #print(f"{stone} -> {a}, {b} ({nstone})")
                #print(a, stonesd[a])
                #print(b, stonesd[b])
            else:
                #print(f"{stone} -> {stone * 2024} ({nstone})")
                add_to_dict(stonesd, stone * 2024, nstone)
                stonesd[stone] -= nstone
    
    #print(stonesd)

    stones_nr = sum([stonesd[s] for s in stonesd.keys()])
    print(it, stones_nr)
    
    #for stone in stonesd.keys():
    #    pcs = stonesd[stone]
    #    if pcs:
    #        print(f"({stone}, {pcs})", end=" ")
    #print()

#Az 5. lepesnel hianyzik a 2-es. ami a 72-bol jott volna.
