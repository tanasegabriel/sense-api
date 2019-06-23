#!/usr/bin/env python3
from sense_hat import SenseHat
from sense_wrappers import sensors, led_matrix

sense = SenseHat()
sensors = sensors.Sensors(sense)
led = led_matrix.LedMatrix(sense)
