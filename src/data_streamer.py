__author__ = "Your name"
__email__ = "Your email"
__version__ = "0.1"

from threading import Thread
from random import randint
from time import time, sleep
from datetime import datetime
import requests
import json


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
        url = "http://db.sead.systems:8080/466419818?limit=601&device=Panel3&type=P"
        while True:
            print("Polling!")
            response = requests.get(url)
            json_data = json.loads(response.text)
            # json_data = list(reversed(json_data))

            values = []
            dates = []
            for i in range(2,601):
                previous_data_point = json_data[i-1]
                current_data_point = json_data[i]
                delta = (float(current_data_point[1]) - float(previous_data_point[1])) / (3600.0*1000.0);
                datetime_object = datetime.strptime(current_data_point[0], '%Y-%m-%d %H:%M:%S')
                values.append(delta)
                dates.append(datetime_object)
            self.message_queue.put((values, dates))
            sleep(60)
        # for i in range(5):
            # self.message_queue.put((time(), "{}kWh".format(randint(0, 5000)/1000.0)))

    def finish(self):
        print("Done")
        self.running = False
        self.thread.join()
