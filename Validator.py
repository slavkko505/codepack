import os

class Validation:
    @staticmethod
    def validateInt(n):
        try:
            n = int(n)
            if n < 0:
                raise ValueError("Input must be a positive integer!")
        except ValueError:
            raise ValueError("Not an integer!")
        return n

    @staticmethod
    def validateFileName(filename, end=".txt"):
        if not filename.endswith(end):
            raise ValueError("Incorrect filename, should end with ." + end + ".")
        if not os.path.isfile(filename):
            raise FileNotFoundError("There's no such" + filename + " file")
        return filename

    @staticmethod
    def validateListGeneration(context):
        if context == None:
            raise UnboundLocalError("You need to choose type of generation first.")
        return context

    @staticmethod
    def validate_inp(func):
        def validate_inpWrapper(*l):
            t = False
            while True:
                try:
                    if t:
                        n = input("Enter 'exit' to go back or 'con' to continue \n")
                        if n == "exit":
                            break
                        elif n == "con":
                            func(*l)
                            break
                        else:
                            continue
                    func(*l)
                    break
                except UnboundLocalError as e:
                    t = True
                    print(e)
                    print("Try one more time!")
                    break
                except ValueError as e:
                    t = True
                    print(e)
                    print("Try one more time!")
                    continue
                except AttributeError as e:
                    t = True
                    print(e)
                    print("Try one more time!")
                    continue
                except NameError as e:
                    t = True
                    print(e)
                    print("Try one more time!")
                    continue
                except FileNotFoundError as e:
                    t = True
                    print(e)
                    print("Try one more time!")
                    continue
                except IndexError as e:
                    t = True
                    print(e)
                    print("Try one more time!")
                    continue
        return validate_inpWrapper
