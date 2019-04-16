import collections


class ConfigSection(collections.OrderedDict):
    def __init__(self, i=None):
        super().__init__()
        if i is not None:
            self.__dict__.update(i)
        else:
            super()

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __delitem__(self, key):
        del self.__dict__[key]

    def __contains__(self, key):
        return key in self.__dict__

    def __len__(self):
        return len(self.__dict__)

    def __repr__(self):
        return repr(self.__dict__)

