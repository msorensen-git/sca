import tkinter as tk
from tkinter import ttk



class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
       

        controlButtonframe = tk.Frame(self)
        controlButtonframe.pack(side="top", fill="both", expand=False)

        # control buttons in place
        tk.Button(controlButtonframe, text="Exit", command=self.quit).pack(side="right")
        tk.Button(controlButtonframe, text="All Off", command=self.allOff).pack(side="right")


    def allOff(self):
        return


if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    root.title("Tabbed Pages App")
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("700x400")
    root.mainloop()
