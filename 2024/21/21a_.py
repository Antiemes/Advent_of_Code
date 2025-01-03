#!/usr/bin/env python3

import sys
from functools import lru_cache

tast = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], [None, '0', 'A']]

lrusize = 128

@lru_cache(maxsize=lrusize)
def alltcombs(pos, target):
    global tast
    (x, y) = pos
    (xt, yt) = target
    h = len(tast)
    w = len(tast[0])
    if pos == target:
        return [""]
    else:
        combl = []
        for xo, yo, d in [(1, 0, '>'), (-1, 0, '<'), (0, 1, 'v'), (0, -1, '^')]:
            xa = x + xo
            ya = y + yo
            if xa < 0 or xa >= w or ya < 0 or ya >= h or tast[ya][xa] is None:
                continue
            if abs(xa - xt) > abs (x - xt):
                continue
            if abs(ya - yt) > abs (y - yt):
                continue
            for comb in alltcombs((xa, ya), target):
                combl.append(d + comb)
        return combl

@lru_cache(maxsize=lrusize)
def tpos(f):
    global tast

    h = len(tast)
    w = len(tast[0])

    for y in range(h):
        for x in range(w):
            if tast[y][x] == f:
                return x, y
    return

@lru_cache(maxsize=lrusize)
def getalltcombs(sf, s):
    if len(s) == 0:
        return([""])
    st = s[0]
    sr = s[1:]

    ll = []
    for comb in alltcombs(tpos(sf), tpos(st)):
        for z in getalltcombs(st, sr):
            ll.append(comb + 'A' + z)
    return ll

dpad = [['None', '^', 'A'], ['<', 'v', '>']]

@lru_cache(maxsize=lrusize)
def alldcombs(pos, target):
    global dpad
    (x, y) = pos
    (xt, yt) = target
    h = len(dpad)
    w = len(dpad[0])
    if pos == target:
        return [""]
    else:
        combl = []
        for xo, yo, d in [(1, 0, '>'), (-1, 0, '<'), (0, 1, 'v'), (0, -1, '^')]:
            xa = x + xo
            ya = y + yo
            if xa < 0 or xa >= w or ya < 0 or ya >= h or dpad[ya][xa] is None:
                continue
            if abs(xa - xt) > abs (x - xt):
                continue
            if abs(ya - yt) > abs (y - yt):
                continue
            for comb in alldcombs((xa, ya), target):
                combl.append(d + comb)
        return combl

@lru_cache(maxsize=lrusize)
def dpos(f):
    global dpad

    h = len(dpad)
    w = len(dpad[0])

    for y in range(h):
        for x in range(w):
            if dpad[y][x] == f:
                return x, y
    return

@lru_cache(maxsize=lrusize)
def getalldcombs(sf, s):
    if len(s) == 0:
        return([""])
    st = s[0]
    sr = s[1:]

    ll = []
    for comb in alldcombs(dpos(sf), dpos(st)):
        for z in getalldcombs(st, sr):
            ll.append(comb + 'A' + z)
    return ll



in_fn = sys.argv[1]

ans = 0

with open(in_fn, 'r') as data:
    for line in data:
        code = line.rstrip('\n')
        print(f'{code}: ', end="")
        
        i = int(code[:-1])

        dcombs = []
        for tcomb in getalltcombs('A', code):
            dcombs += getalldcombs('A', tcomb)

        minl = min(len(x) for x in dcombs)
        for i, comb in enumerate(dcombs):
            if len(comb) > minl:
                del(dcombs[i])
                print(f'del: {comb}')
        
        mll = []
        for dcomb in dcombs:
            dcombs2 = getalldcombs('A', dcomb)
            ml = min([len(x) for x in dcombs2])
            mll.append(ml)
        ml = min(mll)
        
        print(f'{ml} * {i}')
        ans += i * ml

print(ans)


#        ml = min(len(x) for x in ac)
#        mlc = [x for x in ac if len(x) == ml]

