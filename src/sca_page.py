import tkinter as tk

from tkinter import ttk


class Page(tk.Frame):
    """ Generic GUI Page """
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        """ Show this page """
        self.lift()

