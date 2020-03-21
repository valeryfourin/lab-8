'''
output the multiplication of two matrix 3x3
'''
import numpy as np
import random
while True:
    a, b, c = np.zeros((3, 3), dtype=int), np.zeros((3, 3), dtype=int), np.zeros((3, 3), dtype=int)

    # створюємо три матриці з усіма 0, в третю матрицю запишемо добуток першої на другу
    for i in range(3):
        for j in range(3):
            a[i, j] = random.randint(-10, 10)  # генерування елементів матриці а
    for i in range(3):
        for j in range(3):
            b[i, j] = random.randint(-10, 10)  # генерування елементів матриці b

    print(f'Array A:\n{a}')
    print(f'Array B:\n{b}')


    for i in range(3):      # цикл проходить по рядкам матриці
        for j in range(3):      # цикл проходить по стовпчикам матриці
            for g in range(3):
                c[i][j] += a[i][g] * b[g][j]
    # останній вкладений цикл for обчислює суму добутків елементів g-того рядка першої матриці (а)
    # на елементи g-того стовпчика другої матриці (b) і записує результати у третю матрицю (с)

    print(f'The result of A*B=C:\n{c}')
    answer = input('Do you want to continue? Yes-1, No-2:')
    if answer == '1': continue
    else: break

'''

    c[0, 0] = a[0, 0] * b[0, 0] + a[0, 1] * b[1, 0] + a[0, 2] * b[2, 0]
    c[0, 1] = a[0, 0] * b[0, 1] + a[0, 1] * b[1, 1] + a[0, 2] * b[2, 1]
    c[0, 2] = a[0, 0] * b[0, 2] + a[0, 1] * b[1, 2] + a[0, 2] * b[2, 2]
    c[1, 0] = a[1, 0] * b[0, 0] + a[1, 1] * b[1, 0] + a[1, 2] * b[2, 0]
    c[1, 1] = a[1, 0] * b[0, 1] + a[1, 1] * b[1, 1] + a[1, 2] * b[2, 1]
    c[1, 2] = a[1, 0] * b[0, 2] + a[1, 1] * b[1, 2] + a[1, 2] * b[2, 2]
    c[2, 0] = a[2, 0] * b[0, 0] + a[2, 1] * b[1, 0] + a[2, 2] * b[2, 0]
    c[2, 1] = a[2, 0] * b[0, 1] + a[2, 1] * b[1, 1] + a[2, 2] * b[2, 1]
    c[2, 2] = a[2, 0] * b[0, 2] + a[2, 1] * b[1, 2] + a[2, 2] * b[2, 2]

'''