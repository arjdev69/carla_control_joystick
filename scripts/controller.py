#!python
from modules import printText
import pygame

#FUNCTIONS
def event_buttons(event):
  # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
  if event.type == pygame.JOYBUTTONDOWN:
    print("Joystick button pressed.")
  if event.type == pygame.JOYBUTTONUP:
    print("Joystick button released.")

def init_joystick():
  # DRAWING STEP
  # First, clear the screen to white. Don't put other drawing commands
  # above this, or they will be erased with this command.
  screen.fill(WHITE)
  textPrint.reset()

  # Get count of joysticks
  joystick_count = pygame.joystick.get_count()

  textPrint.plint(screen, "Number of joysticks: {}".format(joystick_count) )
  textPrint.indent()
  joystick = pygame.joystick.Joystick(0)
  joystick.init()
  return joystick

def get_axes_buttons_control():
  axes = joystick.get_numaxes()
  if joystick.get_axis(0):
    axis = joystick.get_axis(0)
    if axis > 0.0:
      textPrint.plint(screen, "Right  - Axis {} value: {:>6.3f}".format(0, axis))
    else:
      textPrint.plint(screen, "Left - Axis {} value: {:>6.3f}".format(0, axis))
  
  textPrint.unindent()

WHITE    = ( 255, 255, 255)

textPrint = printText.TextPrint2();

pygame.init()
 
# Set the width and height of the screen [width,height]
size = [500, 700]
screen = pygame.display.set_mode(size)

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
      event_buttons(event)

    joystick = init_joystick()

    name = joystick.get_name()
    textPrint.plint(screen, "Joystick name: {}".format(name) )

    get_axes_buttons_control()

    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # Limit to 20 frames per second
    clock.tick(20)
   
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit ()