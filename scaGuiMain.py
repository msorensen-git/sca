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
        gridRow = 0

        MainView.zones.append(zone.Zone())
        localZone = MainView.zones[gridRow]
        localZone.frame = ttk.LabelFrame(self, text="Zone 1")
        localZone.frame.pack(side="left", fill="x", expand=True)
        # localZone.label = tk.Label(localZone.frame, text="Zone 1", padx=10)
        # localZone.label.grid(row=gridRow, column=0)
        localZone.indicator = tk.Label(localZone.frame, bg=self.offColor, width=2, height=1)
        localZone.indicator.grid(row=gridRow, column=1)
        localZone.button = tk.Button(localZone.frame, text="Z1",
                                               command= MainView.toggle_status0)
        localZone.button.grid(row=gridRow, column=2)
        localZone.setOff()
        localZone.setTimeOn(1)

        gridRow += 1
        MainView.zones.append(zone.Zone())
        localZone = MainView.zones[gridRow]
        localZone.frame = ttk.LabelFrame(self, text="Zone 2")
        localZone.frame.pack(side="left", fill="x", expand=True)
        # localZone.label = tk.Label(localZone.frame, text="Zone 2", padx=10)
        # localZone.label.grid(row=gridRow, column=0)
        localZone.indicator = tk.Label(localZone.frame, bg=self.offColor, width=2, height=1)
        localZone.indicator.grid(row=gridRow, column=1)
        localZone.button = tk.Button(localZone.frame, text="Z2",
                                              command= MainView.toggle_status1)
        localZone.button.grid(row=gridRow, column=2)
        localZone.setOff()
        localZone.setTimeOn(1)

        gridRow += 1
        MainView.zones.append(zone.Zone())
        localZone = MainView.zones[gridRow]
        localZone.frame = ttk.LabelFrame(self, text="Zone 3")
        localZone.frame.pack(side="left", fill="x", expand=True)
        # localZone.label = tk.Label(localZone.frame, text="Zone 2", padx=10)
        # localZone.label.grid(row=gridRow, column=0)
        localZone.indicator = tk.Label(localZone.frame, bg=self.offColor, width=2, height=1)
        localZone.indicator.grid(row=gridRow, column=1)
        localZone.button = tk.Button(localZone.frame, text="Z3",
                                              command= MainView.toggle_status2)
        localZone.button.grid(row=gridRow, column=2)
        localZone.setOff()
        localZone.setTimeOn(1)

        gridRow += 1
        MainView.zones.append(zone.Zone())
        localZone = MainView.zones[gridRow]
        localZone.frame = ttk.LabelFrame(self, text="Zone 4")
        localZone.frame.pack(side="left", fill="x", expand=True)
        # localZone.label = tk.Label(localZone.frame, text="Zone 4", padx=10)
        # localZone.label.grid(row=gridRow, column=0)
        localZone.indicator = tk.Label(localZone.frame, bg=self.offColor, width=2, height=1)
        localZone.indicator.grid(row=gridRow, column=1)
        localZone.button = tk.Button(localZone.frame, text="Z4",
                                              command= MainView.toggle_status3)
        localZone.button.grid(row=gridRow, column=2)
        localZone.setOff()
        localZone.setTimeOn(1)

        gridRow += 1
        MainView.zones.append(zone.Zone())
        localZone = MainView.zones[gridRow]
        localZone.frame = ttk.LabelFrame(self, text="Zone 5")
        localZone.frame.pack(side="left", fill="x", expand=True)
        # localZone.label = tk.Label(localZone.frame, text="Zone 5", padx=10)
        # localZone.label.grid(row=gridRow, column=0)
        localZone.indicator = tk.Label(localZone.frame, bg=self.offColor, width=2, height=1)
        localZone.indicator.grid(row=gridRow, column=1)
        localZone.button = tk.Button(localZone.frame, text="Z5",
                                              command= MainView.toggle_status4)
        localZone.button.grid(row=gridRow, column=2)
        localZone.setOff()
        localZone.setTimeOn(1)

        gridRow += 1
        MainView.zones.append(zone.Zone())
        localZone = MainView.zones[gridRow]
        localZone.frame = ttk.LabelFrame(self, text="Zone 6")
        localZone.frame.pack(side="left", fill="x", expand=True)
        # localZone.label = tk.Label(localZone.frame, text="Zone 6", padx=10)
        # localZone.label.grid(row=gridRow, column=0)
        localZone.indicator = tk.Label(localZone.frame, bg=self.offColor, width=2, height=1)
        localZone.indicator.grid(row=gridRow, column=1)
        localZone.button = tk.Button(localZone.frame, text="Z6",
                                              command= MainView.toggle_status5)
        localZone.button.grid(row=gridRow, column=2)
        localZone.setOff()
        localZone.setTimeOn(1)

        # Sliders
        # gridRow += 1
        # self.temp_slider = tk.Scale(self,
                                    # from_=0, to=100,
                                    # orient="horizontal",
                                    # command=self.temp_slider_changed)
        # self.temp_slider.grid(row=gridRow, column=2)

        # self.temp_slider_value_label = tk.Label(self, text="Temp z F")
        #... self.temp_slider_value_label.grid(row=gridRow, column=3)
        # self.temp_slider_value_label.grid(row=gridRow, column=1)
        # self.temp_slider.set(1)     # start at value 1

