import psutil


def battery_percentage():
    percent = str(psutil.sensors_battery().percent)
    return percent + '%'


def is_plugged_in():
    return psutil.sensors_battery().power_plugged


def battery_time_left():
    if is_plugged_in():
        return 'Device is charging...'
    else:
        return str(round(psutil.sensors_battery().secsleft / 60 / 60)) + 'h'
