import tkinter as tk
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Spinbox Demo')


# spinbox
current_value = tk.StringVar()
spin_box = tk.Spinbox(
    root,
    from_=0,
    to=100,
    values=(0, 10, 20, 30, 40, 50),
    width=5,
    textvariable=current_value,
    wrap=True)

spin_box.pack()

root.mainloop()
