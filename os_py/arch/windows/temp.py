import wmi
from scripts.err import Errors as err
from scripts.unit import Unit


def cpu_temperature(unit='C'):
    try:
        w_temp = wmi.WMI(namespace="root\\wmi")
        kelvin_value = (w_temp.MSAcpi_ThermalZoneTemperature()[0].CurrentTemperature / 10.0)

        if unit.lower() == 'c':
            return str(round(Unit.to_celsius(kelvin_value, 'k'), 2)) + 'C'
        elif unit.lower() == 'f':
            return str(round((Unit.to_fahrenheit(kelvin_value, 'k')), 2)) + 'F'
        elif unit.lower() == 'k':
            return str(round(kelvin_value, 2)) + 'K'
    except:
        err().no_permission()
