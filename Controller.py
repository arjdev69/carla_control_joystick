#!/usr/bin/env python3.5
from modules.joystick import ControlSystem
import pygame, sys

if __name__ == "__main__":
  
  try:
    run_it = ControlSystem.Control()
    run_it.main_loop()
    pygame.quit()
    sys.exit()

  except KeyboardInterrupt:
    print('\nCancelled by user. Bye!')