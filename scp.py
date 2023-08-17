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

        gridRow = 0
        self.zones = []

        self.zones.append(Zone())
        self.zones[gridRow].label = tk.Label(root, text="Zone 1", padx=10)
        self.zones[gridRow].label.grid(row=gridRow, column=0)
        self.zones[gridRow].indicator = tk.Label(root, width=2, height=1)
        self.zones[gridRow].indicator.grid(row=gridRow, column=1)
        self.zones[gridRow].button = tk.Button(root, text="Toggle Z1", command=lambda: self.toggle_status(1))
        self.zones[gridRow].button.grid(row=gridRow, column=2)
        self.zones[gridRow].setOff()
        self.zones[gridRow].setTimeOn(1)

        gridRow += 1
        self.zones.append(Zone())
        self.zones[gridRow].label = tk.Label(root, text="Zone 2", padx=10)
        self.zones[gridRow].label.grid(row=gridRow, column=0)
        self.zones[gridRow].indicator = tk.Label(root, bg=self.offColor, width=2, height=1)
        self.zones[gridRow].indicator.grid(row=gridRow, column=1)
        self.zones[gridRow].button = tk.Button(root, text="Toggle Z2", command=lambda: self.toggle_status(2))
        self.zones[gridRow].button.grid(row=gridRow, column=2)
        self.zones[gridRow].setOff()
        self.zones[gridRow].setTimeOn(1)

        gridRow += 1
        self.zones.append(Zone())
        self.zones[gridRow].label = tk.Label(root, text="Zone 3", padx=10)
        self.zones[gridRow].label.grid(row=gridRow, column=0)
        self.zones[gridRow].indicator = tk.Label(root, bg=self.offColor, width=2, height=1)
        self.zones[gridRow].indicator.grid(row=gridRow, column=1)
        self.zones[gridRow].button = tk.Button(root, text="Toggle Z3", command=lambda: self.toggle_status(3))
        self.zones[gridRow].button.grid(row=gridRow, column=2)
        self.zones[gridRow].setOff()
        self.zones[gridRow].setTimeOn(1)

        gridRow += 1
        self.zones.append(Zone())
        self.zones[gridRow].label = tk.Label(root, text="Zone 4", padx=10)
        self.zones[gridRow].label.grid(row=gridRow, column=0)
        self.zones[gridRow].indicator = tk.Label(root, bg=self.offColor, width=2, height=1)
        self.zones[gridRow].indicator.grid(row=gridRow, column=1)
        self.zones[gridRow].button = tk.Button(root, text="Toggle Z4", command=lambda: self.toggle_status(4))
        self.zones[gridRow].button.grid(row=gridRow, column=2)
        self.zones[gridRow].setOff()
        self.zones[gridRow].setTimeOn(1)

        gridRow += 1
        self.zones.append(Zone())
        self.zones[gridRow].label = tk.Label(root, text="Zone 5", padx=10)
        self.zones[gridRow].label.grid(row=gridRow, column=0)
        self.zones[gridRow].indicator = tk.Label(root, bg=self.offColor, width=2, height=1)
        self.zones[gridRow].indicator.grid(row=gridRow, column=1)
        self.zones[gridRow].button = tk.Button(root, text="Toggle Z5", command=lambda: self.toggle_status(5))
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

        # elapsed time for controlling the zone on/off times in a cycle
        self.elapsedTime = 0

    def update_time(self):
        current_time = strftime('%H:%M:%S %p')
        self.time_label.config(text=current_time)
        self.elapsedTime += 1
        # print(f"ET: {self.elapsedTime}  Z1: {self.zones[0].timeOn()}  Z2: {self.zones[1].timeOn()}  Z3: {self.zones[2].timeOn()}  Z4: {self.zones[3].timeOn()}  Z5: {self.zones[4].timeOn()}")

        timeZone1 = self.zones[0].timeOn()
        timeZone2 = timeZone1 + self.zones[1].timeOn()
        timeZone3 = timeZone2 + self.zones[2].timeOn()
        timeZone4 = timeZone3 + self.zones[3].timeOn()
        timeZone5 = timeZone4 + self.zones[4].timeOn()
        
        if self.elapsedTime >= 10 + timeZone5:
            self.zones[4].setOff()
            self.elapsedTime = 0
            # print("zone 5 off")
        elif self.elapsedTime >= 10 + timeZone4:
            self.zones[3].setOff()
            self.zones[4].setOn()
            # print("zone 5")
        elif self.elapsedTime >= 10 + timeZone3:
            self.zones[2].setOff()
            self.zones[3].setOn()
            # print("zone 4")
        elif self.elapsedTime >= 10 + timeZone2:
            self.zones[1].setOff()
            self.zones[2].setOn()
            # print("zone 3")
        elif self.elapsedTime >= 10 + timeZone1:
            self.zones[0].setOff()
            self.zones[1].setOn()
            # print("zone 2")
        elif self.elapsedTime >= 10:
            self.zones[0].setOn()
            # print("zone 1")
            
        self.time_label.after(100, self.update_time)  # Update every 1000ms (1 second)

    def temp_slider_changed(self, value):
        self.temp_slider_value_label.config(text=f"Temp: {value} F")
        v = int(value)
        self.zones[0].setTimeOn(v)
        self.zones[1].setTimeOn(v)
        self.zones[2].setTimeOn(v)
        self.zones[3].setTimeOn(v)
        self.zones[4].setTimeOn(v)

    def set_status(self, zone, status):
            if status:
                self.zones[zone-1].indicator.configure(bg="red")
                self.zones[zone-1].setOn()
            else:
                self.zones[zone-1].indicator.configure(bg=self.offColor)
                self.zones[zone-1].setOff()
    
    def toggle_status(self, zone):
        self.zones[zone-1].toggle()
        self.set_status(zone, self.zones[zone-1].isOn())

# Create a tkinter window
root = tk.Tk()
root.geometry("700x300")

# Create the main app class
app = SprinklerControlPanelApp(root)

# Start the clock update process
app.update_time()

# Run the tkinter event loop
root.mainloop()
