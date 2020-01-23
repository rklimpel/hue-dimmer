#!/usr/bin/env python3

from phue import Bridge
import json
import time

b = Bridge('192.168.0.106')

b.connect()

#with open('data.json', 'w') as fp:
#	json.dump(b.get_api(), fp, sort_keys=True, indent=4)

lights = b.lights

dim_time = 60*1
step_time = dim_time/(255/5)
if step_time >= 30:
	trans_time = 30
	wait_time = step_time - trans_time
else:
	trans_time = step_time
	wait_time = 0

print("step_time: " + str(step_time))
print("trans_time: " + str(trans_time))
print("dim_time: " + str(dim_time))

for light in lights:
	light.on = True

for brightness in range(255,0,-5):
	print("Set brightness to " + str(brightness))
	for light in lights:
		light.transitiontime = trans_time
		light.brightness = brightness
	time.sleep(wait_time)

for light in lights:
	light.on = False



