__author__ = "Your name"
__email__ = "Your email"
__version__ = "0.1"


from seads_appliance import SeadsAppliance


class SeadsCore(object):
    """
    Docstring here
    """

    def __init__(self, appliance_names):
        """

        :param self:
        """
        self.appliances = [SeadsAppliance(appliance_names[i]) for i in range(4)]
        pass

    def get_appliances(self):
        """

        :return:
        """
        return self.appliances

    def get_power(self):
        return self.appliances[0].get_data()
        pass
