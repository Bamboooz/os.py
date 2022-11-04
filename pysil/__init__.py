from core import system_info, cpu_info, gpu_info, ram_info, machine_info, storage_info, network_info, motherboard_info, \
    display_info, battery_info, sound_info, device_info


class system:
    @staticmethod
    def os_name():
        return system_info.os_name()

    @staticmethod
    def os_version():
        return system_info.os_version()

    @staticmethod
    def linux_distro():
        return system_info.linux_distro()

    @staticmethod
    def os_platform():
        return system_info.os_platform()

    @staticmethod
    def os_release():
        return system_info.os_release()

    @staticmethod
    def os_architecture():
        return system_info.os_architecture()

    @staticmethod
    def process_list():
        return system_info.process_list()

    @staticmethod
    def os_antivirus():
        return system_info.os_antivirus()

    @staticmethod
    def os_uptime():
        return system_info.os_uptime()


class cpu:
    @staticmethod
    def cpu_model():
        return cpu_info.cpu_model()

    @staticmethod
    def cpu_clockspeed():
        return cpu_info.cpu_clockspeed()

    @staticmethod
    def cpu_architecture():
        return cpu_info.cpu_architecture()

    @staticmethod
    def cpu_processor_number():
        return cpu_info.cpu_processor_number()

    @staticmethod
    def cpu_usage():
        return cpu_info.cpu_usage()

    @staticmethod
    def cpu_temperature():
        return cpu_info.cpu_temperature()

    @staticmethod
    def cpu_vendor_id():
        return cpu_info.cpu_vendor_id()


class gpu:
    @staticmethod
    def gpu_id():
        return gpu_info.gpu_id()

    @staticmethod
    def gpu_name():
        return gpu_info.gpu_name()

    @staticmethod
    def gpu_load():
        return gpu_info.gpu_load()

    @staticmethod
    def gpu_free_memory():
        return gpu_info.gpu_free_memory()

    @staticmethod
    def gpu_used_memory():
        return gpu_info.gpu_used_memory()

    @staticmethod
    def gpu_total_memory():
        return gpu_info.gpu_total_memory()

    @staticmethod
    def gpu_temperature():
        return gpu_info.gpu_temperature()


class ram:
    @staticmethod
    def ram_total_memory():
        return ram_info.ram_total_memory()

    @staticmethod
    def ram_manufacturer():
        return ram_info.ram_manufacturer()

    @staticmethod
    def ram_serial_number():
        return ram_info.ram_serial_number()

    @staticmethod
    def ram_memory_type():
        return ram_info.ram_memory_type()

    @staticmethod
    def ram_form_factor():
        return ram_info.ram_form_factor()

    @staticmethod
    def ram_clockspeed():
        return ram_info.ram_clockspeed()

    @staticmethod
    def ram_usage():
        return ram_info.ram_usage()


class storage:
    @staticmethod
    def drive_list():
        return storage_info.drive_list()

    @staticmethod
    def get_total_space(drive_letter=None):
        return storage_info.get_total_space(drive_letter)

    @staticmethod
    def get_used_space(drive_letter=None):
        return storage_info.get_used_space(drive_letter)

    @staticmethod
    def get_free_space(drive_letter=None):
        return storage_info.get_free_space(drive_letter)

    @staticmethod
    def get_used_space_percent(drive_letter=None):
        return storage_info.get_used_space_percent(drive_letter)

    @staticmethod
    def get_drive_fstype(drive_letter=None):
        return storage_info.get_drive_fstype(drive_letter)

    @staticmethod
    def get_drive_mountpoint(drive_letter=None):
        return storage_info.get_drive_mountpoint(drive_letter)


class motherboard:
    @staticmethod
    def motherboard_model():
        return motherboard_info.motherboard_model()

    @staticmethod
    def motherboard_manufacturer():
        return motherboard_info.motherboard_manufacturer()

    @staticmethod
    def motherboard_serial_number():
        return motherboard_info.motherboard_serial_number()

    @staticmethod
    def motherboard_version():
        return motherboard_info.motherboard_version()

    @staticmethod
    def motherboard_node():
        return motherboard_info.motherboard_node()


class machine:
    @staticmethod
    def machine_name():
        return machine_info.machine_name()

    @staticmethod
    def bios_type():
        return machine_info.bios_type()


class display:
    @staticmethod
    def display_device():
        return display_info.display_device()

    @staticmethod
    def screen_resolution():
        return display_info.screen_resolution()

    @staticmethod
    def screen_refresh_frequency():
        return display_info.screen_refresh_frequency()


class battery:
    @staticmethod
    def battery_percentage():
        return battery_info.battery_percentage()

    @staticmethod
    def is_plugged_in():
        return battery_info.is_plugged_in()

    @staticmethod
    def battery_time_left():
        return battery_info.battery_time_left()


class sound:
    @staticmethod
    def get_audio_devices():
        return sound_info.get_audio_devices()


class device:
    @staticmethod
    def get_usb_list():
        return device_info.get_usb_list()


class network:
    @staticmethod
    def get_ipv4():
        return network_info.get_ipv4()

    @staticmethod
    def get_ipv6():
        return network_info.get_ipv6()

    @staticmethod
    def get_subnet_mask():
        return network_info.get_subnet_mask()

    @staticmethod
    def get_default_gateway():
        return network_info.get_default_gateway()

    @staticmethod
    def get_hostname():
        return network_info.get_hostname()

    @staticmethod
    def is_connected():
        return network_info.is_connected()

    @staticmethod
    def get_ping_time():
        return network_info.get_ping_time()

    @staticmethod
    def get_download_speed():
        return network_info.get_download_speed()

    @staticmethod
    def get_upload_speed():
        return network_info.get_upload_speed()
