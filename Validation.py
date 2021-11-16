from datetime import datetime
import re
import enam


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
            datetime.strptime(date, '%Y-%m-%d %H:%M')
            return func(jewelry, date)
        return validateDateExpl

    @staticmethod
    def isBiggerDate(func):
        def isBiggerDateWrapper(product, date2):
            if product.start_datetime > date2 and product.start_datetime - date2 < '24':
                raise ValueError("Incorrect data, start_datetime must be lover than end_datetime.")
            func(product, date2)

        return isBiggerDateWrapper

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
    def check_cars(func):
        def func_wrapper(self, info):
            if str(info).lower() not in enam.Cars.__members__:
                print("That cars " + info + " is not listed in Enum")
            func(self, info)

        return func_wrapper

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
    def validateInt(func):
        def validateIntWrapper(moment, value):
            try:
                v = int(value)
            except ValueError:
                raise ValueError("Not an integer.")
            return func(moment, v)

        return validateIntWrapper

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