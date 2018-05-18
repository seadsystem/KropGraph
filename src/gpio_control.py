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
        """

        """
        GPIO.setmode(GPIO.BOARD)
        for key, value in d.items():
             GPIO.setup(value, GPIO.OUT)


    def pin_on(self, switch):
        """

        :param pin:
        :return:
        """
        print('Turning pin %d on' % GpioControl.switches[switch])
        GPIO.output(GPIO.switches[switch], 1)

    def pin_off(self, switch):
        """

        :param pin:
        :return:
        """
        print('Turning pin %d off' % GpioControl.switches[switch])
        GPIO.output(GPIO.switches[switch], 0)
