#!python
from modules import import_modules
import pygame

SystemController = import_modules.SystemController

pygame.init()


# Set the width and height of the screen [width,height]
size = [500, 700]
screen = pygame.display.set_mode(size)
WHITE = ( 255, 255, 255)
pygame.display.set_caption("My Game")

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()
   
# Get ready to print textPrint = TextPrint()
screen.fill(WHITE)

# -------- Main Program Loop -----------
while done==False:
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
      if event.type == pygame.QUIT: # If user clicked close
        done=True # Flag that we are done so we exit this loop
      SystemController.event_buttons(event)

    joystick = SystemController.init_joystick(screen, WHITE)

    if joystick != 0:
      SystemController.get_axes_buttons_control(joystick)
      pygame.display.flip()
      # Limit to 20 frames per second
      clock.tick(20)

pygame.quit ()