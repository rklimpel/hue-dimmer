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
trans_time = dim_time/(255/5)
print(trans_time)

for light in lights:
	light.on = True

for brightness in range(255,0,-5):
	print("Set brightness to " + str(brightness))
	for light in lights:
		light.transitiontime = 0
		light.brightness = brightness
	time.sleep(trans_time)

for light in lights:
	light.on = False



