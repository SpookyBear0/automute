import gd
import math
import time
import os
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import sys

try:
    app_to_mute = sys.argv[1]
except IndexError:
    app_to_mute = "Discord.exe"
    
# setup volume
volume = None; vol = None
sessions = AudioUtilities.GetAllSessions()
for session in sessions:
    if session.Process and session.Process.name() == app_to_mute:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        vol = volume.GetMasterVolume()

# vars
memory = gd.memory.get_memory()
muted = False
gettingfar = input("what percent to mute at?: ")

# mainloop
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