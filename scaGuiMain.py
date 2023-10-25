import tkinter as tk
from tkinter import ttk
from time import strftime

import scaLed as led
import scaZone as zone


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class PageRun(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        pad = {'padx': 5, 'pady': 5}
        self.offColor = 'Gray32'
        self.nextZone = 0    # current active zone
        self.numZones = 5       # total number of zones

        self.hatLed = led.Led()

        if True:
            gridRow = 0
            self.zones = []

            self.zones.append(zone.Zone())
            localZone = self.zones[gridRow]
            localZone.frame = ttk.LabelFrame(self, text="Zone 1")
            localZone.frame.pack(side="left", fill="x", expand=True)
            # localZone.label = tk.Label(localZone.frame, text="Zone 1", padx=10)
            # localZone.label.grid(row=gridRow, column=0)
            localZone.indicator = tk.Label(localZone.frame, bg=self.offColor, width=2, height=1)
            localZone.indicator.grid(row=gridRow, column=1)
            localZone.button = tk.Button(localZone.frame, text="Z1",
                                                   command=lambda:
                                                   self.toggle_status(0))
            localZone.button.grid(row=gridRow, column=2)
            localZone.setOff()
            localZone.setTimeOn(1)

            gridRow += 1
            self.zones.append(zone.Zone())
            localZone = self.zones[gridRow]
            localZone.frame = ttk.LabelFrame(self, text="Zone 2")
            localZone.frame.pack(side="left", fill="x", expand=True)
            # localZone.label = tk.Label(localZone.frame, text="Zone 2", padx=10)
            # localZone.label.grid(row=gridRow, column=0)
            localZone.indicator = tk.Label(localZone.frame, bg=self.offColor, width=2, height=1)
            localZone.indicator.grid(row=gridRow, column=1)
            localZone.button = tk.Button(localZone.frame, text="Z2",
                                                  command=lambda:
                                                  self.toggle_status(1))
            localZone.button.grid(row=gridRow, column=2)
            localZone.setOff()
            localZone.setTimeOn(1)

            gridRow += 1
            self.zones.append(zone.Zone())
            localZone = self.zones[gridRow]
            localZone.frame = ttk.LabelFrame(self, text="Zone 3")
            localZone.frame.pack(side="left", fill="x", expand=True)
            # localZone.label = tk.Label(localZone.frame, text="Zone 2", padx=10)
            # localZone.label.grid(row=gridRow, column=0)
            localZone.indicator = tk.Label(localZone.frame, bg=self.offColor, width=2, height=1)
            localZone.indicator.grid(row=gridRow, column=1)
            localZone.button = tk.Button(localZone.frame, text="Z3",
                                                  command=lambda:
                                                  self.toggle_status(2))
            localZone.button.grid(row=gridRow, column=2)
            localZone.setOff()
            localZone.setTimeOn(1)

            gridRow += 1
            self.zones.append(zone.Zone())
            localZone = self.zones[gridRow]
            localZone.frame = ttk.LabelFrame(self, text="Zone 4")
            localZone.frame.pack(side="left", fill="x", expand=True)
            # localZone.label = tk.Label(localZone.frame, text="Zone 4", padx=10)
            # localZone.label.grid(row=gridRow, column=0)
            localZone.indicator = tk.Label(localZone.frame, bg=self.offColor, width=2, height=1)
            localZone.indicator.grid(row=gridRow, column=1)
            localZone.button = tk.Button(localZone.frame, text="Z4",
                                                  command=lambda:
                                                  self.toggle_status(3))
            localZone.button.grid(row=gridRow, column=2)
            localZone.setOff()
            localZone.setTimeOn(1)

            gridRow += 1
            self.zones.append(zone.Zone())
            localZone = self.zones[gridRow]
            localZone.frame = ttk.LabelFrame(self, text="Zone 5")
            localZone.frame.pack(side="left", fill="x", expand=True)
            # localZone.label = tk.Label(localZone.frame, text="Zone 5", padx=10)
            # localZone.label.grid(row=gridRow, column=0)
            localZone.indicator = tk.Label(localZone.frame, bg=self.offColor, width=2, height=1)
            localZone.indicator.grid(row=gridRow, column=1)
            localZone.button = tk.Button(localZone.frame, text="Z5",
                                                  command=lambda:
                                                  self.toggle_status(4))
            localZone.button.grid(row=gridRow, column=2)
            localZone.setOff()
            localZone.setTimeOn(1)

            gridRow += 1
            self.zones.append(zone.Zone())
            localZone = self.zones[gridRow]
            localZone.frame = ttk.LabelFrame(self, text="Zone 6")
            localZone.frame.pack(side="left", fill="x", expand=True)
            # localZone.label = tk.Label(localZone.frame, text="Zone 6", padx=10)
            # localZone.label.grid(row=gridRow, column=0)
            localZone.indicator = tk.Label(localZone.frame, bg=self.offColor, width=2, height=1)
            localZone.indicator.grid(row=gridRow, column=1)
            localZone.button = tk.Button(localZone.frame, text="Z6",
                                                  command=lambda:
                                                  self.toggle_status(5))
            localZone.button.grid(row=gridRow, column=2)
            localZone.setOff()
            localZone.setTimeOn(1)

        else:
            l1Frame = ttk.LabelFrame(self, text="Zone 1")
            l1Frame.pack(side="left", fill="x", expand=True)
            entry1 = tk.Entry(l1Frame, width=5)
            entry1.pack(side="top", **pad)
            button1 = tk.Button(l1Frame, text="button1")
            button1.pack(side="top", **pad)

            l2Frame = ttk.LabelFrame(self, text="Zone 2")
            l2Frame.pack(side="left", fill="x", expand=True)
            entry2 = tk.Entry(l2Frame, width=5)
            entry2.pack(side="top", **pad)
            button2 = tk.Button(l2Frame, text="button2")
            button2.pack(side="top", **pad)

            l3Frame = ttk.LabelFrame(self, text="Zone 3")
            l3Frame.pack(side="left", fill="x", expand=True)
            entry3 = tk.Entry(l3Frame, width=5)
            entry3.pack(side="top", **pad)
            button3 = tk.Button(l3Frame, text="button3")
            button3.pack(side="top", **pad)

            l4Frame = ttk.LabelFrame(self, text="Zone 4")
            l4Frame.pack(side="left", fill="x", expand=True)
            entry4 = tk.Entry(l4Frame, width=5)
            entry4.pack(side="top", **pad)
            button4 = tk.Button(l4Frame, text="button4")
            button4.pack(side="top", **pad)

            l5Frame = ttk.LabelFrame(self, text="Zone 5")
            l5Frame.pack(side="left", fill="x", expand=True)
            entry5 = tk.Entry(l5Frame, width=5)
            entry5.pack(side="top", **pad)
            button5 = tk.Button(l5Frame, text="button5")
            button5.pack(side="top", **pad)

            l6Frame = ttk.LabelFrame(self, text="Zone 6")
            l6Frame.pack(side="left", fill="x", expand=True)
            entry6 = tk.Spinbox(l6Frame, width=5)
            entry6.pack(side="top", **pad)
            button6 = tk.Button(l6Frame, text="button6")
            button6.pack(side="top", **pad)

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



class PageProgram(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        # label = tk.Label(self, text="Program Page")
        # label.pack(side="top", expand=True)

        pad = {'padx': 5, 'pady': 5}

        l1Frame = ttk.LabelFrame(self, text="Zone 1")
        # l1Frame.grid(column=0, row=0, padx=20, pady=20)
        l1Frame.pack(side="left", fill="x", expand=True)
        entry1 = tk.Spinbox(l1Frame, width=5)
        entry1.pack(side="top", **pad)
        button1 = tk.Button(l1Frame, text="button1")
        button1.pack(side="top", **pad)

        l2Frame = ttk.LabelFrame(self, text="Zone 2")
        # l2Frame.grid(column=1, row=0, padx=20, pady=20)
        l2Frame.pack(side="left", fill="x", expand=True)
        entry2 = tk.Spinbox(l2Frame, width=5)
        entry2.pack(side="top", **pad)
        button2 = tk.Button(l2Frame, text="button2")
        button2.pack(side="top", **pad)

        l3Frame = ttk.LabelFrame(self, text="Zone 3")
        l3Frame.pack(side="left", fill="x", expand=True)
        entry3 = tk.Spinbox(l3Frame, width=5)
        entry3.pack(side="top", **pad)
        button3 = tk.Button(l3Frame, text="button3")
        button3.pack(side="top", **pad)

        l4Frame = ttk.LabelFrame(self, text="Zone 4")
        l4Frame.pack(side="left", fill="x", expand=True)
        entry4 = tk.Spinbox(l4Frame, width=5)
        entry4.pack(side="top", **pad)
        button4 = tk.Button(l4Frame, text="button4")
        button4.pack(side="top", **pad)

        l5Frame = ttk.LabelFrame(self, text="Zone 5")
        l5Frame.pack(side="left", fill="x", expand=True)
        entry5 = tk.Spinbox(l5Frame, width=5)
        entry5.pack(side="top", **pad)
        button5 = tk.Button(l5Frame, text="button5")
        button5.pack(side="top", **pad)

        l6Frame = ttk.LabelFrame(self, text="Zone 6")
        l6Frame.pack(side="left", fill="x", expand=True)
        entry6 = tk.Spinbox(l6Frame, width=5)
        entry6.pack(side="top", **pad)
        button6 = tk.Button(l6Frame, text="button6")
        button6.pack(side="top", **pad)


class PageTest(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Test Page")
        label.pack(side="top", fill="both", expand=True)


class PageSettings(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Settings Page")
        label.pack(side="top", fill="both", expand=True)


# layout using grid
class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        p1 = PageRun(self)
        p2 = PageProgram(self)
        p3 = PageTest(self)
        p4 = PageSettings(self)

        tabButtonframe = tk.Frame(self)
        container = tk.Frame(self)
        controlButtonframe = tk.Frame(self)
        tabButtonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)
        controlButtonframe.pack(side="top", fill="both", expand=False)

        # pages in place
        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        # tab buttons in place
        b1 = tk.Button(tabButtonframe, text="Run", command=p1.show).pack(side ="left")
        b2 = tk.Button(tabButtonframe, text="Program", command=p2.show).pack(side ="left")
        b3 = tk.Button(tabButtonframe, text="Test", command=p3.show).pack(side ="left")
        b4 = tk.Button(tabButtonframe, text="Settings", command=p4.show).pack(side ="left")

        # control buttons in place
        tk.Button(controlButtonframe, text="Exit", command=self.quit).pack(side="right")
        tk.Button(controlButtonframe, text="All Off", command=self.allOff).pack(side="right")
        self.time_label = tk.Label(controlButtonframe, font=('helvetica', 12), background='gray', foreground='white')
        self.time_label.pack(side="right")

        # Cycle button
        self.cycleButton = tk.Button(controlButtonframe, text="Cycle", command=self.startCycle)
        self.cycleButton.pack(side="right")

        p1.show()
        # p3.show()

    def allOff(self):
        return
    
    # Start a cycle of the zones
    def startCycle(self):
        self.nextZone = 0
        self.update_time()

    ### Problem: this method can't find time_label
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
        for i in range( self.p1.numZones):
            self.set_status(i, False)

