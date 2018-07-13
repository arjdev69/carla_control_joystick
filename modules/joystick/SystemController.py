from modules.joystick import PrintText as outputText
from modules.client import Connection
from modules.client.carla.client import VehicleControl
import pygame

textPrint = outputText.TextPrint()
control_car = Connection.ControlClient
pressed = reverse = False
joystick_event = ""

#FUNCTIONS
def event_buttons_pressed(event):
  global pressed
  # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
  if event.type == pygame.JOYBUTTONDOWN:
    pressed = not pressed
    set_reverse()
  return pressed

def get_axes_buttons_control(joystick, screen):         #RENAME FUNCTIONS
  global joystick_event
  direction_axis(joystick, [0,4,3], ["Steer","Throttle"],screen)
  joystick_event = joystick

def text_axis(axis, direction, screen):
  textPrint.indent();textPrint.reset()
  textPrint.plint(screen, direction + " - Axis {:>6.3f} value: {}".format(0, axis))

def direction_axis(joystick, axis, text, screen):
  set_direction_control(joystick, axis,screen)

def set_direction_control(joystick, axis,screen):
  global reverse; global pressed
  control = VehicleControl()

  if axis[0] == 0:
    control.steer = set_axis_control_car(joystick,axis[0])

  if axis[1] == 4:
    control.throttle = set_axis_control_car(joystick,axis[1])

  control.brake = set_brake(joystick)


  control.reverse = reverse
  send_commands(control)

def set_axis_control_car(joystick,axis):
  axisValue = joystick.get_axis(axis)
  return axisValue

def set_reverse():
  global reverse;global joystick_event

  if get_button_state(joystick_event,3)==1:
    reverse = not reverse

def set_brake(joystick):
  if get_button_state(joystick,5)==1:
    return True
  else:
    return False


def get_button_state(joystick, id):
  value = joystick.get_button(id)
  return value

def send_commands(control):
  control_car.pilots_control(control)
