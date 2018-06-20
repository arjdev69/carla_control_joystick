from modules import printText as outputText
import pygame

textPrint = outputText.TextPrint()

#FUNCTIONS
def event_buttons(event):
  # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
  if event.type == pygame.JOYBUTTONDOWN:
    print("Joystick button pressed.")
  if event.type == pygame.JOYBUTTONUP:
    print("Joystick button released.")

def init_joystick(screen, color):
  # DRAWING STEP
  # First, clear the screen to white. Don't put other drawing commands
  # above this, or they will be erased with this command.
  screen.fill(color)
  textPrint.reset()

  # Get count of joysticks
  joystick_count = pygame.joystick.get_count()
  if joystick_count < 1:
    textPrint.plint(screen, "I am sorry baby, not found joystick {}".format(joystick_count))
    print("I am sorry baby, not found joystick {}")
    textPrint.indent()
    return 0
  else:
    textPrint.plint(screen, "Number of joysticks: {}".format(joystick_count) )
    textPrint.indent()
    joystick = pygame.joystick.Joystick(0)
    #print(joystick_count)
    joystick.init()
    return joystick

def get_axes_buttons_control(joystick):
  axes = joystick.get_numaxes()
  if joystick.get_axis(3):
    axis = joystick.get_axis(3)
    if axis > 0.0:
      textPrint.plint(screen, "Right  - Axis {} value: {:>6.3f}".format(0, axis))
    else:
      textPrint.plint(screen, "Left - Axis {} value: {:>6.3f}".format(0, axis))
    textPrint.unindent()
