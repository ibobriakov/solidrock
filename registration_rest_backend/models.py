__author__ = 'ir4y'


class AbstractObject(object):
    def __init__(self, initial=None):
        self.__dict__['_data'] = {}
        if hasattr(initial, 'items'):
            self.__dict__['_data'] = initial

    def __getattr__(self, name):
        return self._data.get(name, None)

    __getitem__ = __getattr__

    def __setattr__(self, name, value):
        self.__dict__['_data'][name] = value

    def to_dict(self):
        return self._data


class AbstractUserObject(AbstractObject):
    pass


class ActivationObject(AbstractObject):
    pass


class LoginObject(AbstractObject):
    pass