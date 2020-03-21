'''
output array backwards
'''
import numpy as np
import random
while True:
    n = int(input('Input number of elements:'))
    a=np.zeros((n), dtype = int) # створюємо масив а і заповнюємо його нулями

    for i in range(n):  # генеруємо елементи масиву а
        a[i] = random.randint(-10,10)
    print(f'Array a={a}')

    a_backwards = []
    for j in range(n-1, -1, -1): # за допомогою функції range з кроком -1 додаємо у створений масив елементи у зворотньому порядку
        a_backwards.append(a[j])
    print(f'Array a backwards={a_backwards}')

    answer = input('Do you want to continue? Yes-1, No-2:')
    if answer == '1': continue
    else: break

