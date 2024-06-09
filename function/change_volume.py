from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ai_voice import speak


def basic_setting_to_change():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    return volume


def add_volume(volume):
    device_volume = basic_setting_to_change()
    current_volume = device_volume.GetMasterVolumeLevelScalar()
    volume = round(current_volume, 2) + (int(volume)/100)
    device_volume.SetMasterVolumeLevelScalar(volume, None)
    speak("Я збільшив гучність")


def reduce_volume(volume):
    device_volume = basic_setting_to_change()
    current_volume = device_volume.GetMasterVolumeLevelScalar()
    volume = round(current_volume, 2) - (int(volume)/100)
    device_volume.SetMasterVolumeLevelScalar(volume, None)
    speak("Я зменьшив гучність")
