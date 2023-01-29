class Unit:
    @staticmethod
    def to_celsius(val, _type):
        return {
            'c': val,
            'f': ((val - 32) * 5) / 9,
            'k': val - 273.15
        }.get(_type.lower())

    @staticmethod
    def to_fahrenheit(val, _type):
        return {
            'c': (val * 1.8) + 32,
            'f': val,
            'k': (val * (9 / 5)) - 459.67
        }.get(_type.lower())

    @staticmethod
    def to_kelvin(val, _type):
        return {
            'c': val + 273.15,
            'f': (val + 459.67) * (5 / 9),
            'k': val
        }.get(_type.lower())


class Handler:
    @staticmethod
    def exception(err_code):
        raise Exception(err_code)
