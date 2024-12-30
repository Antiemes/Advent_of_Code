#!/usr/bin/env python3

import sys

tast = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], [None, '0', 'A']]

def tastpos(f):
    global tast

    h = len(tast)
    w = len(tast[0])

    for y in range(h):
        for x in range(w):
            if tast[y][x] == f:
                return x, y
    return

def tastize(st):
    global tast
    (x, y) = tastpos('A')

    moves = ''
    
    for s in st:
        (xt, yt) = tastpos(s)


        h = len(tast)
        w = len(tast[0])

        while (x, y) != (xt, yt):
            if yt < y and tast[y - 1][x] is not None:
                y -= 1
                moves += '^'
            elif xt > x and tast[y][x + 1] is not None:
                x += 1
                moves += '>'
            elif yt > y and tast[y + 1][x] is not None:
                y += 1
                moves += 'v'
            elif xt < x and tast[y][x - 1] is not None:
                x -= 1
                moves += '<'
        moves += 'A'

    return moves


dpad = [['None', '^', 'A'], ['<', 'v', '>']]

def dpos(f):
    global dpad

    h = len(dpad)
    w = len(dpad[0])

    for y in range(h):
        for x in range(w):
            if dpad[y][x] == f:
                return x, y
    return

def dpadize(st):
    global dpad
    (x, y) = dpos('A')

    moves = ''
    
    for s in st:
        (xt, yt) = dpos(s)


        h = len(dpad)
        w = len(dpad[0])

        while (x, y) != (xt, yt):
            if yt > y and dpad[y + 1][x] is not None:
                y += 1
                moves += 'v'
            elif yt < y and dpad[y - 1][x] is not None:
                y -= 1
                moves += '^'
            elif xt < x and dpad[y][x - 1] is not None:
                x -= 1
                moves += '<'
            elif xt > x and dpad[y][x + 1] is not None:
                x += 1
                moves += '>'
        moves += 'A'

    return moves


in_fn = sys.argv[1]

ans = 0
with open(in_fn, 'r') as data:
    for line in data:
        code = line.rstrip('\n')
        i = int(code[:-1])
        q = len(dpadize(dpadize(tastize(code))))
        print(i, q)
        ans += i * q

print(ans)

print(tastize('379A'))

print(dpadize(dpadize('^A<<^^A')))
print(dpadize(dpadize('^A^^<<A')))

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
