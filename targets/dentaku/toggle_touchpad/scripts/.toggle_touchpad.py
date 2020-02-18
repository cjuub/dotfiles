#!/usr/bin/env python3

import subprocess
import sys

force_mode = None
if len(sys.argv) > 1:
    force_mode = sys.argv[1]

cmd = 'xinput list'
result = subprocess.run(cmd.split(' '), stdout=subprocess.PIPE, text=True)

touchpad_id = -1
for line in result.stdout.split('\n'):
    line = str(line)
    if 'Touchpad' in line:
        id_index = line.find('id=')
        touchpad_id = int(line[id_index + 3: id_index + 5])
        break
else:
    assert False, 'Could not find touchpad id'

cmd = 'xinput list-props ' + str(touchpad_id)
result = subprocess.run(cmd.split(' '), stdout=subprocess.PIPE, text=True)


device_enabled_id = -1
natural_scoll_enabled_id = -1
speed_id = -1
tapping_enabled_id = -1

device_enabled_curr_value = -1

for line in result.stdout.split('\n'):
    if 'Natural Scrolling Enabled (' in line:
        natural_scoll_enabled_id = line.split(':')[0][-4:-1]
    elif 'Tapping Enabled (' in line:
        tapping_enabled_id = line.split(':')[0][-4:-1]
    elif 'Accel Speed (' in line:
        speed_id = line.split(':')[0][-4:-1]
    elif 'Device Enabled (' in line:
        device_enabled_id = line.split(':')[0][-4:-1]
        device_enabled_curr_value = int(line.split(':')[1].strip())

if force_mode == 'on' or device_enabled_curr_value == 0:
    for prop_id, value in [(device_enabled_id, 1),
                           (natural_scoll_enabled_id, 1),
                           (speed_id, 0.5),
                           (tapping_enabled_id, 1)]:
        cmd = 'xinput set-prop ' + str(touchpad_id) + ' ' + str(prop_id) + ' ' + str(value)
        subprocess.check_call(cmd.split(' '))
else:
    for prop_id, value in [(device_enabled_id, 0)]:
        cmd = 'xinput set-prop ' + str(touchpad_id) + ' ' + str(prop_id) + ' ' + str(value)
        subprocess.check_call(cmd.split(' '))
