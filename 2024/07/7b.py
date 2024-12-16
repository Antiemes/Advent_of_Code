#!/usr/bin/env python3

import sys

def number_to_base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

in_fn = sys.argv[1]

arr = []

with open(in_fn, 'r') as data:
    for line in data:
        [res, nums_s] = line.split(": ")
        nums = [int(x) for x in nums_s.split(" ")]
        arr.append({"res": int(res), "nums": nums})

good_sum = 0

for line in arr:
    res = line["res"]
    nums = line["nums"]
    psize = len(nums) - 1
    print("=========================================")
    print(res, psize)
    for i in range(3 ** psize):
        r = nums[0]
        ms = [{0: '+', 1: '*', 2: '|'}[x] for x in number_to_base(i + 3 ** psize, 3)[1:]]
        for (m, n) in zip(ms, nums[1:]):
            if m == '+':
                r += n
            elif m == '*':
                r *= n
            elif m == '|':
                r = int(str(r) + str(n))
            else:
                raise Exception("Error")
        #print(format(i, '0' + str(psize) + 'b'))
        #z = str(nums[0]) + ''.join([m + str(n) for (m, n) in zip(b, nums[1:])])
        #r = eval(z)
        #print(z)
        #print(ms)
        #print(r)
        if r == res:
            #print(f'{r}: {ms}')
            good_sum += res
                #print("good")
            break
    print("---------")

print(good_sum)
