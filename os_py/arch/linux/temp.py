from scripts.err import Errors as err
from scripts.unit import Unit


def cpu_temperature(unit='C'):
    try:
        temp = '/sys/devices/virtual/thermal/thermal_zone0/temp'
        celsius = int(open(temp).read().strip()) / 1000

        if unit.lower() == 'c':
            return str(round(celsius, 2)) + 'C'
        elif unit.lower() == 'f':
            return str(round((Unit.to_fahrenheit(celsius, 'c')), 2)) + 'F'
        elif unit.lower() == 'k':
            return str(round(Unit.to_kelvin(celsius, 'c'), 2)) + 'K'
    except:
        err().no_permission()
