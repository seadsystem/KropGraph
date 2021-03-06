__author__ = "Your name"
__email__ = "Your email"
__version__ = "0.1"

import json
from datetime import datetime
from threading import Thread
import time
import subprocess

import requests


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
        url = "http://db.sead.systems:8080/466419818?limit=61&device=Panel3&type=P"
        prev_time = int(time.time())
        while True:
            """
            response = requests.get(url)
            json_data = json.loads(response.text)
            for i in range(2,61):
                previous_data_point = json_data[i-1]
                current_data_point = json_data[i]
                delta = (float(current_data_point[1]) - float(previous_data_point[1])) / (3600.0 * 1.0);
                datetime_object = datetime.strptime(current_data_point[0], '%Y-%m-%d %H:%M:%S')
                self.message_queue.put((delta, datetime_object))
            sleep(60)
        # for i in range(5):
            # self.message_queue.put((time(), "{}kWh".format(randint(0, 5000)/1000.0)))
"""         
            cur_time = int(time.time())
            if cur_time == prev_time:
                continue
            prev_time = cur_time
            cur_time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(cur_time))
            datetime_object = datetime.strptime(cur_time_str, '%Y-%m-%d %H:%M:%S')
            delta = 510.0*0.01*float(subprocess.check_output(["apcaccess"]).decode().split("\n")[12].split(":")[1].strip().split(" ")[0])
            self.message_queue.put((delta, datetime_object))
            time.sleep(1)

    def finish(self):
        print("Done")
        self.running = False
        self.thread.join()
