#!/usr/bin/env python3
import sys
from sense_wrappers import sensors, led_matrix

if "emulation" in sys.argv:
  from sense_emu import SenseHat
else:
  from sense_hat import SenseHat

sense = SenseHat()
sensors = sensors.Sensors(sense)
led = led_matrix.LedMatrix(sense)