class PageProgram(Page):
    entry0 = None
    entry1 = None
    entry2 = None
    entry3 = None
    entry4 = None
    entry5 = None

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        # label = tk.Label(self, text="Program Page")
        # label.pack(side="top", expand=True)

        pad = {'padx': 5, 'pady': 5}

        l1Frame = ttk.LabelFrame(self, text="Zone 1")
        # l1Frame.grid(column=0, row=0, padx=20, pady=20)
        l1Frame.pack(side="left", fill="x", expand=True)
        PageProgram.entry1 = tk.Spinbox(l1Frame, width=5, command=PageProgram.spin0)
        PageProgram.entry1.pack(side="top", **pad)
        button1 = tk.Button(l1Frame, text="button1", command= MainView.toggle_status0)
        button1.pack(side="top", **pad)

        l2Frame = ttk.LabelFrame(self, text="Zone 2")
        # l2Frame.grid(column=1, row=0, padx=20, pady=20)
        l2Frame.pack(side="left", fill="x", expand=True)
        PageProgram.entry2 = tk.Spinbox(l2Frame, width=5, command=PageProgram.spin1)
        PageProgram.entry2.pack(side="top", **pad)
        button2 = tk.Button(l2Frame, text="button2", command= MainView.toggle_status1)
        button2.pack(side="top", **pad)

        l3Frame = ttk.LabelFrame(self, text="Zone 3")
        l3Frame.pack(side="left", fill="x", expand=True)
        PageProgram.entry3 = tk.Spinbox(l3Frame, width=5, command=PageProgram.spin2)
        PageProgram.entry3.pack(side="top", **pad)
        button3 = tk.Button(l3Frame, text="button3", command= MainView.toggle_status2)
        button3.pack(side="top", **pad)

        l4Frame = ttk.LabelFrame(self, text="Zone 4")
        l4Frame.pack(side="left", fill="x", expand=True)
        PageProgram.entry4 = tk.Spinbox(l4Frame, width=5, command=PageProgram.spin3)
        PageProgram.entry4.pack(side="top", **pad)
        button4 = tk.Button(l4Frame, text="button4", command= MainView.toggle_status3)
        button4.pack(side="top", **pad)

        l5Frame = ttk.LabelFrame(self, text="Zone 5")
        l5Frame.pack(side="left", fill="x", expand=True)
        PageProgram.entry5 = tk.Spinbox(l5Frame, width=5, command=PageProgram.spin4)
        PageProgram.entry5.pack(side="top", **pad)
        button5 = tk.Button(l5Frame, text="button5", command= MainView.toggle_status4)
        button5.pack(side="top", **pad)

        l6Frame = ttk.LabelFrame(self, text="Zone 6")
        l6Frame.pack(side="left", fill="x", expand=True)
        PageProgram.entry6 = tk.Spinbox(l6Frame, width=5, command=PageProgram.spin5)
        PageProgram.entry6.pack(side="top", **pad)
        button6 = tk.Button(l6Frame, text="button6", command= MainView.toggle_status0)
        button6.pack(side="top", **pad)

    def spin0():
        MainView.cValue0 = int(PageProgram.entry0.get())
    def spin1():
        MainView.cValue1 = int(PageProgram.entry1.get())
    def spin2():
        MainView.cValue2 = int(PageProgram.entry2.get())
    def spin3():
        MainView.cValue3 = int(PageProgram.entry3.get())
    def spin4():
        MainView.cValue4 = int(PageProgram.entry4.get())
    def spin5(self):
        MainView.cValue5 = int(PageProgram.entry5.get())


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
    # Initialize the zones
    zones = []
    nextZone = 0    # current active zone
    numZones = 6    # total number of zones
    hatLed = led.Led()

    cValue0 = 3
    cValue1 = 3
    cValue2 = 3
    cValue3 = 3
    cValue4 = 3
    cValue5 = 3

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        # Initialize the UI
        self.p1 = PageRun(self)
        self.p2 = PageProgram(self)
        self.p3 = PageTest(self)
        self.p4 = PageSettings(self)

        tabButtonframe = tk.Frame(self)
        container = tk.Frame(self)
        controlButtonframe = tk.Frame(self)
        tabButtonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)
        controlButtonframe.pack(side="top", fill="both", expand=False)

        # pages in place
        self.p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        # tab buttons in place
        b1 = tk.Button(tabButtonframe, text="Run", command=self.p1.show).pack(side ="left")
        b2 = tk.Button(tabButtonframe, text="Program", command=self.p2.show).pack(side ="left")
        b3 = tk.Button(tabButtonframe, text="Test", command=self.p3.show).pack(side ="left")
        b4 = tk.Button(tabButtonframe, text="Settings", command=self.p4.show).pack(side ="left")

        # Sliders
        # gridRow += 1
        self.temp_slider = tk.Scale(controlButtonframe,
                                    from_=0, to=100,
                                    orient="horizontal",
                                    command=self.temp_slider_changed)
        self.temp_slider.pack(side="top", fill="x", expand=False)

        self.temp_slider_value_label = tk.Label(controlButtonframe, text="Temp z F")
        #... self.temp_slider_value_label.grid(row=gridRow, column=3)
        self.temp_slider_value_label.pack(side="top", fill="x", expand=False)
        self.temp_slider.set(1)     # start at value 1


        # control buttons in place
        tk.Button(controlButtonframe, text="Exit", command=self.quit).pack(side="right")
        tk.Button(controlButtonframe, text="All Off", command=MainView.resetZones).pack(side="right")
        self.time_label = tk.Label(controlButtonframe, font=('helvetica', 12), background='gray', foreground='white')
        self.time_label.pack(side="right")

        # Cycle button
        self.cycleButton = tk.Button(controlButtonframe, text="Cycle", command=self.startCycle)
        self.cycleButton.pack(side="right")

        self.p1.show()

    
    # Start a cycle of the zones
    def startCycle(self):
        MainView.nextZone = 0
        self.update_time()

    ### Update the clock every second
    def update_clock(self):
        # print("tick")
        current_time = strftime('%H:%M:%S %p')
        self.time_label.config(text=current_time)
    
        self.time_label.after(1000, self.update_clock)  # Update every second

    # progress through each of the zones
    def update_time(self):
        print("examine timers")
        MainView.allZonesOff()

        if MainView.nextZone >= 0 and MainView.nextZone < MainView.numZones:
            sleepTime = MainView.zones[MainView.nextZone].timeOn()
            print(f"Start Zone {MainView.nextZone} for {sleepTime} x 10")
            # self.zones[self.nextZone].setOn()
            MainView.set_status(MainView.nextZone, True)
            MainView.nextZone += 1

            # Sleep for length of this zone
            self.time_label.after(10 * sleepTime, self.update_time)

    # handle slider update
    def temp_slider_changed(self, value):
        self.temp_slider_value_label.config(text=f"Temp: {value} F")
        v = int(value)

        # update all zones
        for i in range(MainView.numZones):
            MainView.zones[i].setTimeOn(v)
        # self.zones[2].setTimeOn(v+100)

    # Reset system
    def resetZones():
        MainView.allZonesOff()
        MainView.nextZone = MainView.numZones

    # turn off all zones
    def allZonesOff():
        for i in range( MainView.numZones ):
            MainView.set_status(i, False)

    # set one zone on or off
    def set_status(zone, status):
        if status:
            MainView.zones[zone].setOn()
            MainView.hatLed.on(zone+1)
        else:
            MainView.zones[zone].setOff()
            MainView.hatLed.off(zone+1)

    # toggle status of one zone
    def toggle_status0():
        MainView.set_status(0, not MainView.zones[0].isOn())
    def toggle_status1():
        MainView.set_status(1, not MainView.zones[1].isOn())
    def toggle_status2():
        MainView.set_status(2, not MainView.zones[2].isOn())
    def toggle_status3():
        MainView.set_status(3, not MainView.zones[3].isOn())
    def toggle_status4():
        MainView.set_status(4, not MainView.zones[4].isOn())
    def toggle_status5():
        MainView.set_status(5, not MainView.zones[5].isOn())
