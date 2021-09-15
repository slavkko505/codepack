# Задано масив а цілих чисел розмірності . Вивести суму додатніх елементів масиву,
# якщо у цьому масиві чергуються додатні і від’ємні елементи.
# Якщо ні, вивести всі від’ємні елементи, зберігаючи їх порядок.

def AddToMat():
    a = []
    while True:
        try:
            n = int(input('Ведіть розмірність масиву '))
            if n == 0:
                print('\nВедіть число відміне від 0 ')
                continue
            if n < 0:
                print('\nВедіть число більше від 0 ')
                continue
            break
        except ValueError:
            print('\nВедіть число')
    for i in range(0, n):
        a.append(int(input()))
    return a

def SumElem(*a):
    t = False
    for i in range(len(a) - 1):
        if a[i]*a[i + 1] < 0:
            t = True
        else:
            t = False
            break
    if t:
        s=0
        for i in a:
            if i >0:
                s =s+i
        print(s)
    else:
        for i in a:
            if i <0:
                print(i,end=' ')

a = AddToMat()
SumElem(a)
