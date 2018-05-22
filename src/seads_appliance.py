__author__ = "Your name"
__email__ = "Your email"
__version__ = "0.1"

from data_streamer import DataStreamer
from queue import Queue
from timestamp_utils import TimestampUtils


class SeadsAppliance(object):
    """
    Docstring here
    """

    def __init__(self, label=""):
        """

        :param self:
        """
        self.label = label
        self.recv_msg_queue = Queue()
        self.power_data = DataStreamer(self.recv_msg_queue)
        pass

    def _parse_data(self):
        """

        :return:
        """
        data = []
        while not self.recv_msg_queue.empty():
            data.append(self.recv_msg_queue.get())
        return data

    def get_data(self):
        """

        :return:
        """
        return self._parse_data()

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
