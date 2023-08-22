import tkinter as tk


class Zone:
    def __init__(self):
        self.status = False
        self._timeOn = 0
        self.label = None
        self.indicator = None
        self.button = None

    def label(self):
        return self.label

    def indicator(self):
        return self.indicator

    def button(self):
        return self.button

    def setOn(self):
        self.status = True
        self.indicator.configure(bg="red")

    def setOff(self):
        self.status = False
        self.indicator.configure(bg='Gray32')

    def toggle(self):
        # self.status = not self.status
        if self.status:
            self.setOff()
        else:
            self.setOn()

    def isOn(self):
        return self.status

    def timeOn(self):
        return self._timeOn     # seconds on for zone

    def setTimeOn(self, value):
        self._timeOn = value
