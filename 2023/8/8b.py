#!/usr/bin/python3

import sys

class Hit(Exception):
    pass

def nSeg(n):
    return [[seg for seg in segs] for segs in xdig if len(segs) == n]

segMix = {}

def decode(segs):
    decodedSegs = [realSeg[s] for s in segs]
    if len(segs) == 2:
        return 1
    elif len(segs) == 4:
        return 4
    elif len(segs) == 3:
        return 7
    elif len(segs) == 7:
        return 8
    elif len(segs) == 5:
        if 'e' in decodedSegs:
            return 2
        elif 'f' in decodedSegs:
            return 5
        else:
            return 3
    elif len(segs) == 6:
        if 'b' in decodedSegs and 'e' in decodedSegs:
            return 0
        elif 'b' in decodedSegs and 'g' in decodedSegs:
            return 9
        elif 'e' in decodedSegs and 'g' in decodedSegs:
            return 6

'''
be
edb
cgeb
cfbegad

fdcge
fecdb
fabcd

 bcdefg
a cdefg
ab defg


'''

infile = open(sys.argv[1], 'r')

answer = 0

with infile:
    while True:
        row = infile.readline()
        if not row:
            break
        [dig10, dig4] = [s.strip() for s in row.split('|')]
        fdig = dig4.split()
        xdig = dig10.split()
        #for dig in fdig:
        #    if len(dig) in [2, 4, 3, 7]:
        #        count += 1
        
        realSeg = {}

        realSeg[[seg for seg in nSeg(3)[0] if not seg in nSeg(2)[0]][0]] = 'a'
        
        for seg in nSeg(2)[0]:
            if len([xseg for xseg in nSeg(6) if seg in xseg]) == 2:
                realSeg[seg] = 'b'
        
        for seg in nSeg(2)[0]:
            if len([xseg for xseg in nSeg(6) if seg in xseg]) == 3:
                realSeg[seg] = 'c'
        
        for seg in nSeg(4)[0]:
            if len([xseg for xseg in nSeg(5) if seg in xseg]) == 1:
                realSeg[seg] = 'f'
        
        for seg in nSeg(7)[0]:
            if len([xseg for xseg in nSeg(5) if seg in xseg]) == 1:
                if not seg in nSeg(4)[0]:
                    realSeg[seg] = 'e'
        
        for seg in nSeg(7)[0]:
            if len([xseg for xseg in nSeg(5) if seg in xseg]) == 3:
                if not seg in nSeg(4)[0]:
                    realSeg[seg] = 'd'
        
        for seg in nSeg(4)[0]:
            if len([xseg for xseg in nSeg(5) if seg in xseg]) == 3:
                realSeg[seg] = 'g'
        
        #for seg in realSeg.keys():
        #    print(f'{seg} -> {realSeg[seg]}')
        decodedStr = ''.join([str(decode(dig)) for dig in fdig])
        answer += int(decodedStr)
        print(decodedStr)


print(answer)

#enyem jo
#2  3
#2  5
#0  9
#0  6
#2  5
#9  9
