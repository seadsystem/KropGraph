__author__ = "Grant Lin"
__email__ = "grant523@gmail.com"

import RPi.GPIO as GPIO


class GpioControl(object):
    """
    Docstring here
    """

    switches = {
        'Switch 1': 31,
        'Switch 2': 33,
        'Switch 3': 35,
        'Switch 4': 37
    }

    def __init__(self):
        try:
            import RPi.GPIO as GPIO
            self.simulate = False
        except ModuleNotFoundError:
            self.simulate = True
            return

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
        if self.simulate:
            return
        GPIO.output(GpioControl.switches[switch], 1)

    def pin_off(self, switch):
        """
        Turns off the pin corresponding to switch
        :param switch: Switch that was toggled to normal
        """
        print('Turning pin %d off' % GpioControl.switches[switch])
        if self.simulate:
            return
        GPIO.output(GpioControl.switches[switch], 0)
