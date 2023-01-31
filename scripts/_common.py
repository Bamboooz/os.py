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

    @staticmethod
    def hz_short_to_full(ticks, scale):
        try:
            # Make sure the number can be converted to a float
            ticks = float(ticks)
            ticks = '{0}'.format(ticks)

            # Scale the numbers
            hz = ticks.lstrip('0')
            old_index = hz.index('.')
            hz = hz.replace('.', '')
            hz = hz.ljust(scale + old_index + 1, '0')
            new_index = old_index + scale
            hz = '{0}.{1}'.format(hz[:new_index], hz[new_index:])
            left, right = hz.split('.')
            left, right = int(left), int(right)
            return left, right
        except Exception:
            return 0, 0

    def hz_short_to_friendly(self, ticks, scale):
        try:
            # Get the raw Hz as a string
            left, right = self.hz_short_to_full(ticks, scale)
            result = '{0}.{1}'.format(left, right)

            # Get the location of the dot, and remove said dot
            dot_index = result.index('.')
            result = result.replace('.', '')

            # Get the Hz symbol and scale
            symbol = "Hz"
            scale = 0
            if dot_index > 9:
                symbol = "GHz"
                scale = 9
            elif dot_index > 6:
                symbol = "MHz"
                scale = 6
            elif dot_index > 3:
                symbol = "KHz"
                scale = 3

            # Get the Hz with the dot at the new scaled point
            result = '{0}.{1}'.format(result[:-scale - 1], result[-scale - 1:])

            # Format the ticks to have 4 numbers after the decimal
            # and remove any superfluous zeroes.
            result = '{0:.4f} {1}'.format(float(result), symbol)
            result = result.rstrip('0')
            return result
        except Exception:
            return '0.0000 Hz'


class Handler:
    @staticmethod
    def exception(err_code):
        raise Exception(err_code)
