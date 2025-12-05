#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

intervals = []

def overlap(b1, e1, b2, e2):
    #if (b2 >= b1 and b2 <= e1) or (e2 >=b1 and e2 <= e1):
    if e1 < b2 or e2 < b1:
        return False
    else:
        return True

with open(in_fn, 'r') as data:
    for line in data:
        line = line.rstrip("\n")
        if line == "":
            break
        (a, b) = [int(x, 10) for x in line.split("-")]
        intervals.append({"first": a, "last": b, "valid": True})

while True:
    new_intervals = []
    for i, interval1 in enumerate(intervals):
        if interval1["valid"]:
            for j, interval2 in enumerate(intervals[i + 1:]):
                if interval2["valid"] and overlap(interval1["first"], interval1["last"], interval2["first"], interval2["last"]):
                    #print(f'Overlap: {interval1}, {interval2}')
                    new_intervals.append({"first": min(interval1["first"], interval2["first"]), "last": max(interval1["last"], interval2["last"]), "valid": True})
                    interval1["valid"] = False
                    interval2["valid"] = False
    if len(new_intervals) == 0:
        break
    intervals.extend(new_intervals)

ans = 0
for interval in intervals:
    if interval["valid"]:
        ans += (interval["last"] - interval["first"] + 1)
        #for x in range(interval["first"], interval["last"] + 1):
        #    print(x, end=", ")
print()

print(ans)
