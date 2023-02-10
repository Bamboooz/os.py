from os_py import *

print('', system.os_name())
print('', system.os_version())
print('', system.os_platform())
print('', system.os_release())
print('', system.os_architecture())
print('', system.machine_architecture())
print('', system.linux_distro())

print('', cpu.cpu_model())
print('', cpu.cpu_total_cores())
print('', cpu.cpu_clockspeed())
print('', cpu.cpu_architecture())
print('', cpu.cpu_bits())
print('', cpu.cpu_manufacturer())
print('', cpu.cpu_vendor_id())

print('', gpu().gpu_id())
print('', gpu().gpu_name())
print('', gpu().gpu_serial_number())
print('', gpu().gpu_uuid())
print('', gpu().gpu_memory_total())
print('', gpu().gpu_memory_free())
print('', gpu().gpu_memory_used())
print('', gpu().gpu_display_mode())
print('', gpu().gpu_display_active())

# print('', ram.ram_capacity())
# print('', ram.ram_form_factor())
# print('', ram.ram_memory_type())
# print('', ram.ram_manufacturer())
# print('', ram.ram_clockspeed())
# print('', ram.ram_serial_number())

print('', storage.drive_list())
print('', storage().get_total_space())
print('', storage().get_used_space())
print('', storage().get_free_space())
print('', storage().get_used_space_percent())

print('', motherboard.model())
print('', motherboard.manufacturer())
print('', motherboard.serial_number())
print('', motherboard.version())
print('', motherboard.node())

print('', device.lst_extern_drives())

print('', sound.get_sound_devices())

print('', battery.battery_percentage())
print('', battery.is_plugged_in())
print('', battery.battery_time_left())

print('', network.get_ipv4())
print('', network.get_ipv6())
print('', network.get_subnet_mask())
print('', network.get_default_gateway())
print('', network.is_connected())
print('', network.get_hostname())
print('', network.get_ping_time())
print('', network.user_download_speed())
print('', network.user_upload_speed())

print('', machine.machine_name())
print('', machine.boot_type())