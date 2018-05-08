#!/usr/bin/python3

__author__ = "Kevin Jung, Ray Burgess, Olexiy"
__email__ = "Your email"

from kivy.app import App
from seads_core import SeadsCore
from time import sleep
from random import randint
from timestamp_utils import TimestampUtils


def main():

    core = SeadsCore()
    for appliance in core.get_appliances():
        appliance.set_label("Panel {}".format(randint(0, 10)))
    sleep(1)
    for appliance in core.get_appliances():
        print("{}={}".format(appliance.get_label(), appliance.get_data()))

    TimestampUtils.convert_to_readable("test")


if __name__ == "__main__":
    main()
