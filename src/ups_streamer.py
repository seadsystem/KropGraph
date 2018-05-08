__author__ = "Your name"
__email__ = "Your email"
__version__ = "0.1"

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

    def finish(self):
        self.running = False
        self.thread.join()
