#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

def disk2list(disk):
    disk_list = []
    for chunk in disk:
        if chunk["type"] == 1 and chunk["active"]:
            c = chunk["id"]
        elif chunk["type"] == 0:
            for id in chunk["sub"]:
                disk_list += [disk[id]["id"]] * disk[id]["len"]
                #print("[" + str(id) + "]", end="")
            c = -1
        #elif chunk["type"] == 1 and not chunk["active"]:
        #    c = -1
        else:
            c = -1
        disk_list += [c] * chunk["len"]
    return disk_list

comp = []
disk = []

# 00...111...2...333.44.5555.6666.777.888899
# 0099.111...2...333.44.5555.6666.777.8888..
# 0099.1117772...333.44.5555.6666.....8888..
# 0099.111777244.333....5555.6666.....8888..
# 00992111777.44.333....5555.6666.....8888..

with open(in_fn, 'r') as data:
    for line in data:
        comp = [int(x) for x in list(line.rstrip("\n"))]

pos = 0
disk = []
for idx, clen in enumerate(comp):
    item = {"start": pos, "end": pos + clen, "len": clen}
    if idx % 2 == 0:
        item["type"] = 1
        item["id"] = idx // 2
        item["active"] = 1
    else:
        item["type"] = 0
        item["sub"] = []
    disk.append(item)
    pos += clen

#print(disk2str(disk))


for i in reversed(range(len(disk))):
    chunk = disk[i]
    if not chunk["type"] == 1:
        continue
    tlen = chunk["len"]
    for j in range(i):
        echunk = disk[j]
        if echunk["type"] == 0 and echunk["len"] >= tlen:
            chunk["active"] = 0
            echunk["len"] -= tlen
            echunk["sub"].append(i)
            break
    #print(disk2str(disk))

#lidx = 0
#ridx = len(disk) - 1
#while True:
#    while disk[ridx] == -1:
#        ridx -= 1
#    while not disk[lidx] == -1:
#        lidx += 1
#    if not ridx > lidx:
#        break
#    disk[lidx], disk[ridx] = disk[ridx], disk[lidx]
#    #print_disk(disk)

disk_list = disk2list(disk)

#print(disk_list)

checksum = sum([idx * fid for (idx, fid) in zip(range(len(disk_list)), [int (x) if x >= 0 else 0 for x in disk_list])])
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
