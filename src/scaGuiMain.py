import tkinter as tk
import pickle
from tkinter import ttk
from time import strftime
# import numpy as np

import scaLed as led
import scaZone as zone_data

import sca_page as Page


class PageRun(Page.Page):
    """ Run page for normal operation """
    def __init__(self, *args, **kwargs):
        Page.Page.__init__(self, *args, **kwargs)

        # pad = {'padx': 5, 'pady': 5}
        self.off_color = 'Gray32'
        grid_row = 0

        MainView.zones.append(zone_data.Zone())
        _zone = MainView.zones[grid_row]
        _zone.frame = ttk.LabelFrame(self, text="Zone 1")
        _zone.frame.pack(side="left", fill="x", expand=True)
        # localZone.label = tk.Label(localZone.frame, text="Zone 1", padx=10)
        # localZone.label.grid(row=gridRow, column=0)
        _zone.indicator = tk.Label(_zone.frame, bg=self.off_color,
                                       width=2, height=1)
        _zone.indicator.grid(row=grid_row, column=1)
        _zone.button = tk.Button(_zone.frame, text="Z1",
                                     command=MainView.toggle_status0)
        _zone.button.grid(row=grid_row, column=2)
        _zone.set_off()
        _zone.set_time_on(1)

        grid_row += 1
        MainView.zones.append(zone_data.Zone())
        _zone = MainView.zones[grid_row]
        _zone.frame = ttk.LabelFrame(self, text="Zone 2")
        _zone.frame.pack(side="left", fill="x", expand=True)
        # localZone.label = tk.Label(localZone.frame, text="Zone 2", padx=10)
        # localZone.label.grid(row=gridRow, column=0)
        _zone.indicator = tk.Label(_zone.frame, bg=self.off_color,
                                       width=2, height=1)
        _zone.indicator.grid(row=grid_row, column=1)
        _zone.button = tk.Button(_zone.frame,
                                     text="Z2",
                                     command=MainView.toggle_status1)
        _zone.button.grid(row=grid_row, column=2)
        _zone.set_off()
        _zone.set_time_on(1)

        grid_row += 1
        MainView.zones.append(zone_data.Zone())
        _zone = MainView.zones[grid_row]
        _zone.frame = ttk.LabelFrame(self, text="Zone 3")
        _zone.frame.pack(side="left", fill="x", expand=True)
        # localZone.label = tk.Label(localZone.frame, text="Zone 2", padx=10)
        # localZone.label.grid(row=gridRow, column=0)
        _zone.indicator = tk.Label(_zone.frame, bg=self.off_color,
                                       width=2, height=1)
        _zone.indicator.grid(row=grid_row, column=1)
        _zone.button = tk.Button(_zone.frame,
                                     text="Z3",
                                     command=MainView.toggle_status2)
        _zone.button.grid(row=grid_row, column=2)
        _zone.set_off()
        _zone.set_time_on(1)

        grid_row += 1
        MainView.zones.append(zone_data.Zone())
        _zone = MainView.zones[grid_row]
        _zone.frame = ttk.LabelFrame(self, text="Zone 4")
        _zone.frame.pack(side="left", fill="x", expand=True)
        # localZone.label = tk.Label(localZone.frame, text="Zone 4", padx=10)
        # localZone.label.grid(row=gridRow, column=0)
        _zone.indicator = tk.Label(_zone.frame,
                                       bg=self.off_color, width=2, height=1)
        _zone.indicator.grid(row=grid_row, column=1)
        _zone.button = tk.Button(_zone.frame,
                                     text="Z4",
                                     command=MainView.toggle_status3)
        _zone.button.grid(row=grid_row, column=2)
        _zone.set_off()
        _zone.set_time_on(1)

        grid_row += 1
        MainView.zones.append(zone_data.Zone())
        _zone = MainView.zones[grid_row]
        _zone.frame = ttk.LabelFrame(self, text="Zone 5")
        _zone.frame.pack(side="left", fill="x", expand=True)
        # localZone.label = tk.Label(localZone.frame, text="Zone 5", padx=10)
        # localZone.label.grid(row=gridRow, column=0)
        _zone.indicator = tk.Label(_zone.frame,
                                       bg=self.off_color, width=2, height=1)
        _zone.indicator.grid(row=grid_row, column=1)
        _zone.button = tk.Button(_zone.frame,
                                     text="Z5",
                                     command=MainView.toggle_status4)
        _zone.button.grid(row=grid_row, column=2)
        _zone.set_off()
        _zone.set_time_on(1)

        grid_row += 1
        MainView.zones.append(zone_data.Zone())
        _zone = MainView.zones[grid_row]
        _zone.frame = ttk.LabelFrame(self, text="Zone 6")
        _zone.frame.pack(side="left", fill="x", expand=True)
        # localZone.label = tk.Label(localZone.frame, text="Zone 6", padx=10)
        # localZone.label.grid(row=gridRow, column=0)
        _zone.indicator = tk.Label(_zone.frame,
                                       bg=self.off_color, width=2, height=1)
        _zone.indicator.grid(row=grid_row, column=1)
        _zone.button = tk.Button(_zone.frame,
                                     text="Z6",
                                     command=MainView.toggle_status5)
        _zone.button.grid(row=grid_row, column=2)
        _zone.set_off()
        _zone.set_time_on(1)


