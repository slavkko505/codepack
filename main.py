from ListColection import LstCollection
from Jewelry import Product
from memento import *

def menu():

    p = LstCollection()
    jewelry = Jewerly(p)
    jewelry.backup("Empty collection.")
    while True:
        help_message = get_help_message()
        task = input(help_message)
        if task == "1":
            read_json_file(p)
            jewelry.backup("Read json.")
        elif task == "2":
            sort_elements(p)
            jewelry.backup("Sort elements.")
            write_in_json_file(p)
        elif task == "3":
            search_elements(p)
            write_in_json_file(p)
        elif task == "4":
            add_product(p)
            jewelry.backup("Add Product to collection.")
            write_in_json_file(p)
        elif task == "5":
            del_product(p)
            jewelry.backup("Del element from collection.")
            write_in_json_file(p)
        elif task == "6":
            edit_product(p)
            jewelry.backup("Edit element from collection.")
            write_in_json_file(p)
        elif task == "7":
            write_in_txt_file(p)
        elif task == "8":
            write_in_json_file(p)
        elif task == "9":
            for product in p:
                print(product)
        elif task == "undo":
            undo_moment(jewelry)
            write_in_json_file(p)
        elif task == "redo":
            redo_moment(jewelry)
            write_in_json_file(p)
        elif task == "move":
            move_moment(jewelry)
            write_in_json_file(p)
        elif task == "history":
            jewelry.show_history()
            write_in_json_file(p)
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
                    "\n  undo - to undo moment. " + 24 * " " + \
                    "\n  redo - to redo moment. " + 24 * " " + \
                    "\n  move - to move on moment. " + 21 * " " + \
                    "\n  history - to show history of moments. " + 9 * " " + \
                    "\n  exit - to exit.  " + 30 * " " + "\n"
    help_message += "*" * 51 + "\n"
    return help_message

@Validation.validate_inp
def read_json_file(p):
    global file_name
    file_name = input("Enter file_name: ")
    p.read_json_file(file_name)

@Validation.validate_inp
def sort_elements(p):
    p.sort(input("Enter field for which you want to sort: \n"
                        "possible: title, code, price, material, type, date_of_creation:\n"))

@Validation.validate_inp
def search_elements(p):
    parameter = input("Enter parameter which elements you want to find: \n")
    for e in p.search(parameter):
        print(e)

@Validation.validate_inp
def add_product(p):
    d = Product.input_("title", "code", "material", "type", "date_of_creation", "price", "u_id")
    p.append(Product(**d))

@Validation.validate_inp
def del_product(p):
    p.delete(input("Enter id to delete: "))

@Validation.validate_inp
def edit_product(p):
    p.edit(input("Enter id to edit: "), input("Enter atter to edit: "), input("Enter value to change: "))

@Validation.validate_inp
def write_in_txt_file(p):
    p.add_el_to_file(input("Enter file_name: "), Product.input_("title", "code", "material", "type", "date_of_creation", "price", "u_id") )

@Validation.validate_inp
def write_in_json_file(p):
    p.write_in_json_file(file_name)

@Validation.validate_inp
def undo_moment(und):
    und.undo()

@Validation.validate_inp
def redo_moment(red):
    red.redo()

@Validation.validate_inp
def move_moment(move):
    move.show_history()
    moment = input("Enter moment: ")
    move.move_on_moment(moment)


if __name__ == "__main__":
    menu()
