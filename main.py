from ListColection import LstCollection
from CarReservation import Product
from Validation import Validation


def menu():
    """
    The menu function.
    """
    p = LstCollection()
    while True:
        help_message = get_help_message()
        task = input(help_message)
        if task == "1":
            read_json_file(p)
        elif task == "2":
            add_product(p)
        elif task == "9":
            for product in p:
                print(product)
        elif task == "exit":
            print("GOODBYE!")
            break
        else:
            print("WRONG INPUT!")
            continue
        print()


def get_help_message():
    """
    The function that returns help message.
    """
    help_message = "*" * 51
    help_message += "\n  HELP:" + 42 * " " + "\n  Possible commands:" + 29 * " " + \
                    "\n  1 - to read from file;" + 25 * " " + \
                    "\n  2 - to to add Cars to collection. " + 10 * " " + \
                    "\n  9 - to print collection. " + 22 * " " + \
                    "\n  exit - to exit.  " + 30 * " " + "\n"
    help_message += "*" * 51 + "\n"
    return help_message

@Validation.validate_inp
def read_json_file(p):
    p.read_json_file((input("Enter file_name: ")))

@Validation.validate_inp
def add_product(p):
    d = Product.input_("name", "price", "car", "start_datetime", "end_datetime", "u_id")
    p.append(Product(**d))

@Validation.validate_inp
def edit_product(p):
    p.edit(input("Enter id to edit: "), input("Enter atter to edit: "), input("Enter value to change: "))


if __name__ == "__main__":
    menu()

