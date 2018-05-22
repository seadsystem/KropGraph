__author__ = "Your name"
__email__ = "Your email"

from time import strftime


class TimestampUtils(object):

    @staticmethod
    def convert_to_readable(timestamp):
        return strftime('%Y-%m-%d %H:%M:%S', timestamp)


    @staticmethod
    def insert_your_function():
        pass
