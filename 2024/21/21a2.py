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
                if xd == 0 or yd == 0:
                    nmovesl.append(e + hc * xd + vc * yd + 'A')
                else:
                    if dpad[ys][xt] is not None:
                        nmovesl.append(e + hc * xd + vc * yd + 'A')
                    elif dpad[yt][xs] is not None:
                        nmovesl.append(e + vc * yd + hc * xd + 'A')
            movesl = nmovesl

            (xs, ys) = (xt, yt)

        movesll += movesl

    ml = min(len(x) for x in movesll)
    #return movesll
    return [x for x in movesll if len(x) == ml]


in_fn = sys.argv[1]

ans = 0
with open(in_fn, 'r') as data:
    for line in data:
        code = line.rstrip('\n')
        i = int(code[:-1])
        q = len(dpadize(dpadize(tastize([code])))[0])

        print(i, q)
        ans += i * q

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
