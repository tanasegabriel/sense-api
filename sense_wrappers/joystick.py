#!/usr/bin/env python3


class Joystick(object):
  def __init__(self, sense):
    self.__sense = sense

  def get_events(self):
    events = self.__sense.stick.get_events()[:1000]
    return [self.__event_dict(event) for event in events]

  @staticmethod
  def __event_dict(event):
    return dict(event._asdict())
