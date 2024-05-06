
class Zone:
    """ One watering zone """
    def __init__(self):
        self.status = False
        self._time_on = 0

    def set_on(self):
        """ set this zone on """
        self.status = True

    def set_off(self):
        """ set this zone off """
        self.status = False

    def is_on(self):
        """ is this zone on? """
        return self.status

    def time_on(self):
        """ how long will this zone be on? """
        return self._time_on     # seconds on for zone

    def set_time_on(self, value):
        """ set how long this zone should be on """
        self._time_on = value
