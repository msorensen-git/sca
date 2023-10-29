#Observer Pattern from Stack overflow

class Observer():
    _observers = []
    def __init__(self):
        self._observers.append(self)
        self._observables = {}
    def observe(self, event_name, callback):
        self._observables[event_name] = callback


class Event():
    def __init__(self, name, data, autofire = True):
        self.name = name
        self.data = data
        if autofire:
            self.fire()
    def fire(self):
        for observer in Observer._observers:
            if self.name in observer._observables:
                observer._observables[self.name](self.data)
                
""" 
Example:

#import ObserverPattern as Observer
class Room(Observer):

    def __init__(self):
        print("Room is ready.")
        Observer.__init__(self) # Observer's init needs to be called
    def someone_arrived(self, who):
        print(who + " has arrived!")

room = Room()
room.Observe('someone arrived',  room.someone_arrived)

Event('someone arrived', 'Lenard')
Output:

Room is ready.
Lenard has arrived! 
"""