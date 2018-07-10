from modules.joystick import PrintText as outputText
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

def get_axes_buttons_control(joystick, screen):
  direction_axis(joystick, 0, ["Right","Left"],screen)

  direction_axis(joystick, 4, ["Back","Front"],screen)

def text_axis(axis, direction, screen):
  textPrint.indent();textPrint.reset()
  textPrint.plint(screen, direction + " - Axis {} value: {:>6.3f}".format(0, axis))

def direction_axis(joystick, axis, text, screen):
  if joystick.get_axis(axis):
    axis = joystick.get_axis(axis)
    if axis > 0.0:
      text_axis(axis,text[0],screen)
    else:
      text_axis(axis,text[1],screen)