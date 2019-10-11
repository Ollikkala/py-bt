#!/usr/bin/env python
# Automatic connect to bluetooth Plattan 2 and sets A2DP sink
# Use ''$ con' to connect
import os
# import pyglet

# Connect to 5C:EB:68:75:78:4D (Plattan 2 BT)
info = os.system('bluetoothctl connect 5C:EB:68:75:78:4D')

# Setting sound quality to A2DP
os.system('pacmd set-card-profile bluez_card.5C_EB_68_75_78_4D a2dp_sink')

# Sets volume to 50%
os.system('amixer -D pulse sset Master 60%')
