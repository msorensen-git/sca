import tkinter as tk

import scaZone
# simple view
import scaGui as gui
# tabbed view
# import scaGuiMain as gui

if __name__ == "__main__":
    # Create a tkinter window
    root = tk.Tk()
    root.geometry("700x300")
    root.title("Sprintkler Control App")

    # Create the main app class
    app = gui.SprinklerControlPanelApp(root)
  
    # Start the clock update process
    app.update_clock()
    # app.update_time()

    # Run the tkinter event loop
    root.mainloop()
