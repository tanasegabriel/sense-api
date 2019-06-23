#!/usr/bin/env python3

class Sensors(object):
  def __init__(self, sense):
    self.__sense = sense

  def humidity(self):
    return self.__u_v_dict("percentage", self.__sense.get_humidity())

  def temperature(self):
    return {
      "from_pressure": self.__u_v_dict("celsius", self.__sense.get_temperature_from_pressure()),
      "from_humidity": self.__u_v_dict("celsius", self.__sense.get_temperature_from_humidity())
    }

  def pressure(self):
    return self.__u_v_dict("millibars", self.__sense.get_pressure())

  def orientation(self):
    return [
      self.__u_v_dict("radians", self.__sense.get_orientation_radians()),
      self.__u_v_dict("degrees", self.__sense.get_orientation_degrees())
    ]

  def compass(self):
    return {
      "north_direction": self.__u_v_dict("degrees", self.__sense.get_compass()),
      "magnetic_intensity": self.__u_v_dict("microteslas", self.__sense.get_compass_raw())
    }

  def gyroscope(self):
    return {
      "axis_angle": self.__u_v_dict("degrees", self.__sense.get_gyroscope()),
      "axis_rotational_intensity": self.__u_v_dict("radians/second", self.__sense.get_gyroscope_raw())
    }

  def accelerometer(self):
    return {
      "axis_angle": self.__u_v_dict("degrees", self.__sense.get_accelerometer()),
      "axis_acceleration_intensity": self.__u_v_dict("G", self.__sense.get_accelerometer_raw()),
    }

  def get(self, name):
    return getattr(self, name)()

  def __u_v_dict(self, u, v):
    return {"unit": u, "value": v}


