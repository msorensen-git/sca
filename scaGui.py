import tkinter as tk
from time import strftime

import scaLed as led
import scaZone as zone


class SprinklerControlPanelApp:
    # setup the controls in the window
    def __init__(self, root):
        self.offColor = 'Gray32'
        self.root = root
        self.root.title("Sprinkler Control Panel")
        self.nextZone = 0    # current active zone
        self.numZones = 5       # total number of zones

        self.hatLed = led.Led()

        gridRow = 0
        self.zones = []

        self.zones.append(zone.Zone())
        self.zones[gridRow].label = tk.Label(root, text="Zone 1", padx=10)
        self.zones[gridRow].label.grid(row=gridRow, column=0)
        self.zones[gridRow].indicator = tk.Label(root, width=2, height=1)
        self.zones[gridRow].indicator.grid(row=gridRow, column=1)
        self.zones[gridRow].button = tk.Button(root, text="Toggle Z1",
                                               command=lambda:
                                               self.toggle_status(0))
        self.zones[gridRow].button.grid(row=gridRow, column=2)
        self.zones[gridRow].setOff()
        self.zones[gridRow].setTimeOn(1)

        gridRow += 1
        self.zones.append(zone.Zone())
        self.zones[gridRow].label = tk.Label(root, text="Zone 2", padx=10)
        self.zones[gridRow].label.grid(row=gridRow, column=0)
        self.zones[gridRow].indicator = tk.Label(root,
                                                 bg=self.offColor,
                                                 width=2, height=1)
        self.zones[gridRow].indicator.grid(row=gridRow, column=1)
        self.zones[gridRow].button = tk.Button(root, text="Toggle Z2",
                                               command=lambda:
                                               self.toggle_status(1))
        self.zones[gridRow].button.grid(row=gridRow, column=2)
        self.zones[gridRow].setOff()
        self.zones[gridRow].setTimeOn(1)

        gridRow += 1
        self.zones.append(zone.Zone())
        self.zones[gridRow].label = tk.Label(root, text="Zone 3", padx=10)
        self.zones[gridRow].label.grid(row=gridRow, column=0)
        self.zones[gridRow].indicator = tk.Label(root, bg=self.offColor,
                                                 width=2, height=1)
        self.zones[gridRow].indicator.grid(row=gridRow, column=1)
        self.zones[gridRow].button = tk.Button(root, text="Toggle Z3",
                                               command=lambda:
                                               self.toggle_status(2))
        self.zones[gridRow].button.grid(row=gridRow, column=2)
        self.zones[gridRow].setOff()
        self.zones[gridRow].setTimeOn(1)

        gridRow += 1
        self.zones.append(zone.Zone())
        self.zones[gridRow].label = tk.Label(root, text="Zone 4", padx=10)
        self.zones[gridRow].label.grid(row=gridRow, column=0)
        self.zones[gridRow].indicator = tk.Label(root,
                                                 bg=self.offColor,
                                                 width=2, height=1)
        self.zones[gridRow].indicator.grid(row=gridRow, column=1)
        self.zones[gridRow].button = tk.Button(root, text="Toggle Z4",
                                               command=lambda:
                                               self.toggle_status(3))
        self.zones[gridRow].button.grid(row=gridRow, column=2)
        self.zones[gridRow].setOff()
        self.zones[gridRow].setTimeOn(1)

        gridRow += 1
        self.zones.append(zone.Zone())
        self.zones[gridRow].label = tk.Label(root, text="Zone 5", padx=10)
        self.zones[gridRow].label.grid(row=gridRow, column=0)
        self.zones[gridRow].indicator = tk.Label(root, bg=self.offColor,
                                                 width=2, height=1)
        self.zones[gridRow].indicator.grid(row=gridRow, column=1)
        self.zones[gridRow].button = tk.Button(root, text="Toggle Z5",
                                               command=lambda:
                                               self.toggle_status(4))
        self.zones[gridRow].button.grid(row=gridRow, column=2)
        self.zones[gridRow].setOff()
        self.zones[gridRow].setTimeOn(1)

        # Sliders
        gridRow += 1
        self.temp_slider = tk.Scale(root,
                                    from_=0, to=100,
                                    orient="horizontal",
                                    command=self.temp_slider_changed)
        self.temp_slider.grid(row=gridRow, column=2)

        self.temp_slider_value_label = tk.Label(root, text="Temp z F")
        self.temp_slider_value_label.grid(row=gridRow, column=3)
        self.temp_slider.set(1)     # start at value 1

        # Create a label to display the time
        gridRow += 1
        self.time_label = tk.Label(root, font=('helvetica', 12),
                                   background='gray', foreground='white')
        self.time_label.grid(row=gridRow, column=8)

        # Cycle button
        cycleButton = tk.Button(root, text="Cycle", command=self.startCycle)
        cycleButton.grid(row=gridRow, column=1)

        # elapsed time for controlling the zone on/off times in a cycle
        # self.elapsedTime = 0

    # Start a cycle of the zones
    def startCycle(self):
        self.nextZone = 0
        self.update_time()

    # update the clock every second
    def update_clock(self):
        # print("tick")
        current_time = strftime('%H:%M:%S %p')
        self.time_label.config(text=current_time)
        self.time_label.after(1000, self.update_clock)  # Update every second

    # progress through each of the zones
    def update_time(self):
        # print("examine timers")
        self.allZonesOff()

        if self.nextZone >= 0 and self.nextZone < self.numZones:
            sleepTime = self.zones[self.nextZone].timeOn()
            print(f"Start Zone {self.nextZone} for {sleepTime} x 10")
            # self.zones[self.nextZone].setOn()
            self.set_status(self.nextZone, True)
            self.nextZone += 1

            # Sleep for length of this zone
            self.time_label.after(10 * sleepTime, self.update_time)

    # turn off all zones
    def allZonesOff(self):
        for i in range(self.numZones):
            self.set_status(i, False)

    # handle slider update
    def temp_slider_changed(self, value):
        self.temp_slider_value_label.config(text=f"Temp: {value} F")
        v = int(value)

        # update all zones
        for i in range(self.numZones):
            self.zones[i].setTimeOn(v)
        # self.zones[2].setTimeOn(v+100)

    # set one zone on or off
    def set_status(self, zone, status):
        if status:
            self.zones[zone].setOn()
            self.hatLed.on(zone+1)
        else:
            self.zones[zone].setOff()
            self.hatLed.off(zone+1)

    # toggle status of one zone
    def toggle_status(self, zone):
        self.set_status(zone, not self.zones[zone].isOn())
