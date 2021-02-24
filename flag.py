#!/usr/bin/python3

import sys
import hid
import time
import subprocess

vid = 0x04d8#  1240
pid = 0xf372# 62322
dev = hid.device()

def col(flg):
  dev.open(vid, pid)
  if flg == 1:
    dev.write([0, 0, 66, 0, 0, 0, 0, 0])# Blue   (away)
  if flg == 2:
    dev.write([0, 0, 71, 0, 0, 0, 0, 0])# Green  (free)
  if flg == 3:
    dev.write([0, 0, 82, 0, 0, 0, 0, 0])# Red    (busy)
  dev.close()

# Off
if sys.argv[-1] == "logout":
  col(1)

# On
else:
  pre = 0
  while True:
    time.sleep(0.5)

    # Flag is unplugged
    if not hid.enumerate(vid, pid): 
      flg = 0

    # Display is sleeping
    elif b"Asleep" in subprocess.check_output(['system_profiler', 'SPDisplaysDataType']):
      flg = 1

    # DND is disabled
    elif subprocess.check_output(['defaults', 'read', 'com.apple.ncprefs.plist', 'dnd_prefs'])[-11:-3] == b'0000007c':
      flg = 2

    # DND is enabled
    else:
      flg = 3

    if flg and flg != pre:
      col(flg)
    pre = flg 
