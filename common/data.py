class ospylib_data_format:
    def __init__(self, **kwargs):
        self._attributes = {name: value for name, value in kwargs.items()}

    def __getattr__(self, name):
        if name is None:
            print('is none')

        if name not in self._attributes:
            raise AttributeError(f"Requested object '{name}' does not exist.")

        function, is_callable = self._attributes[name]
        return function() if is_callable else function

    def __setattr__(self, name, value):
        if name not in ["_attributes"]:
            raise AttributeError("Cannot set attribute value on 'ospylib_data'")

        super().__setattr__(name, value)

    def __repr__(self):
        attributes = {}

        for attribute, value in self._attributes.items():
            attributes[attribute] = value[0]() if value[1] is True else value[0]

        return repr(attributes)


def a():
    print('a')
    return 'a'

def b():
    print('b')
    return 'b'

def c():
    print('c')
    return 'c'

def bla():
    ind = ospylib_data_format(b=(b, True), c=(c, True))
    return ospylib_data_format(a=(a, True), b=(ind, False))

print(bla())

