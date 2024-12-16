#!/usr/bin/env python3

import sys

in_fn = sys.argv[1]

loop_found = 0

arr_orig = []

with open(in_fn, 'r') as data:
    for line in data:
        arr_orig.append(' ' + line.rstrip('\n') + ' ')

dummy = ' ' * len(arr_orig[0])
arr_orig.append(dummy)
arr_orig.insert(0, dummy)

all_cases = 0

for iy, vy in enumerate(arr_orig):
    arr_orig[iy] = list(vy)

for obs_y, obs_vy in enumerate(arr_orig):
    for obs_x, obs_vx in enumerate(obs_vy):
        #(obs_x, obs_y) = (3, 9)
        if arr_orig[obs_y][obs_x] in [" ", "#", '^']:
            continue
        all_cases += 1
        #print(f'{obs_x} {obs_y}')
        arr = []

        #print("Lemasoljuk a tombot")
        for iy, vy in enumerate(arr_orig):
            arr.append(list(vy))
        #for qy, q_vy in enumerate(arr):
        #    for qx, q_vx in enumerate(q_vy):
        #        print(arr[qy][qx], end='')
        #    print()


        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        direction = 0
        (xc, yc) = (0, 0)
        
        for iy, vy in enumerate(arr):
            for ix, vx in enumerate(vy):
                if vx == '^':
                    direction = 0
                    (xc, yc) = (ix, iy)
                    #arr[iy][ix] = "X"
                #print(vx, end='')
            #print()
        
        arr[obs_y][obs_x] = "#"
        
        while True:
            xc2 = xc + directions[direction][0]
            yc2 = yc + directions[direction][1]
            try:
                c = int (arr[yc2][xc2], 16)
            except ValueError:
                c = 0

            if arr[yc2][xc2] == " ":
                break
            elif arr[yc2][xc2] == "#":
                direction += 1
                direction %= 4
            elif c & (1 << direction):
                loop_found +=1
                print(f"LOOP! ({obs_x}, {obs_y}) ({loop_found} / {all_cases})")
                break
            else:
                #print(f'{xc}, {yc} -> {xc2}, {yc2}')
                c |= (1 << direction)
                (xc, yc) = (xc2, yc2)
                arr[yc][xc] = hex(c)[2].upper()
                #print(f'{xc}, {yc} -> {xc2}, {yc2}')
            #for iy, vy in enumerate(arr):
            #    for ix, vx in enumerate(vy):
            #        print(vx, end='')
            #    print()
            #print("----------------------------")
        
        visited = 0
        
        #for iy, vy in enumerate(arr):
        #    for ix, vx in enumerate(vy):
        #        if vx == 'X':
        #            visited += 1
        #        print(vx, end='')
        #    print()


print(loop_found)
