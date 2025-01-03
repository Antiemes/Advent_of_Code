#!/usr/bin/env python3

import sys
from functools import lru_cache

lrusize = 128

tast = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], [None, '0', 'A']]


@lru_cache(maxsize=lrusize)
def tastpos(f):
    global tast

    h = len(tast)
    w = len(tast[0])

    for y in range(h):
        for x in range(w):
            if tast[y][x] == f:
                return x, y
    return

def tastize(stl):
    global tast
   
    movesll = []
    for st in stl:

        (xs, ys) = tastpos('A')

        movesl = ['']
        
        for s in st:
            (xt, yt) = tastpos(s)
            if xt > xs:
                hc = ">"
            else:
                hc = "<"
            if yt > ys:
                vc = "v"
            else:
                vc = "^"
            nmovesl = []
            xd = abs(xt - xs)
            yd = abs(yt - ys)
            for i, e in enumerate(movesl):
                if xd == 0 or yd == 0:
                    nmovesl.append(e + hc * xd + vc * yd + 'A')
                else:
                    if tast[ys][xt] is not None:
                        nmovesl.append(e + hc * xd + vc * yd + 'A')
                    if tast[yt][xs] is not None:
                        nmovesl.append(e + vc * yd + hc * xd + 'A')
            movesl = nmovesl

            (xs, ys) = (xt, yt)

        movesll += movesl

    ml = min(len(x) for x in movesll)
    #return movesll
    return [x for x in movesll if len(x) == ml]


dpad = [[None, '^', 'A'], ['<', 'v', '>']]

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

def dpadize(stl):
    global dpad
   
    movesll = []
    for st in stl:

        (xs, ys) = dpos('A')

        movesl = ['']
        
        for s in st:
            (xt, yt) = dpos(s)
            if xt > xs:
                hc = ">"
            else:
                hc = "<"
            if yt > ys:
                vc = "v"
            else:
                vc = "^"
            nmovesl = []
            xd = abs(xt - xs)
            yd = abs(yt - ys)
            for i, e in enumerate(movesl):
                #print("OK")
                #print(dpad[ys][xt])
                if xd == 0 or yd == 0:
                    nmovesl.append(e + hc * xd + vc * yd + 'A')
                    #print("??")
                else:
                    if dpad[ys][xt] != None:
                        #print(dpad[ys][xt])
                        nmovesl.append(e + hc * xd + vc * yd + 'A')
                        #print("Rossz")
                    elif dpad[yt][xs] != None:
                        nmovesl.append(e + vc * yd + hc * xd + 'A')
                        #print("Jo")
#                for zzz in nmovesl:
#                    if zzz.startswith('<<vA'):
#                        #print(xs, ys, xt, yt)
#                        #print(dpad[ys][xt])
#                        #print(dpad[yt][xs])
#                        #print(e)
#                        #print(yd, vc, xd, hc)
#                        raise Exception("foo")
            movesl = nmovesl

            (xs, ys) = (xt, yt)

        movesll += movesl

    ml = min(len(x) for x in movesll)
    #return movesll
    return [x for x in movesll if len(x) == ml]


in_fn = sys.argv[1]

nn = {}

"""
 ^A
<v>
"""

dp = {}

dp[('A', 'A')] = "A"
dp[('A', '^')] = "<A"
dp[('A', 'v')] = "<vA"
dp[('A', '<')] = "v<<A"
dp[('A', '>')] = "vA"

dp[('^', 'A')] = ">A"
dp[('^', '^')] = "A"
dp[('^', 'v')] = "vA"
dp[('^', '<')] = "v<A"
dp[('^', '>')] = "v>A"

dp[('v', '^')] = "^A"
dp[('v', 'v')] = "A"
dp[('v', 'A')] = ">^A"
dp[('v', '<')] = "<A"
dp[('v', '>')] = ">A"

dp[('<', '^')] = ">^A"
dp[('<', 'v')] = ">A"
dp[('<', 'A')] = ">>^A"
dp[('<', '<')] = "A"
dp[('<', '>')] = ">>A"

dp[('>', '^')] = "<^A"
dp[('>', 'v')] = "<A"
dp[('>', '<')] = "<<A"
dp[('>', '>')] = "A"
dp[('>', 'A')] = "^A"


#c = dpadize(dpadize(tastize(['029A'])))[0]
#
#print(c)
#print(dpadize([c])[0])
#print(os)

a1 = 0
ans = 0

depth = 4

with open(in_fn, 'r') as data:
    for line in data:
        code = line.rstrip('\n')
        i = int(code[:-1])
        f = dpadize(dpadize(tastize([code])))
        c = f[0]
        
        for o in c:
            a1 += i * len(o)

        pairc = {}
        for a, b in zip('A' + c, c):
            try:
                pairc[(a, b)] += 1
            except KeyError:
                pairc[(a, b)] = 1

        
        for r in range(depth - 2):
            #print(f' Iter: {r}, len: {len(f[0])}')
            f = dpadize(f)
        q = len(f[0])
        #print(f[0])

        for r in range(depth - 2):
            os = ""
            for a, b in zip('A' + c, c):
                os += dp[(a, b)]
            c = os
        
        q2 = len(c)
        
        #print(f'pairc: {pairc}')
        for r in range(depth - 2):
            pcn = {}
            for (a, b) in pairc:
                s = dp[(a, b)]
                #print(r, a, b, s)
                #print(f'  s: {s}')
                for (x, y) in zip('A' + s, s):
                    #print(f'    {x, y}')
                    try:
                        pcn[(x, y)] += pairc[(a, b)]
                    except KeyError:
                        pcn[(x, y)] = pairc[(a, b)]
            pairc = pcn
        q3 = sum(x for k, x in pairc.items())
        
        print(i, q, q2, q3)
        #print(i, q3)
        ans += i * q3

print(a1)
print(ans)

#print(tastize(['379A']))

#for x in dpadize(dpadize(['^A<<^^A>>AvvvA'])):
#    for q in dpadize([x]):
#        print(len(q))
#for x in dpadize(tastize(['379A'])):
#    z=dpadize([x])
#    print(min([len(x) for x in z]))

#print(ans)

#print(tastize(['379A']))
#print(tastize(['029A']))

#print(len(dpadize(dpadize(tastize('379A')))))

#print(dpadize(dpadize('^A<<^^A')))
#print(dpadize(dpadize('^A^^<<A')))

#print(dpadize(dpadize('<^A')))
#print(dpadize(dpadize('^<A')))
#print(dpadize('<^A'))
#print(dpadize('^<A'))

#print(dpadize('Av<AA'))
#print(dpadize('A<AvA'))



"""
789
456
123
 0A

 ^A
<v>

"""

"""

<v<A
>>^A
vA
^A
<vA
<A
A
>>^A
A
vA
<^A
>A
A
vA
^A
<vA
>^A
A
<A
>A
<v<A
>A
>^A
A
A
vA
<^A
>A

<A
>A
v<<A
A
>^A
A
>A
vA
A
^A
<vA
A
A
>^A






"""
