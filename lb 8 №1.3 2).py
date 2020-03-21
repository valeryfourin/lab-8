'''
output the transposed matrix 3x3
'''
import numpy as np
import random
while True:
    n = int(input('Input the size of matrix: '))
    a, b = np.zeros((n,n), dtype = int), np.zeros((n,n), dtype = int)
    # створюємо дві матриці з усіма 0, в другу матрицю запишемо транспоновану першу

    for i in range(n):      # цикл проходить по рядкам матриці
        for j in range(n):      # цикл проходить по стовпчикам матриці
            a[i,j] = random.randint(-10,10)     # генерування елементів матриці
    print(f'Array a:\n{a}')
    for i in range(n):     # цикл проходить по рядкам матриці
        for j in range(n):      # цикл проходить по стовпчикам матриці
            b[j][i] = a[i][j]
    # в матрицю b записується елемент матриці а, що знаходиться симетрично відносно головної діагоналі матриці

    print(f'Array a transposed:\n{b}')
    answer = input('Do you want to continue? Yes-1, No-2:')
    if answer == '1': continue
    else: break

