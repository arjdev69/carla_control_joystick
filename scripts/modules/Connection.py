#!/usr/bin/env python3.5
from __future__ import print_function

import argparse
import logging
import random
import threading
import time
    
from modules.PythonClient.carla import image_converter
from modules.PythonClient.carla import sensor
from modules.PythonClient.carla.client import make_carla_client, VehicleControl
from modules.PythonClient.carla.planner.map import CarlaMap
from modules.PythonClient.carla.settings import CarlaSettings
from modules.PythonClient.carla.tcp import TCPConnectionError
from modules.PythonClient.carla.util import print_over_same_line

autopilot = True
class ControlClient(threading.Thread):

  def __init__(self):
    threading.Thread.__init__(self)


  def run_client(self):
    frames_per_episode = 30000000
    with make_carla_client("localhost", 2000) as client:
      print("CarlaClient connected")

      settings = CarlaSettings()
      settings.set(
          SynchronousMode=True,
          SendNonPlayerAgentsInfo=True,
          NumberOfVehicles=200,
          NumberOfPedestrians=180,
          WeatherId=random.choice([1, 3, 7, 8, 14]))
      settings.randomize_seeds()

      scene = client.load_settings(settings)

      # Choose one player start at random.
      number_of_player_starts = len(scene.player_start_spots)
      player_start = random.randint(0, max(0, number_of_player_starts - 1))

      # Notify the server that we want to start the episode at the
      # player_start index. This function blocks until the server is ready
      # to start the episode.
      print('Starting new episode at %r...' % scene.map_name)
      client.start_episode(player_start)
        
      for frame in range(0, frames_per_episode):
        measurements, sensor_data = client.read_data()
        if not autopilot:

          client.send_control(
          steer=random.uniform(-1.0, 1.0),
          throttle=0.5,
          brake=0.0,
          hand_brake=False,
          reverse=False)

        else:

          # Together with the measurements, the server has sent the
          # control that the in-game autopilot would do this frame. We
          # can enable autopilot by sending back this control to the
          # server. We can modify it if wanted, here for instance we
          # will add some noise to the steer.

          control = measurements.player_measurements.autopilot_control
          control.steer += random.uniform(-0.1, 0.1)
          client.send_control(control)

  def run(self):
    while True:
      try:

        self.run_client()

        print('Done.')
        return

      except TCPConnectionError as error:
        logging.error(error)
        time.sleep(1)