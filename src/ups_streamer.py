__author__ = "Your name"
__email__ = "Your email"
__version__ = "0.1"

from threading import Thread
import subprocess
from time import sleep


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
            pct_full = float(subprocess.check_output(["apcaccess"]).decode().split("\n")[13].split(":")[1].strip().split(" ")[0])
            #pct_full = 0
            frac = (100 - pct_full) / 4.0
            frac_1 = pct_full + frac * 1
            frac_2 = pct_full + frac * 2
            frac_3 = pct_full + frac * 3
            frac_4 = pct_full + frac * 4

            self.message_queue.put(pct_full)
            self.message_queue.put(frac_1)
            self.message_queue.put(frac_2)
            self.message_queue.put(frac_3)
            self.message_queue.put(frac_4)

    def finish(self):
        self.running = False
        self.thread.join()
