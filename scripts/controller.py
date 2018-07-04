#!/usr/bin/env python3.5
from modules import ControlSystem
import pygame, sys

if __name__ == "__main__":
  run_it = ControlSystem.Control()
  run_it.start_joystick()
  run_it.main_loop()
  pygame.quit()
  sys.exit()