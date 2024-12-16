#!/usr/bin/env python3

import sys
import re

in_fn = sys.argv[1]

#Button A: X+94, Y+34
#Button B: X+22, Y+67
#Prize: X=8400, Y=5400

#ax + by = v
#cx + dy = w

tokens = 0


with open(in_fn, 'r') as data:
    while True:
        linea = data.readline().rstrip('\n')
        if len(linea) == 0:
            break
        lineb = data.readline().rstrip('\n')
        linep = data.readline().rstrip('\n')
        #(xa, ya) = re.findall(r" X\(.'\d+\), \(\)", linea)
        (a, c) = re.findall(r"X\+?(-?\d+), Y\+?(-?\d+)$", linea)[0]
        (b, d) = re.findall(r"X\+?(-?\d+), Y\+?(-?\d+)$", lineb)[0]
        (v, w) = re.findall(r"X=(\d+), Y=(\d+)$", linep)[0]
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        v = int(v)
        w = int(w)
        print(a, b)
        print(c, d)
        print(v, w)
        D = 1 / (a * d - b * c)
        Ia = D * d
        Ib = D * (-b)
        Ic = D * (-c)
        Id = D * a
        
        x1f = Ia * v + Ib * w
        x2f = Ic * v + Id * w
       
        x1 = int(round(x1f))
        x2 = int(round(x2f))

        print(x1, x2)
        if x1 * a + x2 * b == v and x1 * c + x2 * d == w:
            print(f"GOOD, {x1}, {x2}")
            tokens += 3 * x1 + x2
        else:
            print("NO")


        #if xa*yb == ya*xb:
        #    print("FOO")
        data.readline()
        print()

print(tokens)

