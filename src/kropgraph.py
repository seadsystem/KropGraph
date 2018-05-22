#!/usr/bin/python3

__author__ = "Kevin Jung, Ray Burgess, Olexiy"
__email__ = "Your email"

from kivy.app import App
from seads_core import SeadsCore
from time import sleep
from random import randint
from timestamp_utils import TimestampUtils
from queue import Queue


queue_seads_data = Queue()
queue_ups_data = Queue()

# Labels for the Pins in order
pin_labels = ["Light Bulb", "Huge Bulb", "Lamp", "Fridge"]


def main():

    core = SeadsCore(pin_labels)
    sleep(1)
    for appliance in core.get_appliances():
        print(appliance)


if __name__ == "__main__":
    main()
