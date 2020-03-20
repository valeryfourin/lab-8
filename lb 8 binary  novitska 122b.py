'''
 the binary search
'''
import numpy as np
import random
while True:
    while True:
        try:
            answer1 = int(input("Please type '1' if you want to input an array,\ntype '2' if you want to generate an array,\n"
                                "type '3' to see how the program finds element in already existing array,\n"
                                "type '4' to see how the program doesn't find the element: "))
            if answer1 == 1:    # користувач задає масив
                while True:
                    try:
                        size = int(input('Input the numbers of elements in your array: '))
                        A = np.zeros((size), dtype=int)

                        for s in range(size):

                            while True:
                                try:
                                    A[s] = input(f'Please input {s} element: ')
                                except TypeError and ValueError:
                                    print('Error. Please input only integers.')
                                    continue
                                break

                    except TypeError and ValueError:
                        print('Error. Please input only integers.')
                        continue
                    break
                print(f'\n{A}')
                x = int(input('Please input the item you are looking for: '))

            elif answer1 == 2:     # масив генерується рандомно
                while True:
                    try:
                        size = int(input('Input the numbers of elements in your array: '))
                        lower_limit = int(input('Please input the lower limit of the generating array: '))
                        upper_limit = int(input('Please input the upper limit of the generating array: '))

                    except TypeError and ValueError:
                        print('Error. Please input only integers.')
                        continue
                    break
                A = np.zeros((size), dtype=int)
                for s in range(size):
                    A[s] = random.randint(lower_limit, upper_limit)
                print(f'\n{A}')
                x = int(input('Please input the item you are looking for: '))

            elif answer1 == 3: # заданий масив, заданий елемент, що наявний в масиві
                A = np.array([2, -6, 8, 12, 0, -4, 6, 20])
                x = 12
                print(f'Search for element {x}')

            elif answer1 == 4: # заданий масив, заданий елемент, що відсутній в масиві
                A = np.array([2, -6, 8, 12, 0, -4, 6, 20])
                x = 10
                print(f'Search for element {x}')

            else:
                print("Input '1' or '2' or '3' or '4'.")
                continue
        except TypeError and ValueError:
            print('Error. Please input only integers.')
            continue
        break

    print()
    A = sorted(A)
    print(A)

    L = 0
    R = len(A) - 1
    k = 0
    number_of_comparisons = 0
    flag = False

    while L <= R and not flag:
        k = (L + R) // 2
        number_of_comparisons += 1
        if A[k] == x:
            flag = True
        elif (A[k] < x):
            L = k + 1
        else:
            R = k - 1

    if not flag:
        print('Element not found')
    else:
        print(f'Element {x} is found on the {k}th position')
    print(f'Number of comparisons made is {number_of_comparisons}.')
    print()

    answer2 = input('Do you want to continue? Yes-1, No-2:\n')
    if answer2 == '1':
        continue
    else:
        break