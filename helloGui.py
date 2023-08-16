import tkinter as tk

#def callback

def button_call():
    print("debug button click")
    
window = tk.Tk()
window.geometry('300x200')

#write text
text = tk.Label(window, text= "Hello World")
text.pack()

#create button
button = tk.Button(window, text= "click here", bd = '5', command= button_call)
button.pack(side = 'top')

window.mainloop()
