import os


def get_audio_devices():
    return os.popen('aplay -l').read()
