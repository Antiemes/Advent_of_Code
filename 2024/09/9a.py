#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

def print_disk(disk):
    for cid in disk:
        if cid < 0:
            c = "."
        else:
            c = str(cid)
        print(c, end="\n")
    print()

comp = []
disk = []

with open(in_fn, 'r') as data:
    for line in data:
        comp = [int(x) for x in list(line.rstrip("\n"))]

for idx, clen in enumerate(comp):
    if idx % 2 == 0:
        cid = idx // 2
    else:
        cid = -1
    disk += [cid] * clen

#print_disk(disk)

lidx = 0
ridx = len(disk) - 1
while True:
    while disk[ridx] == -1:
        ridx -= 1
    while not disk[lidx] == -1:
        lidx += 1
    if not ridx > lidx:
        break
    disk[lidx], disk[ridx] = disk[ridx], disk[lidx]
    #print_disk(disk)

#print()
#print_disk(disk)
#print()

checksum = sum([idx * fid for (idx, fid) in zip(range(len(disk)), [x if x >= 0 else 0 for x in disk])])
print(checksum)

#checksum = 0
#
#for idx, foo in enumerate(disk):
#    if foo < 0:
#        foo = 0
#    a = idx * foo
#    #print(idx, foo, a)
#    checksum += a
#
#print(checksum)
