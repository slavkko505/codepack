# material(gold/silver/platinum), type(rings/earrings/bracelets), code(*****/*-**)
from datetime import datetime
import re

class Validation:

    @staticmethod
    def validateStr(func):
        def validateStrExpl(jewelry, value):
            if any(map(str.isdigit, value)):
                print("Words must not contain integers.")
                raise ValueError
            return func(jewelry, value)
        return validateStrExpl

    @staticmethod
    def validatePrice(func):
        def validatePriceExpl(jewelry, value):
            try:
                v = float(value)
                if re.match(r'[0-9]*\.[0-9]{2}', value):
                    print("Price must have two digits after coma.")
                    raise ValueError
            except ValueError:
                print("Price must be float of int and must have two digits after coma!")
                raise ValueError
            return func(jewelry, value)

        return validatePriceExpl

    @staticmethod
    def validateDate(func):
        def validateDateExpl(jewelry, date):
            datetime.strptime(date, '%Y-%m-%d')
            if int(date[0:4]) > 2022:
                print("Data time error")
                raise ValueError
            return func(jewelry, date)
        return validateDateExpl

    @staticmethod
    def validateCode(func):
        def validateCodeExpl(jewelry, value):
            if Validation.isDigit(value):
                if len(str(value)) == 8:
                    return func(jewelry, str(value)[:5] + '/' + str(value)[5] + '-' + str(value)[6:9])
                else:
                    print(" code must be integers with len 3 or 5.")
                    raise ValueError
            else:
                print(" code must be integers.")
                raise ValueError
        return validateCodeExpl

    @staticmethod
    def isDigit(func):
        def isDigitExpl(x):
            return func(all(map(str.isdigit, x)))
        return isDigitExpl

    @staticmethod
    def isId(func):
        def isIdExpl(jewelry, value):
            if Validation.isDigit(value):
                return func(jewelry, value)
            else:
                raise ValueError
        return isIdExpl

    @staticmethod
    def validateType(func):
        def validateTypeExpl(jewelry, title):
            if Validation.validateStr(title):
                for i in ['rings', 'earrings', 'bracelets']:
                    if title == i:
                        return func(jewelry, title)
                else:
                    print("Error type ")
                    raise ValueError
        return validateTypeExpl

    @staticmethod
    def validateMat(func):
        def validateMatExpl(jewelry, title):
            if Validation.validateStr(title):
                for i in ['gold', 'silver', 'platinum']:
                    if title == i:
                        return func(jewelry, title)
                else:
                    print("Error material ")
                    raise ValueError

        return validateMatExpl

    @staticmethod
    def validateFileName(end=".txt"):
        def validateFileNameDecorator(func):
            def validateFileNameExpl(L, filename):
                if not filename.endswith(end):
                    raise ValueError("Incorrect filename, should end with ." + end + ".")
                return func(L, filename)

            return validateFileNameExpl

        return validateFileNameDecorator

    @staticmethod
    def validate_inp(func):
        def validate_inpExpl(m):
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
                    t = True
                    print("Try one more time!")
                    continue
                except AttributeError:
                    t = True
                    print("Try one more time!")
                    continue
                except NameError:
                    t = True
                    print("Try one more time!")
                    continue
                except FileNotFoundError:
                    t = True
                    print("Try one more time!")
                    continue

        return validate_inpExpl