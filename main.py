import  numpy as np

def StartMetod():
    while True:
        print(Help_mes())
        try:
            n = int(input())
            if n == 2:
                s = MakeMatByFirstMetod(EnterNumberMat())
                PrintMat("Матриця яку вели вручну",s)
                printCountOfSearchAndYourElem(s)
            elif n == 1:
                s = MakeMatByRandomMetod(EnterNumberMat())
                PrintMat("Матриця рандомного типу",s)
                printCountOfSearchAndYourElem(s)
            elif n == 3:
                print("Завершення програми")
                break
            else:
                continue
        except ValueError:
            print('\nВедіть число')

def Help_mes():
    help_message = "*" * 30
    help_message += "\n Команди:" + 9 * " " + \
                    "\n 1 - Створити рандомну матрицю; \n 2 - Самостійно вводимо матрицю; " + 5 * \
                    " " + "\n 3 - Завершити програму.  \n"
    help_message += "*" * 30 + "\n"
    return help_message


def printCountOfSearchAndYourElem(s):
    s = SortMat(s)
    PrintMat("Sorted Mat ",s)
    while True:
        try:
            n = int(input('1 - якщо ви хочете знайти елемент матриці, 2 - для виходу \n'))
            if n == 1:
                while True:
                    try:
                        x = int(input("Введіть значення яке хочете знати? \n"))
                        if n==1:
                            BinarySearch(s,x)
                        else:
                            continue
                        break
                    except ValueError:
                        print('\nВведіть число')
            elif n == 2:
                break
            else:
                continue
        except ValueError:
            print('\nВведіть число')

def BinarySearch(mat,val):
    if len(mat) == 0:
        return False
    row_len = len(mat[0])
    col_len = len(mat[0])

    low = 0
    high = row_len * col_len

    while low < high:
        mid = (low + high) // 2
        if mat[mid // col_len][mid % col_len] == val:
            print("Число знайдене (", mid // col_len, ",", mid % col_len, ")")
            return True
        elif mat[mid // col_len][mid % col_len] < val:
            low  = mid +1
        else:
            high = mid
    print("Число не знайдене")
    return False

def SortMat(*array):
    count = 0
    b = []
    for i in array[0]:
        for j in i:
            b.append(j)
            count = count + 1
    for i in range(len(b)):
        for j in range(len(b)-1):
            if b[j] > b[j+1]:
                b[j], b[j+1] = b[j+1], b[j]
                count = count + 1
    mat = []
    l, r = 0, len(*array)
    for i in range(len(*array)):
        mat.append(b[l:r])
        l,r=l+len(*array),r+len(*array)
        count=count+1

    print("sortedCount - ", count)

    return mat

def MakeMatByFirstMetod(s):
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

def MakeMatByRandomMetod(s):
    while True:
        try:
            a = int(input("Введіть границю - а "))
            b = int(input("Введіть границю - b "))
            if a > b:
                print("а не повинно бути більше за b")
                continue
            break
        except ValueError:
            print('\nВедіть число')
    mat = np.random.randint(a,b, (s, s))
    return mat

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

def PrintMat(str='',*a):
    print()
    print(str)
    for i in a:
        for row in i:
            print(*map("{:4d}".format, row))
    print()

StartMetod()