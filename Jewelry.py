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
    @Validation.validateStr
    def title(self, value):
        self._title = value

    @property
    def price(self):
        return self._price

    @price.setter
    @Validation.validatePrice
    def price(self, value):
        self._price = value

    @property
    def code(self):
        return self._code

    @code.setter
    @Validation.validateCode
    def code(self, value):
        self._code = value

    @property
    def material(self):
        return self._material

    @material.setter
    @Validation.validateMat
    def material(self, value):
        self._material = value

    @property
    def type(self):
        return self._type

    @type.setter
    @Validation.validateType
    def type(self, value):
         self._type = value

    @property
    def date_of_creation(self):
        return self._date_of_creation

    @date_of_creation.setter
    @Validation.validateDate
    def date_of_creation(self, value):
        self._date_of_creation = value

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

    def __repr__(self):
        return "Product:\n" + '\n'.join("%s : %r" % (key2, str(val2)) for (key2, val2)
                                        in self.__get_dictionary().items()) + "\n"