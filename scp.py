import tkinter as tk

# simple view
import scaGui  # as gui

# tabbed view
import scaGuiMain  # as gui

if __name__ == "__main__":
    # Create a tkinter window
    root = tk.Tk()
    root.title("Sprintkler Control App")

    # if True:
    if False:
        # Create the main app class
        app = scaGui.SprinklerControlPanelApp(root)

        # Start the clock update process
        app.update_clock()
        # app.update_time()
    else:
        main = scaGuiMain.MainView(root)
        main.pack(side="top", fill="both", expand=True)
        main.update_clock()

    root.wm_geometry("700x400")

    # Run the tkinter event loop
    root.mainloop()
