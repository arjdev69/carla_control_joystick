from modules.joystick import SystemController
from modules.button import button
from modules.joystick import PrintText
from modules.client import Connection

import pygame
import random
import os
import sys
import subprocess

SystemController = SystemController
TextOutput = PrintText.TextPrint()

os.environ["SDL_VIDEO_CENTERED"] = '1'
pygame.init()

RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
ORANGE = (255,180,0)
joystick = []
i = 0
#The button can be styled in a manner similar to CSS.
BUTTON_STYLE = {"hover_color" : BLUE
                , "clicked_color" : GREEN
                , "clicked_font_color" : BLACK
                , "hover_font_color" : ORANGE
                , "hover_sound" : pygame.mixer.Sound(os.getcwd()+"/sound.wav")
                }

clock = pygame.time.Clock()

class Control(object):
  def __init__(self):
    self.screen = pygame.display.set_mode((500,500))
    self.screen_rect = self.screen.get_rect()
    self.clock = pygame.time.Clock()
    self.done = False
    self.fps = 60.0
    self.color = WHITE
    self.startClient = False
    message = "Start Carla Server"

    self.button = button.Button((0,0,110,25),RED, ServerController().start_server_carla,text=message, **BUTTON_STYLE)
    self.button.rect.center = (70, self.screen_rect.height - 50)

    self.button2 = button.Button((0,0,110,25),RED, self.start_joystick,text="Start Joystick", **BUTTON_STYLE)
    self.button2.rect.center = (190, self.screen_rect.height - 50)

    self.buttonStartClient = button.Button((0,0,110,25),RED, self.connect_client,text="Start Client", **BUTTON_STYLE)
    self.buttonStartClient.rect.center = (310, self.screen_rect.height - 50)

  def change_color(self):
    pass#self.color = [random.randint(0,255) for _ in range(3)]

  def connect_client(self):
    Connection.ControlClient().start()
    self.startClient = True

  def event_loop(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.done = True
      SystemController.event_buttons_pressed(event)      
      self.button.check_event(event)
      self.button2.check_event(event)
      self.buttonStartClient.check_event(event)

  def start_joystick(self):
    joystick_count = pygame.joystick.get_count()
    if joystick_count < 1:
      return 0
    if self.startClient:  
      for i in range(joystick_count):
        joystick.append(pygame.joystick.Joystick(i))
        joystick[i].init()
  
  def joystick_loop(self):
    if len(joystick) != 0:
      for x in range(len(joystick)):
        SystemController.get_axes_buttons_control(joystick[x], self.screen)
      pygame.display.flip()
    else:
      TextOutput.reset()
      TextOutput.plint(self.screen, "Joystick not found".format())

  def main_loop(self):
    while not self.done:
      self.event_loop()
      self.screen.fill(self.color)
      self.button.update(self.screen)
      self.button2.update(self.screen)
      self.buttonStartClient.update(self.screen)
      self.joystick_loop()
      pygame.display.update()
      self.clock.tick(self.fps)

class ServerController(object):
  def __init__(self):
    pass
  
  def start_server_carla(self):
    exec(open(os.getcwd()+"/modules/client/StartCarlaServer.py").read())