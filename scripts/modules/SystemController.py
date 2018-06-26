from modules import printText as outputText
import pygame

textPrint = outputText.TextPrint()
alert = "I am sorry baby, not found joystick"
#FUNCTIONS
def event_buttons(event):
  # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
  if event.type == pygame.JOYBUTTONDOWN:
    print("Joystick button pressed.")
  if event.type == pygame.JOYBUTTONUP:
    print("Joystick button released.")

def init_joystick(screen, color):
  global alert
  # DRAWING STEP
  # First, clear the screen to white. Don't put other drawing commands
  # above this, or they will be erased with this command.
  screen.fill(color)
  textPrint.reset()

  # Get count of joysticks
  joystick_count = pygame.joystick.get_count()
  if joystick_count < 1:
    textPrint.plint(screen, alert.format(joystick_count))
    if alert != "":
      print(alert)
      alert = ""
      textPrint.indent()
    return 0
  else:
    textPrint.plint(screen, "Number of joysticks: {}".format(joystick_count) )
    textPrint.indent()
    joystick = pygame.joystick.Joystick(0)
    #print(joystick_count)
    joystick.init()
    return joystick

def get_axes_buttons_control(joystick, screen):
  direction_axis(joystick, 0, ["Right","Left"],screen)

  direction_axis(joystick, 4, ["Back","Front"],screen)

def text_axis(axis, direction, screen):
  textPrint.plint(screen, direction + " - Axis {} value: {:>6.3f}".format(0, axis))

def direction_axis(joystick,axis, text, screen):
  if joystick.get_axis(axis):
    axis = joystick.get_axis(axis)
    if axis > 0.0:
      text_axis(axis,text[0],screen)
    else:
      text_axis(axis,text[1],screen)