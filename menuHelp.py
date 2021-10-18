import metodList as mm
import class_Ll


def start_metod():
    s = class_Ll.Ll()
    while True:
        print(help_mes())
        try:
            n = int(input())
            if n == 2:
                num = mm.enter_number()
                lList = mm.make_mas_by_generator(s, num)
                mm.print_mas(lList, "Генератор масив")

            elif n == 1:
                num = mm.enter_number()
                lList = mm.make_mas_by_iter(s, num)
                mm.print_mas(lList, "Ітератор масив")
            elif n == 3:
                mm.print_mas(mm.sum_or_swap(s))
                mm.print_mas(s, "Змінений масив ")
            elif n == 4:
                while True:
                    try:
                        item = int(input("Введіть елемент який хочете додати \n"))
                        pos = int(input("Введіть позицію в яку хочете додати елемент \n"))
                        break
                    except ValueError:
                        print('\nВведіть число')
                mm.add_elem(s, item, pos)
                mm. print_mas(s, "Змінений масив ")
            elif n == 5:
                while True:
                    try:
                        pos = int(input("Введіть позицію з якої хочете видалити елемент \n"))
                        break
                    except ValueError:
                        print('\nВведіть число')
                mm.del_elem(s, pos)
                mm.print_mas(s, "Змінений масив ")
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
                    "\n \t1 - Ітератор масив; \n \t2 - Генератор масив; " + 5 * \
                    " " + "\n \t3 - Знайти суму усіх додатніх елементів;  \n"
    help_message += " \t4 - Додати елемент в k позицію; " + 5 * \
                    " " + "\n \t5 - Видалити елемент з k позиції; \n" \
                          " \t6 - Завершити програму. \n"
    help_message += "*" * 45 + "\n"
    return help_message
