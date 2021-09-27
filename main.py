from ListColection import LstCollection
from Jewelry import Product
from Validation import Validation


def menu():
    p = LstCollection()
    while True:
        help_message = get_help_message()
        task = input(help_message)
        if task == "1":
            Validation.validate_inp(read_json_file, p)
        elif task == "2":
            Validation.validate_inp(sort_elements, p)
        elif task == "3":
            search_elements(p)
        elif task == "4":
            Validation.validate_inp(add_product, p)
        elif task == "5":
            Validation.validate_inp(del_product, p)
        elif task == "6":
            Validation.validate_inp(edit_product, p)
        elif task == "7":
            Validation.validate_inp(write_in_txt_file, p)
        elif task == "8":
            Validation.validate_inp(write_in_json_file, p)
        elif task == "9":
            for product in p:
                print(product)
        elif task == "exit":
            print("Goodbye!")
            break
        else:
            print("___wrong input___")
            continue
        print()


def get_help_message():
    help_message = "*" * 51
    help_message += "\n  HELP:" + 42 * " " + "\n  Possible commands:" + 29 * " " + \
                    "\n  1 - to read from json file;" + 25 * " " + \
                    "\n  2 - to sort elements; " + 25 * " " + \
                    "\n  3 - to search element.  " + 20 * " " + \
                    "\n  4 - to add Jewelry to collection. " + 10 * " " + \
                    "\n  5 - to del Jewelry element from collection.  " + 10 * " " + \
                    "\n  6 - to edit Jewelry element from collection.  " + 9 * " " + \
                    "\n  7 - to write collection elements to txt file.  " \
                    "\n  8 - to write collection elements to json file. " \
                    "\n  9 - to print collection. " + 22 * " " + \
                    "\n  exit - to exit.  " + 30 * " " + "\n"
    help_message += "*" * 51 + "\n"
    return help_message


def read_json_file(p):
    p.read_json_file(Validation.validateFileName(input("Enter file_name: "), "json"))


def sort_elements(p):
    p.sort(input("Enter field for which you want to sort: \n"
                        "possible: title, code, price, material, type, date_of_creation:\n"))


def search_elements(p):
    parameter = input("Enter parameter which elements you want to find: \n")
    for e in p.search(parameter):
        print(e)


def add_product(p):
    d = Product.input_("title", "code", "material", "type", "date_of_creation", "price", "u_id")
    p.append(Product(**d))


def del_product(p):
    p.delete(input("Enter id to delete: "))


def edit_product(p):
    p.edit(input("Enter id to edit: "), input("Enter atter to edit: "), input("Enter value to change: "))


def write_in_txt_file(p):
    p.add_el_to_file(input("Enter file_name: "), Product.input_("title", "code", "material", "type", "date_of_creation", "price", "u_id") )


def write_in_json_file(p):
    p.write_in_json_file(Validation.validateFileName(input("Enter file_name: "), "json"))


if __name__ == "__main__":
    menu()
