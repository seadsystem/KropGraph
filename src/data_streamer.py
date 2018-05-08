__author__ = "Your name"
__email__ = "Your email"
__version__ = "0.1"

from threading import Thread
from random import randint
from time import time


class DataStreamer(object):
    """
    Docstring here
    """

    def __init__(self, message_queue):
        """

        :param self:
        """
        self.message_queue = message_queue
        self.running = True
        self.thread = Thread(target=self._start_data_poll).start()
        pass

    def _start_data_poll(self):
        """

        :return:
        """
        for i in range(5):
            self.message_queue.put((time(), "{}kWh".format(randint(0, 5000)/1000.0)))

    def finish(self):
        self.running = False
        self.thread.join()
