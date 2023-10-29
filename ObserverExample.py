from ObserverPattern import *

class Room(Observer):

    def __init__(self):
        print("Room is ready.")
        Observer.__init__(self) # Observer's init needs to be called
    def someone_arrived(self, who):
        print(who + " has arrived in Room!")

class Boat(Observer):

    def __init__(self):
        print("Boat is ready.")
        Observer.__init__(self) # Observer's init needs to be called
    def someone_arrived(self, who):
        print(who + " has arrived on Boat!")

room = Room()
room.observe('someone arrived',  room.someone_arrived)

Event('someone arrived', 'Lenard')

boat = Boat()
boat.observe('someone arrived', boat.someone_arrived)

Event('someone arrived', 'Charles')