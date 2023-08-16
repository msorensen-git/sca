import tkinter as tk
from time import strftime

class Zone:
    def __init__(self):        
        self.status = False
        self._timeOn = 0
        
    def setOn(self):
        self.status = True
            
    def setOff(self):
        self.status = False
    
    def toggle(self):
        self.status = not self.status
        
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
        self.zonesLabel = []
        self.zonesIndicator = []
        self.zonesButton = []
        self.zonesZone = []

        self.zonesLabel.append(tk.Label(root, text="Zone 1", padx=10))
        self.zonesLabel[gridRow].grid(row=gridRow, column=0)
        self.zonesIndicator.append(tk.Label(root, bg=self.offColor, width=2, height=1))
        self.zonesIndicator[gridRow].grid(row=gridRow, column=1)
        self.zonesButton.append(tk.Button(root, text="Toggle Z1", command=lambda: self.toggle_status(1)))
        self.zonesButton[gridRow].grid(row=gridRow, column=2)
        self.zonesZone.append(Zone())

        gridRow += 1
        self.zonesLabel.append(tk.Label(root, text="Zone 2", padx=10))
        self.zonesLabel[gridRow].grid(row=gridRow, column=0)
        self.zonesIndicator.append(tk.Label(root, bg=self.offColor, width=2, height=1))
        self.zonesIndicator[gridRow].grid(row=gridRow, column=1)
        self.zonesButton.append(tk.Button(root, text="Toggle Z2", command=lambda: self.toggle_status(2)))
        self.zonesButton[gridRow].grid(row=gridRow, column=2)
        self.zonesZone.append(Zone())

        gridRow += 1
        self.zonesLabel.append(tk.Label(root, text="Zone 3", padx=10))
        self.zonesLabel[gridRow].grid(row=gridRow, column=0)
        self.zonesIndicator.append(tk.Label(root, bg=self.offColor, width=2, height=1))
        self.zonesIndicator[gridRow].grid(row=gridRow, column=1)
        self.zonesButton.append(tk.Button(root, text="Toggle Z3", command=lambda: self.toggle_status(3)))
        self.zonesButton[gridRow].grid(row=gridRow, column=2)
        self.zonesZone.append(Zone())

        gridRow += 1
        self.zonesLabel.append(tk.Label(root, text="Zone 4", padx=10))
        self.zonesLabel[gridRow].grid(row=gridRow, column=0)
        self.zonesIndicator.append(tk.Label(root, bg=self.offColor, width=2, height=1))
        self.zonesIndicator[gridRow].grid(row=gridRow, column=1)
        self.zonesButton.append(tk.Button(root, text="Toggle Z4", command=lambda: self.toggle_status(4)))
        self.zonesButton[gridRow].grid(row=gridRow, column=2)
        self.zonesZone.append(Zone())

        gridRow += 1
        self.zonesLabel.append(tk.Label(root, text="Zone 5", padx=10))
        self.zonesLabel[gridRow].grid(row=gridRow, column=0)
        self.zonesIndicator.append(tk.Label(root, bg=self.offColor, width=2, height=1))
        self.zonesIndicator[gridRow].grid(row=gridRow, column=1)
        self.zonesButton.append(tk.Button(root, text="Toggle Z5", command=lambda: self.toggle_status(5)))
        self.zonesButton[gridRow].grid(row=gridRow, column=2)
        self.zonesZone.append(Zone())

        self.zonesZone[0].setOff()
        self.zonesZone[1].setOff()
        self.zonesZone[2].setOff()
        self.zonesZone[3].setOff()
        self.zonesZone[4].setOff()

        self.zonesZone[0].setTimeOn(1)
        self.zonesZone[1].setTimeOn(1)
        self.zonesZone[2].setTimeOn(1)
        self.zonesZone[3].setTimeOn(1)
        self.zonesZone[4].setTimeOn(1)

        self.set_status(1, False)
        self.set_status(2, False)
        self.set_status(3, False)        
        self.set_status(4, False)        
        self.set_status(5, False)        

        # Sliders
        gridRow += 1
        self.temp_slider = tk.Scale(root, from_=0, to=100, orient="horizontal", command=self.temp_slider_changed)
        self.temp_slider.grid(row=gridRow, column=2)

        self.temp_slider_value_label = tk.Label(root, text="Temp: z F")
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
        # print(f"ET: {self.elapsedTime}  Z1: {self.zonesZone[0].timeOn()}  Z2: {self.zonesZone[1].timeOn()}  Z3: {self.zonesZone[2].timeOn()}  Z4: {self.zonesZone[3].timeOn()}  Z5: {self.zonesZone[4].timeOn()}")

        if (self.elapsedTime == 10):
            self.zonesZone[0].setOn()
            self.set_status(1, True)                                               
            # print("zone 1")
        elif (self.elapsedTime == 10 + self.zonesZone[0].timeOn()):
            self.zonesZone[0].setOff()
            self.set_status(1, False)
            self.zonesZone[1].setOn()
            self.set_status(2, True)
            # print("zone 2")
        elif (self.elapsedTime == 10 + self.zonesZone[0].timeOn() + self.zonesZone[1].timeOn()):
            self.zonesZone[1].setOff()
            self.set_status(2, False)
            self.zonesZone[2].setOn()
            self.set_status(3, True)
            # print("zone 3")
        elif (self.elapsedTime == 10 + self.zonesZone[0].timeOn() + self.zonesZone[1].timeOn() + self.zonesZone[2].timeOn()):
            self.zonesZone[2].setOff()
            self.set_status(3, False)
            self.zonesZone[3].setOn()
            self.set_status(4, True)
            # print("zone 4")
        elif (self.elapsedTime == 10 + self.zonesZone[0].timeOn() + self.zonesZone[1].timeOn() + self.zonesZone[2].timeOn() + self.zonesZone[3].timeOn()):
            self.zonesZone[3].setOff()
            self.set_status(4, False)
            self.zonesZone[4].setOn()
            self.set_status(5, True)
            # print("zone 5")
        elif (self.elapsedTime >= 10 + self.zonesZone[0].timeOn() + self.zonesZone[1].timeOn() + self.zonesZone[2].timeOn() + self.zonesZone[3].timeOn() + self.zonesZone[4].timeOn()):
            self.zonesZone[4].setOff()
            self.set_status(5, False)
            self.elapsedTime = 0
            # print("zone 5 off")
            
        self.time_label.after(100, self.update_time)  # Update every 1000ms (1 second)

    def temp_slider_changed(self, value):
        self.temp_slider_value_label.config(text=f"Temp: {value} F")
        v = int(value)
        self.zonesZone[0].setTimeOn(v)
        self.zonesZone[1].setTimeOn(v)
        self.zonesZone[2].setTimeOn(v)
        self.zonesZone[3].setTimeOn(v)
        self.zonesZone[4].setTimeOn(v)

    def set_status(self, zone, status):
            if status:
                self.zonesIndicator[zone-1].configure(bg="red")
                self.zonesZone[zone-1].setOn()
            else:
                self.zonesIndicator[zone-1].configure(bg=self.offColor)
                self.zonesZone[zone-1].setOff()
    
    def toggle_status(self, zone):
        self.zonesZone[zone-1].toggle()
        self.set_status(zone, self.zonesZone[zone-1].isOn())

# Create a tkinter window
root = tk.Tk()
root.geometry("700x300")

# Create the main app class
app = SprinklerControlPanelApp(root)

# Start the clock update process
app.update_time()

# Run the tkinter event loop
root.mainloop()
