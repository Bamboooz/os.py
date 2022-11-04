import os
import sys
import sounddevice as sd
from core.exception import *


def get_audio_devices():
    if sys.platform == 'win32':
        return sd.query_devices()
    elif sys.platform == 'darwin':
        print(unsupported_exception())
    elif sys.platform == 'linux':
        return os.popen('aplay -l').read()
    else:
        print(unsupported_exception())
