#!/usr/bin/env python3

class LedMatrix(object):
  def __init__(self, sense):
    self.__sense = sense

  def get_settings(self):
    sense_settings = {}
    for setting in ['rotation', 'low_light']:
      sense_settings[setting] = getattr(self.__sense, setting)
    return sense_settings

  def update_settings(self, body):
    for s_name, s_value in body.items():
      setattr(self.__sense, s_name, s_value)

  def get_pixel(self, x, y):
    return self.__sense.get_pixel(x, y)

  def update_pixel(self, body):
    self.__sense.set_pixel(body["x"], body["y"], body["colour"])

  def get_pixels(self):
    return self.__sense.get_pixels()

  def update_pixels(self, body):
    self.__sense.set_pixels(body)

  def clear(self, body):
    self.__sense.clear(body)

  def flip(self, body):
    attr_mapping = {
      "horizontal": "flip_h",
      "vertical": "flip_v"
    }
    getattr(self.__sense, attr_mapping[body.get("axis")])(body.get("redraw", False))

  def show_letter(self, body):
    self.__sense.show_letter(
      body["letter"],
      body.get("text_colour", [255, 255, 255]),
      body.get("back_colour", [0,0,0])
    )

  def show_message(self, body):
    self.__sense.show_message(
      body["message"],
      body.get("scroll_speed", 0.1),
      body.get("text_colour", [255, 255, 255]),
      body.get("back_colour", [0,0,0])
    )

