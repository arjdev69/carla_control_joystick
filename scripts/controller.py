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


class Control(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((500,500))
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.done = False
        self.fps = 60.0
        self.color = WHITE
        message = "Change the screen color."

        self.button = button.Button((0,0,200,50),RED, self.change_color,text=message, **BUTTON_STYLE)
        self.button.rect.center = (self.screen_rect.centerx,25)
        self.button2 = button.Button((0,0,200,50),RED, self.change_color,text="ola", **BUTTON_STYLE)
        self.button2.rect.center = (self.screen_rect.centerx,110)

    def change_color(self):
        self.color = [random.randint(0,255) for _ in range(3)]

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            self.button.check_event(event)
            self.button2.check_event(event)

    def main_loop(self):
        while not self.done:
            self.event_loop()
            self.screen.fill(self.color)
            self.button.update(self.screen)
            self.button2.update(self.screen)
            pygame.display.update()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    run_it = Control()
    run_it.main_loop()
    pygame.quit()
    sys.exit()