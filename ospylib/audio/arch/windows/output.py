import ctypes

MMSYSERR_NOERROR = 0x00000000
waveOutGetNumDevs = ctypes.windll.winmm.waveOutGetNumDevs
waveOutGetDevCaps = ctypes.windll.winmm.waveOutGetDevCapsA

class WAVEOUTCAPS(ctypes.Structure):
    _fields_ = [
        ('wMid', ctypes.c_uint16),
        ('wPid', ctypes.c_uint16),
        ('vDriverVersion', ctypes.c_uint32),
        ('szPname', ctypes.c_char * 32),
        ('dwFormats', ctypes.c_uint32),
        ('wChannels', ctypes.c_uint16),
        ('wReserved1', ctypes.c_uint16),
        ('dwSupport', ctypes.c_uint32),
    ]


def output_devices():
    device_list = []

    num_devices = waveOutGetNumDevs()
    if num_devices == 0:
        return device_list

    for device_id in range(num_devices):
        caps = WAVEOUTCAPS()
        result = waveOutGetDevCaps(device_id, ctypes.byref(caps), ctypes.sizeof(caps))
        if result == MMSYSERR_NOERROR:
            device_name = caps.szPname.decode('utf-8')
            device_list.append(device_name)

    return device_list