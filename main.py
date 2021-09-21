# Задана цілочисельна квадратна матриця порядку n.
# Знайти у кожному рядку матриці найбільший елемент
# і поміняти його місцями з елементом головної діагоналі.

def EnterNumberMat():
    while True:
        try:
            n = int(input('Ведіть порядок матриці '))
            if n == 0:
                print('\nВедіть число відміне від 0 ')
                continue
            if n < 0:
                print('\nВедіть число більше від 0 ')
                continue
            break
        except ValueError:
            print('\nВведіть число')
    return n

def StartMetod():
    while True:
        print(help_mes())
        try:
            n = int(input())
            if n == 1:
                allMatInDisplay()
            elif n == 2:
                break
            else:
                continue
        except ValueError:
            print('\nВедіть число')

def help_mes():
    help_message = "*" * 31
    help_message += "\n Команди:" + 9 * " " + \
                    "\n 1 - Ввести матрицю;" + 5 * \
                    " " + "\n 2 - Завершити програму.  \n"
    help_message += "*" * 31 + "\n"
    return help_message

def MakeMat(s):
    a = []
    print("Вводимо матрцю через Enter")
    for i in range(s):
        a.append([])
        for j in range(s):
            while True:
                try:
                    n = int(input())
                    a[i].append(n)
                    break
                except ValueError:
                    print('\nВведіть число')
    return a

def PrintMat(str='',*a):
    print(str)
    print(str)
    for row in a:
        print(*map("{:4d}".format, row))
    print()

def SwapMat(*a):
    for i in range(len(a)):
        m = a[i][0]
        pos=0
        for j in range(len(a)):
            if m < a[i][j]:
                m = a[i][j]
                pos = j

        a[i][i], a[i][pos] = m, a[i][i]
    return a

def allMatInDisplay():
    a = MakeMat(EnterNumberMat())
    PrintMat("Початкова матриця", *a)

    b = SwapMat(*a)
    PrintMat("Кінцева матриця", *b)

StartMetod()
