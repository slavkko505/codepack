import random
import class_Ll


def add_elem(a, item, pos):
    a.insert(item, pos)


def del_elem(a, pos):
    a.delete(pos)


def make_mas_by_iter(my_list, s):
    while True:
        try:
            a = int(input("Введіть границю - а "))
            b = int(input("Введіть границю - b "))
            if a > b:
                print("а не повинно бути більше за b \n")
                continue
            break
        except ValueError:
            print('\nВедіть число')

    for i in range(s):
        my_list.append(class_Ll.Node(random.randint(a, b)))

    return my_list


def make_mas_by_generator(my_list, s):
    while True:
        try:
            a = int(input("Введіть границю - а "))
            b = int(input("Введіть границю - b "))
            if a > b:
                print("а не повинно бути більше за b \n")
                continue
            break
        except ValueError:
            print('\nВедіть число')

    for i in range(s):
        my_list.append(class_Ll.Node(*generator(a, b)))

    return my_list


def generator(a, b):
     yield random.randint(a, b)


def enter_number():
    while True:
        try:
            n = int(input('Ведіть кількість елементів які хочете додати \n'))
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


def sum_or_swap(a):
    t = False
    for i in range(a.__len__()-1):
        if a.__getitem__(i) * a.__getitem__(i+1) < 0:
            t = True
        else:
            t = False
            break
    if t:
        my_list_1 = class_Ll.Ll()
        s = 0
        for i in range(a.__len__()):
            if a.__getitem__(i) > 0:
                s = s + a.__getitem__(i)
        my_list_1.append(class_Ll.Node("Сума дадатніх елементів \n"))
        my_list_1.append(class_Ll.Node(s))
        return my_list_1
    else:
        my_list_2 = class_Ll.Ll()
        my_list_2.append(class_Ll.Node("В масиві не чергуються відємні і додатні елементи \n"))
        for i in range(a.__len__()):
            if a.__getitem__(i) < 0:
                my_list_2.append(class_Ll.Node(a.__getitem__(i)))
        return my_list_2


def print_mas(a, s=''):
    print()
    print(s)
    for i in a:
        print(i, end=" ")
    print()

