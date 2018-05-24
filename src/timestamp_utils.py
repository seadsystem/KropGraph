__author__ = "Your name"
__email__ = "Your email"

from datetime import datetime
from time import strftime, mktime


class TimestampUtils(object):

    @staticmethod
    def convert_to_readable(timestamp):
        return strftime('%Y-%m-%d %H:%M:%S', timestamp)

    @staticmethod
    def convert_to_timestamp(str_datetime):
        return mktime(datetime.strptime(str_datetime, "%Y-%m-%d %H:%M:%S"))


    @staticmethod
    def insert_your_function():
        pass
