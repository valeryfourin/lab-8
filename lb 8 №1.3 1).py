'''
output array backwards
'''
import numpy as np
import random
while True:
    n = int(input('Input n:'))
    a=np.zeros((n), dtype = int)

    for i in range(n):
        a[i] = random.randint(-10,10)
    print(f'Array a={a}')

    a_backwards = []
    for j in range(n-1, -1, -1):
        a_backwards.append(a[j])
    print(f'Array a backwards={a_backwards}')

    answer = input('Do you want to continue? Yes-1, No-2:')
    if answer == '1': continue
    else: break

