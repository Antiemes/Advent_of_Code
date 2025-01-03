#!/usr/bin/env python3

import sys
from functools import lru_cache

tast = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], [None, '0', 'A']]

lrusize = 128
lrusize2 = 16384

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

def tpos(f):
    global tast

    h = len(tast)
    w = len(tast[0])

    for y in range(h):
        for x in range(w):
            if tast[y][x] == f:
                return x, y
    return

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

@lru_cache(maxsize=lrusize2)
def getcost(p, level):
    if level == 0:
        return min([len(x) for x in dp[p]])
    j = None
    for c in dp[p]:
        s = 0
        for f in zip('A' + c, c):
            s += getcost(f, level - 1)
        if j == None or s < j:
            j = s
    return j

dpad = [[None, '^', 'A'], ['<', 'v', '>']]

"""
 ^A
<v>
"""

dp = {}

dp[('A', 'A')] = ["A"]
dp[('A', '^')] = ["<A"]
dp[('A', 'v')] = ["<vA", "v<A"]
dp[('A', '<')] = ["v<<A", "<v<A"]
dp[('A', '>')] = ["vA"]

dp[('^', 'A')] = [">A"]
dp[('^', '^')] = ["A"]
dp[('^', 'v')] = ["vA"]
dp[('^', '<')] = ["v<A"]
dp[('^', '>')] = ["v>A", ">vA"]

dp[('v', '^')] = ["^A"]
dp[('v', 'v')] = ["A"]
dp[('v', 'A')] = [">^A", "^>A"]
dp[('v', '<')] = ["<A"]
dp[('v', '>')] = [">A"]

dp[('<', '^')] = [">^A"]
dp[('<', 'v')] = [">A"]
dp[('<', 'A')] = [">>^A", ">^>A"]
dp[('<', '<')] = ["A"]
dp[('<', '>')] = [">>A"]

dp[('>', '^')] = ["<^A", "^<A"]
dp[('>', 'v')] = ["<A"]
dp[('>', '<')] = ["<<A"]
dp[('>', '>')] = ["A"]
dp[('>', 'A')] = ["^A"]

in_fn = sys.argv[1]

ans = 0

robots = 25

with open(in_fn, 'r') as data:
    for line in data:
        code = line.rstrip('\n')
        print(f'{code}: ', end="")
        
        i = int(code[:-1])

        dcombs = []
        c = None
        for tcomb in getalltcombs('A', code):
            #print(tcomb)
            s = 0
            for p in zip('A' + tcomb, tcomb):
                s += getcost(p, robots - 1)
            if c == None or s < c:
                c = s
        print(c)
        ans += c * i

print(ans)

#zz = "<A^A>^^AvvvA"
#zzz = zip("A" + zz, zz)
#
#aa = 0
#for p in zzz:
#    a = getcost(p, 1)
#    aa += a
#    print(f'p: {p}: {a}')
#
#print(aa)
