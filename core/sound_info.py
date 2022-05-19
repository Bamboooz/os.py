import os
import sys
import sounddevice as sd
from core.exception import *


def get_audio_devices():
    if sys.platform == 'win32':
        return sd.query_devices()
    elif sys.platform == 'darwin':
        return
    elif sys.platform == 'linux':
        return os.popen('aplay -l').read()
    else:
        return unsupported_exception()
