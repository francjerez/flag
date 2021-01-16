#!/usr/bin/python3

import sys
import hid
import time
import subprocess

dev = hid.device() 

def col(flg):
  dev.open(0x04d8, 0xf372)
  if flg == 1:
    dev.write([0, 0, 82, 0, 0, 0, 0, 0])# Red    (busy)
  if flg == 2:
    dev.write([0, 0, 71, 0, 0, 0, 0, 0])# Green  (free)
  if flg == 3:
    dev.write([0, 0, 66, 0, 0, 0, 0, 0])# Blue   (away)
  dev.close()

# Off
if sys.argv[-1] == "logout":
  col(3)

# On
else:
  flg = 3
  pre =-1
  while True:
    time.sleep(0.5)

    # Display is sleeping
    if b"Asleep" in subprocess.check_output(['system_profiler', 'SPDisplaysDataType']):
      flg = 3

    # DND is disabled
    elif subprocess.check_output(['defaults', 'read', 'com.apple.ncprefs.plist', 'dnd_prefs'])[-11:-3] == b'0000007c':
      flg = 2

    # DND is enabled
    else:
      flg = 1

    if pre != flg:
      col(flg)
    pre = flg 
