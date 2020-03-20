'''
7. Інформація про кількість товарів певної групи заноситься в комп'ютер по мірі
надходження товарів. Групи товарів стандартизовані, шифруються трьома буквами
алфавіту і кількість груп обмежена. Скласти програму, яка виводить на екран зведену
відомість наявності товарів по заданій при перерахуванні ознаці упорядкування.
'''
import numpy as np
import random

mlk = {'cheese':15, 'cream':20, 'yogurt':12}
brd = {'bread':50, 'bagel':25, 'biscuit':60}
crn = {'buckwheat':100, 'corn':83, 'oatmeal':90}

print('\nINFORMATION ABOUT GROUPS, PRODUCTS AND QUANTITIES:\n')
print('For group "mlk":')
for i in dict.keys(mlk):
    print(f'{i} - {mlk[i]}')

print('\nFor group "brd":')
for i in dict.keys(brd):
    print(f'{i} - {brd[i]}')

print('\nFor group "crn":')
for i in dict.keys(crn):
    print(f'{i} - {crn[i]}')
while True:
    while True:
        try:
            answer = input('\nIf you want to sort in ascending order type "1",\n'
                           'If you want to sort in descending order type "2"\n'
                           'If you want to sort in alphabet order type "3"\n'
                           'If you want to sort in alphabet order in reverse type "4": ')


            if answer == '1': # відбувається упорядкування елементів кожної групи за зростанням кількості товарів
                print('\nGroup "mlk" sorted in ascending order:')
                for i in sorted(dict.values(mlk)):
                    for name, quant in dict.items(mlk):
                        if quant == i:
                            print(f'{name} - {i}')
                print('\nGroup "brd" sorted in ascending order:')
                for i in sorted(dict.values(brd)):
                    for name, quant in dict.items(brd):
                        if quant == i:
                            print(f'{name} - {i}')
                print('\nGroup "crn" sorted in ascending order:')
                for i in sorted(dict.values(crn)):
                    for name, quant in dict.items(crn):
                        if quant == i:
                            print(f'{name} - {i}')


            elif answer == '2': # відбувається упорядкування елементів кожної групи за спаданням кількості товарів
                print('\nGroup "mlk" sorted in ascending order:')
                for i in sorted(dict.values(mlk), reverse = True):
                    for name, quant in dict.items(mlk):
                        if quant == i:
                            print(f'{name} - {i}')
                print('\nGroup "brd" sorted in ascending order:')
                for i in sorted(dict.values(brd), reverse = True):
                    for name, quant in dict.items(brd):
                        if quant == i:
                            print(f'{name} - {i}')
                print('\nGroup "crn" sorted in ascending order:')
                for i in sorted(dict.values(crn), reverse = True):
                    for name, quant in dict.items(crn):
                        if quant == i:
                            print(f'{name} - {i}')


            elif answer == '3': # відбувається упорядкування елементів кожної групи в алфавітному порядку
                print('\nGroup "mlk" sorted by alphabet order:')
                for i in sorted(dict.keys(mlk)):
                    print(f'{i} - {mlk[i]}')
                print('\nGroup "brd" sorted by alphabet order:')
                for i in sorted(dict.keys(brd)):
                    print(f'{i} - {brd[i]}')
                print('\nGroup "crn" sorted by alphabet order:')
                for i in sorted(dict.keys(crn)):
                    print(f'{i} - {crn[i]}')


            elif answer == '4': # відбувається упорядкування елементів кожної групи в зворотньому алфавітному порядку
                print('\nGroup "mlk" sorted by alphabet order in reverse:')
                for i in sorted(dict.keys(mlk), reverse = True):
                    print(f'{i} - {mlk[i]}')
                print('\nGroup "brd" sorted by alphabet order:')
                for i in sorted(dict.keys(brd), reverse = True):
                    print(f'{i} - {brd[i]}')
                print('\nGroup "crn" sorted by alphabet order:')
                for i in sorted(dict.keys(crn), reverse = True):
                    print(f'{i} - {crn[i]}')


            else:
                print("\nError. Please input '1' or '2' or '3' or '4'.")
                continue
        except TypeError and ValueError:
            print('\nError. Please input only integers.')
            continue
        break

    answer2 = input('Do you want to continue? Yes-1, No-2:\n')
    if answer2 == '1':
        continue
    else:
        break