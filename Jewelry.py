# Клас "JEWELRY" з полями: ID, title, code(*****/*-**), price, data_of_creation (date),
# material(gold/silver/platinum), type(rings/earrings/bracelets).

from Validation import Validation


class Product(object):
    def __init__(self, **kwargs):
        for (prop, default) in kwargs.items():
            setattr(self, prop, kwargs.get(prop, default))

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = Validation.validateStr(value)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = Validation.validatePrice(value)

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = Validation.validateCode(value)

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        n = input("Enter 'free' if you wont put your material of jewelry or skip this to 'enter' (defoult is gold, silver or platinum) \n")
        if n == 'free':
            self._material = Validation.validateStr(value)
        else:
            self._material = Validation.validateMaterial(value)

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        n = input("Enter 'free' if you wont put your type of jewelry or skip this to 'enter' (defoult is rings, earrings or bracelets)\n")
        if n == 'free':
            self._type = Validation.validateStr(value)
        else:
            self._type = Validation.validateType(value)

    @property
    def date_of_creation(self):
        return self._date_of_creation

    @date_of_creation.setter
    def date_of_creation(self, value):
        self._date_of_creation = Validation.validateDate(value)

    @property
    def u_id(self):
        return self._u_id

    @u_id.setter
    def u_id(self, value):
        self._u_id = Validation.isId(value)


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
