from __future__ import print_function

import argparse
import logging
import random
import time

try:
    import pygame
    from pygame.locals import K_DOWN
    from pygame.locals import K_LEFT
    from pygame.locals import K_RIGHT
    from pygame.locals import K_SPACE
    from pygame.locals import K_UP
    from pygame.locals import K_a
    from pygame.locals import K_d
    from pygame.locals import K_p
    from pygame.locals import K_q
    from pygame.locals import K_r
    from pygame.locals import K_s
    from pygame.locals import K_w
except ImportError:
    raise RuntimeError('cannot import pygame, make sure pygame package is installed')

try:
    import numpy as np
except ImportError:
    raise RuntimeError('cannot import numpy, make sure numpy package is installed')
    
from PythonClient.carla import image_converter
from PythonClient.carla import sensor
from PythonClient.carla.client import make_carla_client, VehicleControl
from PythonClient.carla.planner.map import CarlaMap
from PythonClient.carla.settings import CarlaSettings
from PythonClient.carla.tcp import TCPConnectionError
from PythonClient.carla.util import print_over_same_line

