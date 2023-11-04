from gpiozero import LED
# from time import sleep


class Led():
    def __init__(self):
        self.indicator = []

        self.indicator.append(LED(7))
        self.indicator.append(LED(8))
        self.indicator.append(LED(11))
        self.indicator.append(LED(9))
        self.indicator.append(LED(10))
        self.indicator.append(LED(18))
        self.indicator.append(LED(17))
        self.indicator.append(LED(16))
        self.indicator.append(LED(6))
        self.indicator.append(LED(5))
        self.indicator.append(LED(25))
        self.indicator.append(LED(24))
        self.indicator.append(LED(15))
        self.indicator.append(LED(14))
        self.indicator.append(LED(19))
        self.indicator.append(LED(20))
        self.indicator.append(LED(12))
        self.indicator.append(LED(1))
        self.indicator.append(LED(22))
        self.indicator.append(LED(23))
        self.indicator.append(LED(26))
        self.indicator.append(LED(13))
        self.indicator.append(LED(21))
        self.indicator.append(LED(27))
        self.indicator.append(LED(4))
        self.indicator.append(LED(3))
        self.indicator.append(LED(2))

    def toggle(self, index):
        self.indicator[index].toggle()

    def on(self, index):
        self.indicator[index].on()

    def off(self, index):
        self.indicator[index].off()