class PageProgram(Page.Page):
    """ Programming GUI page """

    def __init__(self, *args, **kwargs):
        """ Initialize Programming page """
        Page.Page.__init__(self, *args, **kwargs)

        pad = {'padx': 5, 'pady': 5}

        # Spinnter for zone 1
        self.spin_var1 = tk.DoubleVar(
            value=MainView.zones[0].time_on())  # initial value
        l1_frame = ttk.LabelFrame(self, text="Zone 1")
        l1_frame.pack(side="left", fill="x", expand=True)
        entry1 = tk.Spinbox(l1_frame, width=5,
                            from_=0, to=30,
                            textvariable=self.spin_var1,
                            command=self.spin1)
        entry1.pack(side="top", **pad)
        button1 = tk.Button(l1_frame, text="button1",
                            command=MainView.toggle_status0)
        button1.pack(side="top", **pad)

        self.spin_var2 = tk.DoubleVar(
            value=MainView.zones[1].time_on())
        l2_frame = ttk.LabelFrame(self, text="Zone 2")
        l2_frame.pack(side="left", fill="x", expand=True)
        entry2 = tk.Spinbox(l2_frame, width=5,
                            from_=0, to=30,
                            textvariable=self.spin_var2,
                            command=self.spin2)
        entry2.pack(side="top", **pad)
        button2 = tk.Button(l2_frame, text="button2",
                            command=MainView.toggle_status1)
        button2.pack(side="top", **pad)

        self.spin_var3 = tk.DoubleVar(
            value=MainView.zones[2].time_on())
        l3_frame = tk.LabelFrame(self, text="Zone 3")
        l3_frame.pack(side="left", fill="x", expand=True)
        entry3 = tk.Spinbox(l3_frame, width=5,
                            from_=0, to=30,
                            textvariable=self.spin_var3,
                            command=self.spin3)
        entry3.pack(side="top", **pad)
        button3 = tk.Button(l3_frame, text="button3",
                            command=MainView.toggle_status2)
        button3.pack(side="top", **pad)

        self.spin_var4 = tk.DoubleVar(
            value=MainView.zones[3].time_on())
        l4_frame = ttk.LabelFrame(self, text="Zone 4")
        l4_frame.pack(side="left", fill="x", expand=True)
        entry4 = tk.Spinbox(l4_frame, width=5,
                            from_=0, to=30,
                            textvariable=self.spin_var4,
                            command=self.spin4)
        entry4.pack(side="top", **pad)
        button4 = tk.Button(l4_frame, text="button4",
                            command=MainView.toggle_status3)
        button4.pack(side="top", **pad)

        self.spin_var5 = tk.DoubleVar(
            value=MainView.zones[4].time_on())
        l5_frame = ttk.LabelFrame(self, text="Zone 5")
        l5_frame.pack(side="left", fill="x", expand=True)
        entry5 = tk.Spinbox(l5_frame, width=5,
                            from_=0, to=30,
                            textvariable=self.spin_var5,
                            command=self.spin5)
        entry5.pack(side="top", **pad)
        button5 = tk.Button(l5_frame, text="button5",
                            command=MainView.toggle_status4)
        button5.pack(side="top", **pad)

        self.spin_var6 = tk.DoubleVar(
            value=MainView.zones[5].time_on())
        l6_frame = ttk.LabelFrame(self, text="Zone 6")
        l6_frame.pack(side="left", fill="x", expand=True)
        entry6 = tk.Spinbox(l6_frame, width=5,
                            from_=0, to=30,
                            textvariable=self.spin_var6,
                            command=self.spin6)
        entry6.pack(side="top", **pad)
        button6 = tk.Button(l6_frame, text="button6",
                            command=MainView.toggle_status5)
        button6.pack(side="top", **pad)

    def spin1(self):
        """ Handle spinner 1 """
        lval = self.spin_var1.get()
        MainView.zones[0].set_time_on(int(lval))

    def spin2(self):
        """ Handle spinner 2 """
        lval = self.spin_var2.get()
        MainView.zones[1].set_time_on(int(lval))

    def spin3(self):
        """ Handle spinner 3 """
        lval = self.spin_var3.get()
        MainView.zones[2].set_time_on(int(lval))

    def spin4(self):
        """ Handle spinner 4 """
        lval = self.spin_var4.get()
        MainView.zones[3].set_time_on(int(lval))

    def spin5(self):
        """ Handle spinner 5 """
        lval = self.spin_var5.get()
        MainView.zones[4].set_time_on(int(lval))

    def spin6(self):
        """ Handle spinner 6 """
        lval = self.spin_var6.get()
        MainView.zones[5].set_time_on(int(lval))


