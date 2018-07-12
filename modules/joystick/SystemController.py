from modules.joystick import PrintText as outputText
from modules.client import Connection
from modules.client.carla.client import VehicleControl
import pygame

textPrint = outputText.TextPrint()
control_car = Connection.ControlClient
alert = "I am sorry baby, not found joystick"
wheel = velocity = 0
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
  global velocity; global wheel
  #velocity = wheel = 0
  control = VehicleControl()
  if joystick.get_axis(axis):
    axisValue = joystick.get_axis(axis)

    if axis == 0:
      if axisValue > 0.0:
        text_axis(axisValue,text[0],screen)
        control.steer = axisValue
        print("Steer +")
      else:
        text_axis(axisValue,text[1],screen)
        control.steer = axisValue
        print("Steer -")
    
    if axis == 4:
      if axisValue > 0.0:
        text_axis(axisValue,text[0],screen)
        control.throttle = axisValue
        print("throttle +")
      else:
        text_axis(axisValue,text[1],screen)
        control.throttle = axisValue
        print("throttle -")
    car_control(control)

      

def car_control(control):
    control_car.pilots_control(control)