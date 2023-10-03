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

        pad = {'padx': 5, 'pady': 5}

        l1Frame = ttk.LabelFrame(self, text="Zone 1")
        # l1Frame.grid(column=0, row=0, padx=20, pady=20)
        l1Frame.pack(side="left", fill="x", expand=True)
        entry1 = tk.Entry(l1Frame, width=5)
        entry1.pack(side="top", **pad)
        button1 = tk.Button(l1Frame, text="button1")
        button1.pack(side="top", **pad)

        l2Frame = ttk.LabelFrame(self, text="Zone 2")
        # l2Frame.grid(column=1, row=0, padx=20, pady=20)
        l2Frame.pack(side="left", fill="x", expand=True)
        entry2 = tk.Entry(l2Frame, width=5)
        entry2.pack(side="top", **pad)
        button2 = tk.Button(l2Frame, text="button2")
        button2.pack(side="top", **pad)

        l3Frame = ttk.LabelFrame(self, text="Zone 3")
        l3Frame.pack(side="left", fill="x", expand=True)
        entry3 = tk.Entry(l3Frame, width=5)
        entry3.pack(side="top", **pad)
        button3 = tk.Button(l3Frame, text="button3")
        button3.pack(side="top", **pad)

        l4Frame = ttk.LabelFrame(self, text="Zone 4")
        l4Frame.pack(side="left", fill="x", expand=True)
        entry4 = tk.Entry(l4Frame, width=5)
        entry4.pack(side="top", **pad)
        button4 = tk.Button(l4Frame, text="button4")
        button4.pack(side="top", **pad)

        l5Frame = ttk.LabelFrame(self, text="Zone 5")
        l5Frame.pack(side="left", fill="x", expand=True)
        entry5 = tk.Entry(l5Frame, width=5)
        entry5.pack(side="top", **pad)
        button5 = tk.Button(l5Frame, text="button5")
        button5.pack(side="top", **pad)

        l6Frame = ttk.LabelFrame(self, text="Zone 6")
        l6Frame.pack(side="left", fill="x", expand=True)
        entry6 = tk.Spinbox(l6Frame, width=5)
        entry6.pack(side="top", **pad)
        button6 = tk.Button(l6Frame, text="button6")
        button6.pack(side="top", **pad)

        # label = tk.Label(self, text="This is page 1")
        # label.pack(side="top", fill="both", expand=True)


class PageProgram(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        # label = tk.Label(self, text="Program Page")
        # label.pack(side="top", expand=True)

        pad = {'padx': 5, 'pady': 5}

        l1Frame = ttk.LabelFrame(self, text="Zone 1")
        # l1Frame.grid(column=0, row=0, padx=20, pady=20)
        l1Frame.pack(side="left", fill="x", expand=True)
        entry1 = tk.Spinbox(l1Frame, width=5)
        entry1.pack(side="top", **pad)
        button1 = tk.Button(l1Frame, text="button1")
        button1.pack(side="top", **pad)

        l2Frame = ttk.LabelFrame(self, text="Zone 2")
        # l2Frame.grid(column=1, row=0, padx=20, pady=20)
        l2Frame.pack(side="left", fill="x", expand=True)
        entry2 = tk.Spinbox(l2Frame, width=5)
        entry2.pack(side="top", **pad)
        button2 = tk.Button(l2Frame, text="button2")
        button2.pack(side="top", **pad)

        l3Frame = ttk.LabelFrame(self, text="Zone 3")
        l3Frame.pack(side="left", fill="x", expand=True)
        entry3 = tk.Spinbox(l3Frame, width=5)
        entry3.pack(side="top", **pad)
        button3 = tk.Button(l3Frame, text="button3")
        button3.pack(side="top", **pad)

        l4Frame = ttk.LabelFrame(self, text="Zone 4")
        l4Frame.pack(side="left", fill="x", expand=True)
        entry4 = tk.Spinbox(l4Frame, width=5)
        entry4.pack(side="top", **pad)
        button4 = tk.Button(l4Frame, text="button4")
        button4.pack(side="top", **pad)

        l5Frame = ttk.LabelFrame(self, text="Zone 5")
        l5Frame.pack(side="left", fill="x", expand=True)
        entry5 = tk.Spinbox(l5Frame, width=5)
        entry5.pack(side="top", **pad)
        button5 = tk.Button(l5Frame, text="button5")
        button5.pack(side="top", **pad)

        l6Frame = ttk.LabelFrame(self, text="Zone 6")
        l6Frame.pack(side="left", fill="x", expand=True)
        entry6 = tk.Spinbox(l6Frame, width=5)
        entry6.pack(side="top", **pad)
        button6 = tk.Button(l6Frame, text="button6")
        button6.pack(side="top", **pad)


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


class ScaGui(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        # p1 = PageRun(self)
        # p2 = PageProgram(self)
        p3 = PageTest(self)
        p4 = PageSettings(self)

        tabButtonframe = tk.Frame(self)
        container = tk.Frame(self)
        controlButtonframe = tk.Frame(self)
        tabButtonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)
        controlButtonframe.pack(side="top", fill="both", expand=False)

        # pages in place
        # p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        # p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        # tab buttons in place
        # b1 = tk.Button(tabButtonframe, text="Run", command=p1.show).pack(side ="left")
        # b2 = tk.Button(tabButtonframe, text="Program", command=p2.show).pack(side ="left")
        b3 = tk.Button(tabButtonframe, text="Test", command=p3.show).pack(side ="left")
        b4 = tk.Button(tabButtonframe, text="Settings", command=p4.show).pack(side ="left")

        # control buttons in place
        tk.Button(controlButtonframe, text="Exit", command=self.quit).pack(side="right")
        tk.Button(controlButtonframe, text="All Off", command=self.allOff).pack(side="right")

        # p1.show()
        p3.show()

    def allOff(self):
        return
    
    def update_clock(self):
        # print("tick")
        # current_time = strftime('%H:%M:%S %p')
        # self.time_label.config(text=current_time)
        self.time_label.after(1000, self.update_clock)  # Update every second
