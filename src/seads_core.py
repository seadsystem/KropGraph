__author__ = "Your name"
__email__ = "Your email"
__version__ = "0.1"


from seads_appliance import SeadsAppliance


class SeadsCore(object):
    """
    Docstring here
    """

    def __init__(self):
        """

        :param self:
        """
        self.appliances = [SeadsAppliance()]
        pass

    def get_appliances(self):
        """

        :return:
        """
        return self.appliances
