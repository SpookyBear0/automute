import gd
import math
import time
import os
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

volume = None; vol = None
sessions = AudioUtilities.GetAllSessions()
for session in sessions:
    if session.Process and session.Process.name() == "Discord.exe":
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        vol = volume.GetMasterVolume()

memory = gd.memory.get_memory()

gettingfar = input("what percent to mute at?: ")
muted = False

while True:
    memory.reload()
    percent = memory.get_percent()
    if math.floor(percent) == int(gettingfar):
        if not muted:
            volume.SetMasterVolume(0, None)
            muted = True
    if memory.is_dead():
        if muted:
            volume.SetMasterVolume(vol, None)
            muted = False
    time.sleep(0.5)