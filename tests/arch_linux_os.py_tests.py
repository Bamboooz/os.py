from os_py import *

print('OS name: ', system.os_name())
print('OS version: ', system.os_version())
print('OS platform: ', system.os_platform())
print('OS release: ', system.os_release())
print('OS architecture: ', system.os_architecture())
print('Machine architecture', system.machine_architecture())
print('Linux distro', system.linux_distro())

print('CPU model:', cpu.cpu_model())
print('CPU total cores: ', cpu.cpu_total_cores())
print('CPU clockspeed: ', cpu.cpu_clockspeed())
print('CPU architecture: ', cpu.cpu_architecture())
print('CPU bits: ', cpu.cpu_bits())
print('CPU manufacturer: ', cpu.cpu_manufacturer())
print('CPU vendor id: ', cpu.cpu_vendor_id())

print('GPU id: ', gpu().gpu_id())
print('GPU model: ', gpu().gpu_name())
print('GPU serial number: ', gpu().gpu_serial_number())
print('GPU uuid: ', gpu().gpu_uuid())
print('GPU total memory: ', gpu().gpu_memory_total())
print('GPU free memory: ', gpu().gpu_memory_free())
print('GPU used memory: ', gpu().gpu_memory_used())
print('GPU display mode: ', gpu().gpu_display_mode())
print('GPU active display: ', gpu().gpu_display_active())

# print('RAM capacity: ', ram.ram_capacity())
# print('RAM form factor: ', ram.ram_form_factor())
# print('RAM memory type: ', ram.ram_memory_type())
# print('RAM manufacturer: ', ram.ram_manufacturer())
# print('RAM clockspeed: ', ram.ram_clockspeed())
# print('RAM serial number: ', ram.ram_serial_number())

print('Drive list: ', storage.drive_list())
print('Drive total space: ', storage().get_total_space())
print('Drive used space: ', storage().get_used_space())
print('Drive free space: ', storage().get_free_space())
print('Drive used space in percent: ', storage().get_used_space_percent())

print('Motherboard model: ', motherboard.model())
print('Motherboard manufacturer: ', motherboard.manufacturer())
print('Motherboard serial number: ', motherboard.serial_number())
print('Motherboard version: ', motherboard.version())
print('Motherboard node: ', motherboard.node())

print('USB list: ', device.lst_extern_drives())

print('Sound devices: ', sound.get_sound_devices())

print('Battery percentage: ', battery.battery_percentage())
print('Is battery plugged in: ', battery.is_plugged_in())
print('Battery time left: ', battery.battery_time_left())

print('Machine name: ', machine.machine_name())
print('Boot type: ', machine.boot_type())
