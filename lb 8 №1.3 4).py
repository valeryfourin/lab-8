'''
output the array 3x3 and replace negative elements with 0
'''
import numpy as np
import random
while True:
    a = np.zeros((4, 4), dtype=int)
    # створюємо матрицю 4х4 з усіма 0

    for i in range(4):
        for g in range(4):
            a[i,g] = input(f'Input [{i},{g}] element of array A:')  # користувач вводить елементи матриці

    print(f'Array A:\n{a}')
    for i in range(4):      # цикл проходить по рядкам матриці
        for g in range(4):      # цикл проходить по стовпчикам матриці
            if a[i,g] < 0:  # якщо елемент менший за 0, то він замінюється нулем
                a[i,g] = 0

    print(f'Array A without negative elements:\n{a}')
    answer = input('Do you want to continue? Yes-1, No-2:')
    if answer == '1': continue
    else: break

