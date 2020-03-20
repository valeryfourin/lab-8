'''
output the transposed matrix 3x3
'''
import numpy as np
import random
while True:
    a=np.zeros((3,3), dtype = int)
    for i in range(3):
        for g in range(3):
            a[i,g] = random.randint(-10,10)
    print(f'Array a:\n{a}')
    a[0, 1], a[1, 0] = a[1, 0], a[0, 1]
    a[0, 2], a[2, 0] = a[2, 0], a[0, 2]
    a[1, 2], a[2, 1] = a[2, 1], a[1, 2]
    print(f'Array a transposed:\n{a}')
    answer = input('Do you want to continue? Yes-1, No-2:')
    if answer == '1': continue
    else: break

