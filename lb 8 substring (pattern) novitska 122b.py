'''
 the direct substring search
'''
import random
import string
while True:
    while True:
        try:
            answer1 = int(input("Please type '1' if you want to input an string,\ntype '2' if you want to generate a string,\n"
                                "type '3' to see how the program finds substring in already existing string,\n"
                                "type '4' to see how the program doesn't find the element: \n"))

            if answer1 == 1:     # користувач задає рядок і підрядок
                s = input('Please input a sentence: ')
                s1 = input('Please input a substring you are looking for: ')

            elif answer1 == 2:  # програма генерує рядок, користувач задає рядок, який потрібно знайти
                N = int(input('Please input number of words: '))
                s = []
                for i in range(3):
                    s.append(''.join([random.choice(string.ascii_letters + string.digits + ' ') for n in range(random.randint(2, 8))]))
                s = ' '.join(s)
                print(s)
                s1 = input('Please input a substring you are looking for: ')

            elif answer1 == 3:  # заданий рядок, заданий підрядок, що наявний в рядку
                s = 'London is the capital of Great Britain.'
                s1 = 'Great Britain'
                print(f'\n{s}')
                print(f'Search for substring "{s1}"')

            elif answer1 == 4:   # заданий рядок, заданий підрядок, що відсутній в рядку
                s = 'London is the capital of Great Britain.'
                s1 = 'United States'
                print(f'\n{s}')
                print(f'Search for substring "{s1}"')

            else:
                print("Input '1' or '2' or '3' or '4'.")
                continue
        except TypeError and ValueError:
            print('\nError. Please input only integers.\n')
            continue
        break

    i = -1
    j = 0

    while (j < len(s1)) and i < ((len(s) - len(s1))):
        j = 0
        i += 1
        while j < len (s1) and s1[j] == s[i+j]:
            j += 1

    if j == len(s1):
        print(f'Substring {s1} is found on the {i}th position')
        print(f'{i} comparisons have been made.')
    else:
        print('Substring is not found')
        print(f'{i+1} comparisons have been made.')

    answer2 = input('Do you want to continue? Yes-1, No-2:\n')
    if answer2 == '1':
        continue
    else:
        break