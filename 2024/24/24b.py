#!/usr/bin/env python3

import sys
import re
from functools import lru_cache
import random

in_fn = sys.argv[1]

values = {}
eqs = []

route = {}

def calculate(xn, yn):
    global values
    values = {k: 0 for k, v in values.items() if k[0] in ["x", "y"]}
    eqs_c = eqs.copy()
    
    i = 0
    while xn > 0:
        if xn & 1:
            values["x" + format(i, "02d")] = 1
        xn //= 2
        i += 1
    
    i = 0
    while yn > 0:
        if yn & 1:
            values["y" + format(i, "02d")] = 1
        yn //= 2
        i += 1

    while len(eqs_c) > 0:
        iden1, op, iden2, res = eqs_c[0]
        #resr = route[res]
        resr = res
        eqs_c = eqs_c[1:]
        if iden1 in values and iden2 in values:
            val1 = values[iden1]
            val2 = values[iden2]
            if op == "AND":
                resval = val1 & val2
            elif op == "OR":
                resval = val1 | val2
            elif op == "XOR":
                resval = val1 ^ val2
            else:
                raise Exception("Unknown operator")
            values[resr] = resval
        else:
            eqs_c.append((iden1, op, iden2, res))
    
    res = 0
    for v in sorted(values):
        if v.startswith("z"):
            zidx = int(v[1:])
            res += values[v] * (2 ** zidx)
    return res

def prev(o):
    for iden1, op, iden2, res in eqs:
        if res == o:
            return [iden1, iden2]

def dep(o):
    iset = set()
    if o[0] in ["x", "y"]:
        iset.add(o)
    else:
        for iden1, op, iden2, res in eqs:
            if res == o:
                iset |= dep(iden1)
                iset |= dep(iden2)
                iset.add(res)
    return iset

def gd(g):
    for iden1, op, iden2, res in eqs:
        if res == g:
            print(f'{iden1} {op} {iden2} -> {res}')

def gt(g):
    for iden1, op, iden2, res in eqs:
        if res == g:
            return op


def check(a, b):
    ex = a + b
    c = calculate(a, b)
    if c != ex:
        print(a, b, c, ex)


"""
jmq
qsf

OR
XOR
AND
AND

XOR
OR
AND
AND

AND
XOR
AND
OR

AND
AND

AND
AND
OR
XOR


z13:
OR kapu. Egy XOR-t keresunk, aminek jok a depjei.
Ez a gmh kapu.

z38:
AND kapu. Ehelyett is XOR-t keresunk.

6k+1 dependencyje kell, hogy legyen


A z25-nel akadt el a random kereso.
A z25:
AND
AND
AND
OR

Itt az egyik AND helyett kell XOR

AND-ok:
pww
rkw
rqf

Ennek a XOR-nak tudjuk, hogy az x25 es az y25 a bemenete
Ez a cbd

"""

#route["z06"] = "qsf"
#route["qsf"] = "z06"
route["z06"] = "jmq"
route["jmq"] = "z06"
route["z13"] = "gmh"
route["gmh"] = "z13"
route["z38"] = "qrh"
route["qrh"] = "z38"
route["rqf"] = "cbd"
route["cbd"] = "rqf"

# A z13 a kovetkezo hibas kimenet
# Barmi, aminek az osszege 8192

with open(in_fn, 'r') as data:
    for line in data:
        line = line.rstrip('\n')
        if line == "":
            break
        iden, val = re.findall(r'^(\w+): (\d+)$', line)[0]
        values[iden] = int(val)
    for line in data:
        line = line.rstrip('\n')
        iden1, op, iden2, res = re.findall(r'^(\w+) ([A-Z]+) (\w+) -> (\w+)$', line)[0]
        res = route.setdefault(res, res)
        eqs.append((iden1, op, iden2, res))


#z13 search:
#for iden1, op, iden2, res in eqs:
#    if op == "XOR" and len(dep(res)) == 6 * 13 + 1:
#        print(res)

#z38 search:
#for iden1, op, iden2, res in eqs:
#    if op == "XOR" and len(dep(res)) == 6 * 38 + 1:
#        print(res)

#z25 search:
for iden1, op, iden2, res in eqs:
    if op == "XOR" and iden1[1:] == "25" and iden2[1:] == "25":
        print(res)

#z25 search:
#for i in range(46):
#    g = "z" + format(i, "02d")
#    gd(g)
#    for v in d:
#        if int(v[1:]) > i:
#            print(d, v)

#a = 1
#for b in range(1024):
#    c = calculate(a, b)
#    if c != a + b:
#        print(a, b, c)
#        break

#for a in range(64):
#    for b in range(64):
#        m = 40
#        ex = (a + b) * m
#        if calculate(a * m, b * m) != ex:
#            print(a * m, b * m)

#for b in range(46):
#    d = set()
#    zs = "z" + format(b, "02d")
#    for i in range(b + 1):
#        d.add("x" + format(i, "02d"))
#        d.add("y" + format(i, "02d"))
#    if dep(zs) != d:
#        print(zs)
#        print(d - dep(zs))
#        print(dep(zs) - d)


#
#while True:
#    a = random.randrange(2 ** 45)
#    b = random.randrange(2 ** 45)
#    check(a, b)
#
#for iden1, op, iden2, res in eqs:
#    if iden1 in ["x45", "y45"] or iden2 in ["x45", "y45"]:
#        print(iden1, op, iden2, res)
    #    if not res.startswith("z"):
#        if dep(res) == d:
#            print(res)

print(",".join(sorted(["jmq", "z06", "gmh", "z13", "qrh", "z38", "cbd", "rqf"])))
