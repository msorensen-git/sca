import tkinter as tk

class IndicatorLightsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Indicator Lights")
        
        self.red_status = tk.StringVar()
        self.green_status = tk.StringVar()
        self.blue_status = tk.StringVar()
        
        self.red_label = tk.Label(root, text="Red:", padx=10)
        self.green_label = tk.Label(root, text="Green:", padx=10)
        self.blue_label = tk.Label(root, text="Blue:", padx=10)
        
        self.red_indicator = tk.Label(root, textvariable=self.red_status, bg="gray", width=2, height=1)
        self.green_indicator = tk.Label(root, textvariable=self.green_status, bg="gray", width=2, height=1)
        self.blue_indicator = tk.Label(root, textvariable=self.blue_status, bg="gray", width=2, height=1)
        
        self.red_label.grid(row=0, column=0)
        self.green_label.grid(row=1, column=0)
        self.blue_label.grid(row=2, column=0)
        
        self.red_indicator.grid(row=0, column=1)
        self.green_indicator.grid(row=1, column=1)
        self.blue_indicator.grid(row=2, column=1)
        
        self.set_status("red", False)
        self.set_status("green", False)
        self.set_status("blue", False)
        
        self.red_button = tk.Button(root, text="Toggle Red", command=lambda: self.toggle_status("red"))
        self.green_button = tk.Button(root, text="Toggle Green", command=lambda: self.toggle_status("green"))
        self.blue_button = tk.Button(root, text="Toggle Blue", command=lambda: self.toggle_status("blue"))
        
        self.red_button.grid(row=0, column=2)
        self.green_button.grid(row=1, column=2)
        self.blue_button.grid(row=2, column=2)

    def set_status(self, color, status):
        if color == "red":
            self.red_status.set("ON" if status else "OFF")
            self.red_indicator.configure(bg="red" if status else "gray")
        elif color == "green":
            self.green_status.set("ON" if status else "OFF")
            self.green_indicator.configure(bg="green" if status else "gray")
        elif color == "blue":
            self.blue_status.set("ON" if status else "OFF")
            self.blue_indicator.configure(bg="blue" if status else "gray")
    
    def toggle_status(self, color):
        if color == "red":
            self.set_status("red", not self.red_status.get() == "ON")
        elif color == "green":
            self.set_status("green", not self.green_status.get() == "ON")
        elif color == "blue":
            self.set_status("blue", not self.blue_status.get() == "ON")

root = tk.Tk()
app = IndicatorLightsApp(root)
root.mainloop()
