import tkinter as tk
from tkinter import ttk


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class PageRun(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        l1Frame = ttk.LabelFrame(self, text="Zone 1")
        # l1Frame.grid(column=0, row=0, padx=20, pady=20)
        # l1Frame.grid(column=0, row=0, padx=20, pady=20)
        l1Frame.pack(side="left", fill="both", expand=True)
        # label1 = tk.Label(l1Frame, text="first Label")
        # entry1 = tk.Entry(l1Frame)

        l2Frame = ttk.LabelFrame(self, text="Zone 2")
        # l2Frame.grid(column=1, row=0, padx=20, pady=20)
        l2Frame.pack(side="left", fill="both", expand=True)
        # label2 = tk.Label(l2Frame, text="second Label")
        # entry2 = tk.Entry(l2Frame)

        l3Frame = ttk.LabelFrame(self, text="Zone 3")
        l3Frame.pack(side="left", fill="both", expand=True)

        l4Frame = ttk.LabelFrame(self, text="Zone 4")
        l4Frame.pack(side="left", fill="both", expand=True)

        l5Frame = ttk.LabelFrame(self, text="Zone 5")
        l5Frame.pack(side="left", fill="both", expand=True)

        l6Frame = ttk.LabelFrame(self, text="Zone 6")
        l6Frame.pack(side="left", fill="both", expand=True)

        # label = tk.Label(self, text="This is page 1")
        # label.pack(side="top", fill="both", expand=True)


class PageProgram(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Program Page")
        label.pack(side="top", fill="both", expand=True)


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


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = PageRun(self)
        p2 = PageProgram(self)
        p3 = PageTest(self)
        p4 = PageSettings(self)

        tabButtonframe = tk.Frame(self)
        container = tk.Frame(self)
        controlButtonframe = tk.Frame(self)
        tabButtonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)
        controlButtonframe.pack(side="top", fill="both", expand=False)

        # pages in place
        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        # tab buttons in place
        b1 = tk.Button(tabButtonframe, text="Run", command=p1.show)
        b2 = tk.Button(tabButtonframe, text="Program", command=p2.show)
        b3 = tk.Button(tabButtonframe, text="Test", command=p3.show)
        b4 = tk.Button(tabButtonframe, text="Settings", command=p4.show)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")

        # control buttons in place
        bx = tk.Button(controlButtonframe, text="Exit", command=self.exitApp)
        bx.pack(side="right")
        ba = tk.Button(controlButtonframe, text="All Off", command=self.allOff)
        ba.pack(side="right")

        p1.show()

    def exitApp(self):
        return

    def allOff(self):
        return


if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()
