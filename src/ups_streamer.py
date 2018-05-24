__author__ = "Your name"
__email__ = "Your email"
__version__ = "0.1"

from random import randint
from threading import Thread


class UpsStreamer(object):
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
        # TODO: inject apcupsd syscall
        while True:
            self.message_queue.put(randint(0, 100))

    def finish(self):
        self.running = False
        self.thread.join()
