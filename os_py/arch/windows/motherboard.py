import subprocess
import uuid


def motherboard_model():
    model = subprocess.check_output('wmic baseboard get product').decode().split('\n')[1].strip()
    return model


def motherboard_manufacturer():
    manufacturer = subprocess.check_output('wmic baseboard get Manufacturer').decode().split('\n')[1].strip()
    return manufacturer


def motherboard_serial_number():
    serial_id = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    return serial_id


def motherboard_version():
    version = subprocess.check_output('wmic baseboard get version').decode().split('\n')[1].strip()
    return version


def motherboard_node():
    return uuid.getnode()
