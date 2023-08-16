import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Message", "Button Clicked!")

def update_slider_label(value):
    slider_label.config(text=f"Slider Value: {value}")

app = tk.Tk()
app.title("GUI Controls Example")

# Labels
name_label = tk.Label(app, text="Name:")
age_label = tk.Label(app, text="Age:")
slider_label = tk.Label(app, text="Slider Value: 50")

name_label.pack()
age_label.pack()
slider_label.pack()

# Entry fields
name_entry = tk.Entry(app)
age_entry = tk.Entry(app)

name_entry.pack()
age_entry.pack()

# Checkbuttons
gender_var = tk.StringVar()
male_checkbox = tk.Checkbutton(app, text="Male", variable=gender_var, onvalue="Male", offvalue="")
female_checkbox = tk.Checkbutton(app, text="Female", variable=gender_var, onvalue="Female", offvalue="")

male_checkbox.pack()
female_checkbox.pack()

# Sliders
slider = tk.Scale(app, from_=0, to=100, orient=tk.HORIZONTAL, command=update_slider_label)
slider.set(50)  # Set initial slider value
slider.pack()

# Buttons
message_button = tk.Button(app, text="Show Message", command=show_message)
submit_button = tk.Button(app, text="Submit")

message_button.pack()
submit_button.pack()

app.mainloop()
