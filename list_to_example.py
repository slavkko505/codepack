import random
import class_Ll


def start_metod():
    while True:
        print(help_mes())
        try:
            n = int(input())
            if n == 2:
                num = enter_number()
                s = make_mas_by_yourself(num)
                print_mas(s, "Масив введений вручну")
                next_step(s)
            elif n == 1:
                num = enter_number()
                s = make_mas_by_random(num)
                print_mas(s, "Масив рандомного типу")
                next_step(s)
            elif n == 3:
                print("Завершення програми")
                break
            else:
                continue
        except ValueError:
            print('\nВедіть число')


def help_mes():
    help_message = "*" * 30
    help_message += "\n Команди:" + 9 * " " + \
                    "\n 1 - Створити рандомний масив; \n 2 - Самостійно ввести масив; " + 5 * \
                    " " + "\n 3 - Завершити програму.  \n"
    help_message += "*" * 30 + "\n"
    return help_message


def help_mes_2():
    print()
    help_message = "*" * 45
    help_message += "\nДодаткові команди:" + 9 * " " + \
                    "\n 1 - Знайти суму усіх додатніх елементів; \n 2 - Додати елемент в k позицію; " + 5 * \
                    " " + "\n 3 - Видалити елемент з k позиції;  \n 4 - Повернутися в головне меню \n"
    help_message += "*" * 45 + "\n"
    return help_message


def next_step(s):
    while True:
        try:
            print(help_mes_2())
            n = int(input())
            if n == 1:
                sum_or_swap(s).display()
            elif n == 2:
                while True:
                    try:
                        item = int(input("Введіть елемент який хочете додати \n"))
                        pos = int(input("Введіть позицію в яку хочете додати елемент \n"))
                        break
                    except ValueError:
                        print('\nВведіть число')
                add_elem(s, item, pos)
                print_mas(s, "Змінений масив ")
            elif n == 3:
                while True:
                    try:
                        pos = int(input("Введіть позицію з якої хочете видалити елемент \n"))
                        break
                    except ValueError:
                        print('\nВведіть число')
                del_elem(s, pos)
                print_mas(s, "Змінений масив ")
            elif n == 4:
                break
            else:
                continue
        except ValueError:
            print('\nВведіть число')


def add_elem(a, item, pos):
    a.insert(item, pos)


def del_elem(a, pos):
    a.delete(pos)


def make_mas_by_yourself(s):
    my_list = class_Ll.Ll()
    print("Вводимо масив через Enter \n")
    for i in range(s):
        while True:
            try:
                n = int(input())
                my_list.append(class_Ll.Node(n))
                break
            except ValueError:
                print('\nВведіть число')
    return my_list


def make_mas_by_random(s):
    my_list = class_Ll.Ll()
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
    a.display()
    print()
