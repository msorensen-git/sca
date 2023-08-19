import tkinter as tk
from time import strftime

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

class SprinklerControlPanelApp:
    def __init__(self, root):
        self.offColor = 'Gray32'
        self.root = root
        self.root.title("Sprinkler Control Panel")      
        self.nextZone = 0    # current active zone
        self.numZones = 5       # total number of zones 

        gridRow = 0
        self.zones = []

        self.zones.append(Zone())
        self.zones[gridRow].label = tk.Label(root, text="Zone 1", padx=10)
        self.zones[gridRow].label.grid(row=gridRow, column=0)
        self.zones[gridRow].indicator = tk.Label(root, width=2, height=1)
        self.zones[gridRow].indicator.grid(row=gridRow, column=1)
        self.zones[gridRow].button = tk.Button(root, text="Toggle Z1", command=lambda: self.toggle_status(0))
        self.zones[gridRow].button.grid(row=gridRow, column=2)
        self.zones[gridRow].setOff()
        self.zones[gridRow].setTimeOn(1)

        gridRow += 1
        self.zones.append(Zone())
        self.zones[gridRow].label = tk.Label(root, text="Zone 2", padx=10)
        self.zones[gridRow].label.grid(row=gridRow, column=0)
        self.zones[gridRow].indicator = tk.Label(root, bg=self.offColor, width=2, height=1)
        self.zones[gridRow].indicator.grid(row=gridRow, column=1)
        self.zones[gridRow].button = tk.Button(root, text="Toggle Z2", command=lambda: self.toggle_status(1))
        self.zones[gridRow].button.grid(row=gridRow, column=2)
        self.zones[gridRow].setOff()
        self.zones[gridRow].setTimeOn(1)

        gridRow += 1
        self.zones.append(Zone())
        self.zones[gridRow].label = tk.Label(root, text="Zone 3", padx=10)
        self.zones[gridRow].label.grid(row=gridRow, column=0)
        self.zones[gridRow].indicator = tk.Label(root, bg=self.offColor, width=2, height=1)
        self.zones[gridRow].indicator.grid(row=gridRow, column=1)
        self.zones[gridRow].button = tk.Button(root, text="Toggle Z3", command=lambda: self.toggle_status(2))
        self.zones[gridRow].button.grid(row=gridRow, column=2)
        self.zones[gridRow].setOff()
        self.zones[gridRow].setTimeOn(1)

        gridRow += 1
        self.zones.append(Zone())
        self.zones[gridRow].label = tk.Label(root, text="Zone 4", padx=10)
        self.zones[gridRow].label.grid(row=gridRow, column=0)
        self.zones[gridRow].indicator = tk.Label(root, bg=self.offColor, width=2, height=1)
        self.zones[gridRow].indicator.grid(row=gridRow, column=1)
        self.zones[gridRow].button = tk.Button(root, text="Toggle Z4", command=lambda: self.toggle_status(3))
        self.zones[gridRow].button.grid(row=gridRow, column=2)
        self.zones[gridRow].setOff()
        self.zones[gridRow].setTimeOn(1)

        gridRow += 1
        self.zones.append(Zone())
        self.zones[gridRow].label = tk.Label(root, text="Zone 5", padx=10)
        self.zones[gridRow].label.grid(row=gridRow, column=0)
        self.zones[gridRow].indicator = tk.Label(root, bg=self.offColor, width=2, height=1)
        self.zones[gridRow].indicator.grid(row=gridRow, column=1)
        self.zones[gridRow].button = tk.Button(root, text="Toggle Z5", command=lambda: self.toggle_status(4))
        self.zones[gridRow].button.grid(row=gridRow, column=2)
        self.zones[gridRow].setOff()
        self.zones[gridRow].setTimeOn(1)

        # Sliders
        gridRow += 1
        self.temp_slider = tk.Scale(root, from_=0, to=100, orient="horizontal", command=self.temp_slider_changed)
        self.temp_slider.grid(row=gridRow, column=2)

        self.temp_slider_value_label = tk.Label(root, text="Temp z F")
        self.temp_slider_value_label.grid(row=gridRow, column=3)
        self.temp_slider.set(1)     # start at value 1

        # Create a label to display the time
        gridRow += 1
        self.time_label = tk.Label(root, font=('helvetica', 12), background='gray', foreground='white')
        self.time_label.grid(row=gridRow, column=8)

        # Cycle button
        cycleButton = tk.Button(root, text="Cycle", command= self.startCycle)
        cycleButton.grid(row=gridRow, column=1)

        # elapsed time for controlling the zone on/off times in a cycle
        # self.elapsedTime = 0

    def startCycle(self):
        self.nextZone = 0
        self.update_time()

    def update_clock(self):
        # print("tick")
        current_time = strftime('%H:%M:%S %p')
        self.time_label.config(text=current_time)
        self.time_label.after(1000, self.update_clock)  # Update every 1000ms (1 second)

    def update_time(self):
        # print("examine timers")
        self.allZonesOff()

        if self.nextZone >=0 and self.nextZone < self.numZones:
            sleepTime = self.zones[self.nextZone].timeOn()
            print(f"Start Zone {self.nextZone} for {sleepTime} x 10")
            self.zones[self.nextZone].setOn()
            self.nextZone += 1

            self.time_label.after(10 * sleepTime, self.update_time)  # Sleep for length of this zone        

    def allZonesOff(self):
        for i in range(self.numZones):
            self.zones[i].setOff()

    def temp_slider_changed(self, value):
        self.temp_slider_value_label.config(text=f"Temp: {value} F")
        v = int(value)

        # update all zones
        for i in range(self.numZones):
            self.zones[i].setTimeOn(v)
        # self.zones[2].setTimeOn(v+100)

    def set_status(self, zone, status):
            if status:
                self.zones[zone].indicator.configure(bg="red")
                self.zones[zone].setOn()
            else:
                self.zones[zone].indicator.configure(bg=self.offColor)
                self.zones[zone].setOff()
    
    def toggle_status(self, zone):
        self.zones[zone].toggle()
        self.set_status(zone, self.zones[zone].isOn())

# Create a tkinter window
root = tk.Tk()
root.geometry("700x300")

# Create the main app class
app = SprinklerControlPanelApp(root)

# Start the clock update process
app.update_clock()
# app.update_time()

# Run the tkinter event loop
root.mainloop()
