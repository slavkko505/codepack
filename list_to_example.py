import random
import class_Ll


def start_metod():
    s = class_Ll.Ll()
    while True:
        print(help_mes())
        try:
            n = int(input())
            if n == 2:
                print_mas(make_mas_by_yourself(s), "Масив введений вручну")
            elif n == 1:
                num = enter_number()
                print_mas(make_mas_by_random(s, num), "Масив рандомного типу")
            elif n == 3:
                sum_or_swap(s).display()
                print_mas(s, "Змінений масив ")
            elif n == 4:
                while True:
                    try:
                        item = int(input("Введіть елемент який хочете додати \n"))
                        pos = int(input("Введіть позицію в яку хочете додати елемент \n"))
                        break
                    except ValueError:
                        print('\nВведіть число')
                add_elem(s, item, pos)
                print_mas(s, "Змінений масив ")
            elif n == 5:
                while True:
                    try:
                        pos = int(input("Введіть позицію з якої хочете видалити елемент \n"))
                        break
                    except ValueError:
                        print('\nВведіть число')
                del_elem(s, pos)
                print_mas(s, "Змінений масив ")
            elif n == 6:
                print("Завершення програми")
                break
            else:
                continue
        except ValueError:
            print('\nВедіть число')


def help_mes():
    help_message = "*" * 45
    help_message += "\n Команди:" + 9 * " " + \
                    "\n \t1 - Створити рандомний масив; \n \t2 - Самостійно ввести масив; " + 5 * \
                    " " + "\n \t3 - Знайти суму усіх додатніх елементів;  \n"
    help_message += " \t4 - Додати елемент в k позицію; " + 5 * \
                    " " + "\n \t5 - Видалити елемент з k позиції; \n" \
                          " \t6 - Завершити програму. \n"
    help_message += "*" * 45 + "\n"
    return help_message


def add_elem(a, item, pos):
    a.insert(item, pos)


def del_elem(a, pos):
    a.delete(pos)


def make_mas_by_yourself(my_list):
    print("Вводимо через пробіл")
    while True:
        try:
            n = list(map(int, input().split()))
            for i in range(len(n)):
                my_list.append(class_Ll.Node(n[i]))
            break
        except ValueError:
            print('\nВведіть число')
    return my_list


def make_mas_by_random(my_list, s):
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

