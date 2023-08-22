import tkinter as tk

import scaZone
import scaGui


# Create a tkinter window
root = tk.Tk()
root.geometry("700x300")

# Create the main app class
app = scaGui.SprinklerControlPanelApp(root)

# Start the clock update process
app.update_clock()
# app.update_time()

# Run the tkinter event loop
root.mainloop()
