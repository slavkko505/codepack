from class_Ll import Ll
import abc
import random


class Strategy(Ll):
    @abc.abstractmethod
    def generate_data(self, data: Ll, pos, param):
        pass


class FirstStrategy(Strategy):
    def generate_data(self, data: Ll, pos, s) -> None:
        while True:
            try:
                a = int(input("Enter number - а "))
                b = int(input("Enter number - b "))
                if a > b:
                    print("a shouldn't be greater than b \n")
                    continue
                break
            except ValueError:
                print('\nEnter number')

        for i in range(s):
            data.append(data.insert(*generator(a, b), pos))

        return data


def generator(a, b):
    yield random.randint(a, b)


class SecondStrategy(Strategy):
    def generate_data(self, data: Ll, pos, filename) -> None:
        with open(filename, "r") as infile:
            for line in infile:
                for x in line.split():
                    data.insert(int(x), pos)
                    pos += 1
        infile.close()
