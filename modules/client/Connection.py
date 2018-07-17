#!/usr/bin/env python3.5
from __future__ import print_function

import argparse
import logging
import random
import threading
import time
    
from modules.client.carla import image_converter
from modules.client.carla import sensor
from modules.client.carla.client import make_carla_client, VehicleControl
from modules.client.carla.planner.map import CarlaMap
from modules.client.carla.settings import CarlaSettings
from modules.client.carla.tcp import TCPConnectionError
from modules.client.carla.util import print_over_same_line
from modules.joystick import SystemController

autopilot = False
clientSide = ""
class ControlClient(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self._stop_event = threading.Event()

  def stop(self):
    self._stop_event.set()

  def stopped(self):
    return self._stop_event.is_set()

  def run_client(self):
    global clientSide
    frames_per_episode = 30 * 600000
    with make_carla_client("localhost", 2000) as client:
      print("CarlaClient connected")
      clientSide = client
      settings = CarlaSettings()
      settings.set(
          SynchronousMode=True,
          SendNonPlayerAgentsInfo=True,
          NumberOfVehicles=20,
          NumberOfPedestrians=50,
          WeatherId=random.choice([1, 3, 7, 8, 14]))
      settings.randomize_seeds()

      scene = clientSide.load_settings(settings)

      # Choose one player start at random.
      number_of_player_starts = len(scene.player_start_spots)
      player_start = random.randint(0, max(0, number_of_player_starts - 1))

      # Notify the server that we want to start the episode at the
      # player_start index. This function blocks until the server is ready
      # to start the episode.
      print('Starting new episode at %r...' % scene.map_name)
      clientSide.start_episode(player_start)
        
      for frame in range(0, frames_per_episode):
        measurements, sensor_data = client.read_data()
        self.control_vechile(measurements)

  def control_vechile(self,measurements):
    global clientSide; global autopilot
    if not autopilot:
      clientSide.send_control()
    else:
      self.autopilot_control(measurements)
  
  def autopilot_control(self,measurements):
    global clientSide
    # Together with the measurements, the server has sent the
    # control that the in-game autopilot would do this frame. We
    # can enable autopilot by sending back this control to the
    # server. We can modify it if wanted, here for instance we
    # will add some noise to the steer.

    control = measurements.player_measurements.autopilot_control
    #control.steer += 0.0random.uniform(-0.1, 0.1)
    clientSide.send_control(control)

  def pilots_control(control):
    global clientSide; global autopilot
    if not autopilot:
      clientSide.send_control(control)

  def set_autopilot(self):
    global autopilot
    autopilot = not autopilot

  def run(self):
    test_connection = 2
    while True:
      try:
        self.run_client()
        break
      except TCPConnectionError as error:
        logging.error(error)
        time.sleep(1)
        test_connection += -1
        if test_connection <=0:
          break