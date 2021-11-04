# Var 2
# Створити клас CarReservation, який містить такі поля
# // 1. Id (унікальне число)
# // 2. car (enum: Audi A3, BMW X1, Toyota Yaris, Volkswagen T-Roc, Ford Fiesta, Honda Civic, Volkswagen Golf)
# // 3. start_datetime
#  // 4. end_datetime
#  // 5. name (лиш літери)
# // 6. price (2 цифри після коми)

from Validation import Validation


class Product(object):
    def __init__(self, **kwargs):
        for (prop, default) in kwargs.items():
            setattr(self, prop, kwargs.get(prop, default))

    @property
    def name(self):
        return self._name

    @name.setter
    @Validation.validateStr
    def name(self, value):
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    @Validation.validatePrice
    def price(self, value):
        self._price = value

    @property
    def car(self):
        return self._car

    @car.setter
    @Validation.check_cars
    def car(self, value):
        self._car = value

    @property
    def start_datetime(self):
        return self._start_datetime

    @start_datetime.setter
    @Validation.validateDate
    def start_datetime(self, value):
        self._start_datetime = value

    @property
    def end_datetime(self):
        return self._end_datetime

    @end_datetime.setter
    @Validation.validateDate
    @Validation.isBiggerDate
    def end_datetime(self, value):
        self._end_datetime = value

    @property
    def u_id(self):
        return self._u_id

    @u_id.setter
    @Validation.isId
    def u_id(self, value):
        self._u_id = value


    def __get_dictionary(self):
        return dict((name, getattr(self, name)) for name in dir(self) if not name.startswith('__')
                    and not name.startswith('_') and name != "input_")

    @staticmethod
    def input_(*args):
        d = dict((prop, input(prop + ": ")) for prop in args)
        return d

    def __str__(self):
        return "Product:\n" + '\n'.join("%s : %r" % (key, str(val)) for (key, val)
                                        in self.__get_dictionary().items()) + "\n"
