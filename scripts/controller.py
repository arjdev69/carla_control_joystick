#!/usr/bin/env python3.5
from modules import import_modules
from modules import button
import pygame
import random
import os
import sys

SystemController = import_modules.SystemController

os.environ["SDL_VIDEO_CENTERED"] = '1'
pygame.init()

RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
ORANGE = (255,180,0)

#The button can be styled in a manner similar to CSS.
BUTTON_STYLE = {"hover_color" : BLUE,
                "clicked_color" : GREEN,
                "clicked_font_color" : BLACK,
                "hover_font_color" : ORANGE,
                "hover_sound" : pygame.mixer.Sound("sound.wav")}

clock = pygame.time.Clock()

class Control(object):
  def __init__(self):
    self.screen = pygame.display.set_mode((500,500))
    self.screen_rect = self.screen.get_rect()
    self.clock = pygame.time.Clock()
    self.done = False
    self.fps = 60.0
    self.color = WHITE
    message = "Start Carla Server"

    self.button = button.Button((0,0,110,25),RED, self.change_color,text=message, **BUTTON_STYLE)
    self.button.rect.center = (70, self.screen_rect.height - 50)
    self.button2 = button.Button((0,0,50,50),RED, self.change_color,text="ola", **BUTTON_STYLE)
    self.button2.rect.center = (self.screen_rect.centerx,110)

  def change_color(self):
    self.color = [random.randint(0,255) for _ in range(3)]

  def event_loop(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.done = True
      self.button.check_event(event)
      self.button2.check_event(event)

  def start_joystick(self):
    pygame.joystick.init()
  
  def joystick_loop(self):
    joystick = SystemController.init_joystick(self.screen)
    if joystick != 0:
      SystemController.get_axes_buttons_control(joystick, self.screen)
      pygame.display.flip()

  def main_loop(self):
    while not self.done:
      self.event_loop()
      self.screen.fill(self.color)
      self.button.update(self.screen)
      self.button2.update(self.screen)
      self.joystick_loop()
      pygame.display.update()
      self.clock.tick(self.fps)

if __name__ == "__main__":
  run_it = Control()
  run_it.start_joystick()
  run_it.main_loop()
  pygame.quit()
  sys.exit()