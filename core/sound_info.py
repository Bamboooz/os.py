import sys
import sounddevice as sd
from core.exception import *


def get_audio_devices():
    if sys.platform == 'win32':
        return sd.query_devices()
    else:
        return unsupported_exception()
