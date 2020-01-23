# hue-dimmer

The light in my room is controlled by a Philips Hue Bridge, but consists of a mixture of Philips Hue bulbs and Ikea Treadfri bulbs. Since the function from the Hue app to dim the lamps in the evening and to get up in the mornings sometimes doesn't work with the Tradfri lights, here is the attempt to do the dimming manually.

The python script is executed on my raspberry and triggered by a cronjob and will hopefully wake me up in the morning with nice light.

The whole thing will look something like this:

```python

40 23 * * * /home/pi/code/hue-dimmer/hue-dimmer.py down 15
50 6 * * * /home/pi/code/hue-dimmer/hue-dimmer.py up 35
