__author__ = "Your name"
__email__ = "Your email"
__version__ = "0.1"

from collections import deque
from queue import Queue

from data_streamer import DataStreamer


class SeadsAppliance(object):
    """
    Docstring here
    """

    current_data = deque([])

    def __init__(self, label=""):
        """

        :param self:
        """
        self.label = label
        self.recv_msg_queue = Queue()
        if label == "master":
            self.power_data = DataStreamer(self.recv_msg_queue)
        pass

    def _parse_data(self):
        """

        :return:
        """
        while not self.recv_msg_queue.empty():
            self.current_data.appendleft(self.recv_msg_queue.get())

    def get_data(self):
        """

        :return:
        """
        self._parse_data()
        if (len(self.current_data) != 0):
            data = self.current_data.popleft()
            return data
        else:
            return -1

    def set_label(self, label):
        """

        :param label:
        :return:
        """
        self.label = label

    def get_label(self):
        """

        :return:
        """
        return self.label

    def __repr__(self):
        return "{}={}".format(self.get_label(), self.get_data())
