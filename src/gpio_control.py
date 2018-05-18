__author__ = "Grant Lin"
__email__ = "grant523@gmail.com"

import RPi.GPIO as GPIO


class GpioControl(object):
    """
    Docstring here
    """

    switches = {
        'Switch 1': 3,
        'Switch 2': 5,
        'Switch 3': 7,
        'Switch 4': 29
    }

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        for key, value in GpioControl.switches.items():
            GPIO.setup(value, GPIO.OUT)
            GPIO.output(value, 0)

    def pin_on(self, switch):
        """
        Turns on the pin corresponding to switch
        :param switch: Switch that was toggled to down
        """
        print('Turning pin %d on' % GpioControl.switches[switch])
        GPIO.output(GpioControl.switches[switch], 1)

    def pin_off(self, switch):
        """
        Turns off the pin corresponding to switch
        :param switch: Switch that was toggled to normal
        """
        print('Turning pin %d off' % GpioControl.switches[switch])
        GPIO.output(GpioControl.switches[switch], 0)
