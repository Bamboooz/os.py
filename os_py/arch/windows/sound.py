import sounddevice as sd


def get_audio_devices():
    return sd.query_devices()
