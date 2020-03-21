'''
 the direct substring search
'''
import random
import string
import timeit

while True:
    while True:
        try:
            answer1 = int(input("Please type '1' if you want to input an string,\ntype '2' if you want to generate a string,\n"
                                "type '3' to see how the program finds substring in already existing string,\n"
                                "type '4' to see how the program doesn't find the element: \n"))
            # користувачу представлений вибір з 4 варіантів проходження програми:
            # при першому користувач вводить рядок і підрядок, який потрібно знайти у рядку
            # при другому програма генерує рядок і користувач задає підрядок, який потрібно знайти у рядку
            # при третьому задано рядок та підрядок, який потрібно знайти
            # при четвертому задано рядок та підрядок, який потрібно знайти, проте цього підрядка у рядку немає

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

    i = -1  # використовується, щоб перейти на наступний символ рядка, відповідає за індекси рядка
    j = 0   # кількість збігів, відповідає за індекси підрядка
    num_of_comp = 0  # кількість порівнянь

    while (j < len(s1)) and i < ((len(s) - len(s1))):
        j = 0
        i += 1
        num_of_comp += 2  # дві умови перевіряються перед тим, як зайти у цикл
        while j < len (s1) and s1[j] == s[i+j]:
            j += 1
            num_of_comp += 2  # також дві умови перевіряються перед тим, як зайти у цикл
    # вкладений цикл порівнює символи підрядка і рядка, якщо виконався збіг першого символа,
    # у змінну "j" записується +1 і далі порівнюється наступний елемент рядка і наступний елемент підрядка
    # до тих пір, доки всі елементи не співпадуть, або доки ітерація не дойде до моменту,
    # після якого вже не буде змісту шукати підрядок, бо відстань до кінця рядка менша за довжину підрядка
    # (за це відповідає друга умова першого циклу)

    if j == len(s1):  # якщо довжина змінної "j" така ж, як і довжина підрядка, то ми його знайшли на позиції "і"
        num_of_comp += 1  # ще одна перевірка
        print(f'Substring {s1} is found on the {i}th position')

    else:
        num_of_comp += 2  # ця і попередня умови
        print('Substring is not found')

    print(f'{num_of_comp} comparisons have been made.')
    t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)  # час виконання програми
    print(f'Time of program execution: {t} sec')

    answer2 = input('\nDo you want to continue? Yes-1, No-2:\n')
    if answer2 == '1':
        continue
    else:
        break