import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime('%H:%M:%S %p')
    time_label.config(text=current_time)
    time_label.after(900, update_time)  # Update every 1000ms (1 second)

# Create a tkinter window
window = tk.Tk()
window.title('Digital Clock')

# Create a label to display the time
time_label = tk.Label(window, font=('helvetica', 48), background='black', foreground='white')
time_label.pack(padx=20, pady=20)

# Start the clock update process
update_time()

# Run the tkinter event loop
window.mainloop()
