#!/usr/bin/env python3

from phue import Bridge
import json
import time
import sys


dim_direction = sys.argv[1]
dim_duration = sys.argv[2]

b = Bridge('192.168.0.106')
b.connect()
lights = b.lights

#with open('data.json', 'w') as fp:
#	json.dump(b.get_api(), fp, sort_keys=True, indent=4)

dim_time = 60*int(dim_duration)
step_time = dim_time/(255/1)

print("step_time: " + str(step_time))
print("dim_time: " + str(dim_time))

if dim_direction == "up":
	value_from = 0
	value_to = 255
	value_inc = 1
elif dim_direction == "down":
	value_from = 255
	value_to = 0
	value_inc = -1

for light in lights:
	light.on = True

for brightness in range(value_from,value_to,value_inc):
	print("Set brightness to " + str(brightness))
	for light in lights:
		light.transitiontime = 3
		light.brightness = brightness
	time.sleep(step_time)

if dim_direction == "down":
	for light in lights:
		light.on = False