class PageTest(Page.Page):
    """ Test page """
    def __init__(self, *args, **kwargs):
        """ Initialize Test page """
        Page.Page.__init__(self, *args, **kwargs)

        label = tk.Label(self, text="Test Page")
        label.pack(side="top", fill="both", expand=True)


class PageSettings(Page.Page):
    """ Settings page """
    def __init__(self, *args, **kwargs):
        """ Initialize PageSettings """
        Page.Page.__init__(self, *args, **kwargs)
        
        label = tk.Label(self, text="Settings Page")
        label.pack(side="top", fill="both", expand=True)


class MainView(tk.Frame):
    """ Layout using grid """
    # Initialize the zones
    zones: list[zone_data.Zone] = []
    nextZone = 0    # current active zone
    numZones = 6    # total number of zones
    hatLed = led.Led()

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        # Initialize the UI
        self.p1 = PageRun(self)
        self.p2 = PageProgram(self)
        self.p3 = PageTest(self)
        self.p4 = PageSettings(self)

        tab_button_frame = tk.Frame(self)
        container = tk.Frame(self)
        control_button_frame = tk.Frame(self)
        tab_button_frame.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)
        control_button_frame.pack(side="top", fill="both", expand=False)

        # pages in place
        self.p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        # tab buttons in place
        tk.Button(tab_button_frame, text="Run",
                  command=self.p1.show).pack(side="left")
        tk.Button(tab_button_frame, text="Program",
                  command=self.p2.show).pack(side="left")
        tk.Button(tab_button_frame, text="Test",
                  command=self.p3.show).pack(side="left")
        tk.Button(tab_button_frame, text="Settings",
                  command=self.p4.show).pack(side="left")

        # Sliders
        self.temp_value = 0
        self.temp_slider = tk.Scale(control_button_frame,
                                    from_=0, to=100,
                                    orient="horizontal",
                                    command=self.temp_slider_changed)
        self.temp_slider.pack(side="top", fill="x", expand=False)

        self.temp_slider_value_label = tk.Label(
            control_button_frame, text="Temp z F")
        self.temp_slider_value_label.pack(side="top", fill="x", expand=False)
        self.temp_slider.set(self.temp_value)   # start at value 1s

        # control buttons in place
        tk.Button(control_button_frame, text="Exit",
                  command=self.exit_save).pack(side="right")
        tk.Button(control_button_frame, text="All Off",
                  command=MainView.reset_zones).pack(side="right")
        self.time_label = tk.Label(control_button_frame, font=('helvetica', 12),
                                   background='gray', foreground='white')
        self.time_label.pack(side="right")

        # Cycle button
        self.cycle_button = tk.Button(control_button_frame,
                                     text="Cycle", command=self.start_cycle)
        self.cycle_button.pack(side="right")

        self.p1.show()

    # Start a cycle of the zones
    def start_cycle(self):
        """ Start a new cycle """
        MainView.nextZone = 0
        self.update_time()

    def update_clock(self):
        """ update the clock every second """
        # print("tick")
        current_time = strftime('%H:%M:%S %p')
        self.time_label.config(text=current_time)

        self.time_label.after(1000, self.update_clock)  # Update every second

    def update_time(self):
        """ cycle through all zones """
        print("examine timers")
        MainView.all_zones_off()

        if MainView.nextZone >= 0 and MainView.nextZone < MainView.numZones:
            sleep_time = MainView.zones[MainView.nextZone].time_on()
            sleep_time += self.temp_value
            print(f"Start Zone {MainView.nextZone} for {sleep_time} x 10")
            MainView.set_status(MainView.nextZone, True)
            MainView.nextZone += 1

            # Sleep for length of this zone
            self.time_label.after(10 * sleep_time, self.update_time)

    # handle slider update
    def temp_slider_changed(self, value):
        """ handle slider update """
        self.temp_slider_value_label.config(text=f"Temp: {value} F")
        self.temp_value = int(value)

    # Reset system
    def reset_zones():
        """ cycle is finished """
        MainView.all_zones_off()
        MainView.nextZone = MainView.numZones

    def all_zones_off():
        """ set all zones to off """
        for i in range(MainView.numZones):
            MainView.set_status(i, False)

    # set one zone on or off
    def set_status(zone, status):
        """ Set zone status """
        if status:
            MainView.zones[zone].set_on()
            MainView.hatLed.on(zone+1)
            MainView.zones[zone].indicator.configure(bg='red')

        else:
            MainView.zones[zone].set_off()
            MainView.hatLed.off(zone+1)
            MainView.zones[zone].indicator.configure(bg='Gray32')

    # toggle status of one zone
    def toggle_status0():
        """ Toggle zone 0 """
        MainView.set_status(0, not MainView.zones[0].is_on())

    def toggle_status1():
        """ Toggle zone 1 """
        MainView.set_status(1, not MainView.zones[1].is_on())

    def toggle_status2():
        """ Toggle zone 2 """
        MainView.set_status(2, not MainView.zones[2].is_on())

    def toggle_status3():
        """ Toggle zone 3 """
        MainView.set_status(3, not MainView.zones[3].is_on())

    def toggle_status4():
        """ Toggle zone 4"""
        MainView.set_status(4, not MainView.zones[4].is_on())

    def toggle_status5():
        """ Toggle zone 5 """
        MainView.set_status(5, not MainView.zones[5].is_on())

    def exit_save(self):
        """ Exit app after saving settings """
        with open('scpa.pkl', 'wb') as f:  # Python 3: open(..., 'wb')
            # pickle.dump([obj0, obj1, obj2], f)
            pickle.dump(self.temp_value, f)
        print("quitting")
        self.quit()
