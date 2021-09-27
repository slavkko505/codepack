# material(gold/silver/platinum), type(rings/earrings/bracelets), code(*****/*-**)
from datetime import datetime
import re

class Validation:

    @staticmethod
    def validateStr(value):
        if any(map(str.isdigit, value)):
            print("Title must not contain integers.")
            raise ValueError
        return value

    @staticmethod
    def validatePrice(value):
        try:
            v = float(value)
            if re.match(r'[0-9]*\.[0-9]{2}', value):
                print("Price must have two digits after coma.")
                raise ValueError
        except ValueError:
            print("Price must be float of int and must have two digits after coma!")
            raise ValueError
        return v

    @staticmethod
    def validateDate(date):
        datetime.strptime(date, '%Y-%m-%d')
        if int(date[0:4]) > 2022:
            raise ValueError
        else:
            return date

    @staticmethod
    def isBiggerDate(date1, date2):
        if date1 > date2:
            print("Incorrect data")
            raise ValueError

    @staticmethod
    def validateCode(value):
        if Validation.isDigit(value):
            if len(str(value)) == 5:
                return value
            elif len(str(value)) == 3:
                return str(value)[0] + '-' + str(value)[1] + str(value)[2]
            else:
                print(" code must be integers with len 3 or 5.")
                raise ValueError
        else:
            print(" code must be integers.")
            raise ValueError

    @staticmethod
    def isDigit(x):
        return all(map(str.isdigit, x))

    @staticmethod
    def isId(value):
        if Validation.isDigit(value):
            return value
        else:
            raise ValueError

    @staticmethod
    def validateMaterial(title):
        if Validation.validateStr(title):
            if title == 'gold' or title == 'silver' or title == 'platinum':
                return title
            else:
                print("Material must be 'gold', 'silver' or 'platinum'")
                raise ValueError

    @staticmethod
    def validateType(title):
        if Validation.validateStr(title):
            if title == 'rings' or title == 'earrings' or title == 'bracelets':
                return title
            else:
                print("Type must be 'rings', 'earrings' or 'bracelets'")
                raise  ValueError

    @staticmethod
    def validateFileName(filename, end=".txt"):
        if not filename.endswith(end):
            raise ValueError("Incorrect filename, should end with ." + end + ".")
        return filename

    @staticmethod
    def validate_inp(func, m):
        t = False
        while True:
            try:
                if t:
                    n = input("Enter 'exit' to go back or 'con' to continue \n")
                    if n == "exit":
                        break
                    elif n == "con":
                        func(m)
                    else:
                        continue
                func(m)
                break
            except ValueError:
                print("\n___wrong input___\n")
                t = True
                continue
