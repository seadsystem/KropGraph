#!/usr/bin/python3

__author__ = "Kevin Jung, Ray Burgess, Olexiy"
__email__ = "Your email"

from queue import Queue

from graphics import Graphics

queue_seads_data = Queue()
queue_ups_data = Queue()

# Labels for the Pins in order
pin_labels = ["Light Bulb", "Huge Bulb", "Lamp", "Fridge"]


def main():
    graphics = Graphics()
    graphics.run()



if __name__ == "__main__":
    main()
