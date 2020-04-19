import keyword
from collections import namedtuple


class ColorizeMixin(object):

    def __init__(self):
        self.repr_color_code = 33

    def __repr__(self):
        return f'\033[1;{self.repr_color_code};40m'


class JSONMapper:

    def __init__(self, mapping):
        if not isinstance(mapping, dict):
            raise TypeError('Incorrect file type: Not a DICT object.')

        for name, value in mapping.items():
            if isinstance(value, dict):
                self.__setattr__(name, namedtuple('WrappedMapping', value.keys())(*value.values()))
            else:
                self.__setattr__(name, value)


class Advert(JSONMapper, ColorizeMixin):
    repr_color_code = 32

    def __init__(self, mapping):
        super().__init__(mapping)
        if not self.__dict__.get('price'):
            self.price = 0

    def __setattr__(self, name, value):
        if name == 'price' and value < 0:
            raise ValueError('Incorrect price value: Price must be greater or equal 0.')
        if keyword.iskeyword(name):
            name += '_'
        self.__dict__[name] = value

    def __repr__(self):
        end = '\033[0m'
        return super().__repr__() + f'{self.title} | {self.price} ₽' + end
