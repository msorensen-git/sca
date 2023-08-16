import tkinter as tk
import time
import math

class AnalogClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Analog Clock")
        
        self.canvas = tk.Canvas(root, width=300, height=300, bg="white")
        self.canvas.pack()
        
        self.center_x = 150
        self.center_y = 150
        self.radius = 120
        
        self.hour_hand = None
        self.minute_hand = None
        self.second_hand = None
        
        self.draw_clock()
        self.update_time()

    def draw_clock(self):
        self.canvas.create_oval(self.center_x - self.radius, self.center_y - self.radius,
                                self.center_x + self.radius, self.center_y + self.radius)
        
        margin = 15
        
        for i in range(12):
            angle = math.radians(60 - i * 30)
            x = self.center_x + (self.radius - margin) * math.cos(angle)
            y = self.center_y - (self.radius - margin) * math.sin(angle)
            self.canvas.create_text(x, y, text=str(i + 1), font=("Helvetica", 12, "bold"))
        
        self.hour_hand = self.canvas.create_line(self.center_x, self.center_y, self.center_x, self.center_y, width=4)
        self.minute_hand = self.canvas.create_line(self.center_x, self.center_y, self.center_x, self.center_y, width=2)
        self.second_hand = self.canvas.create_line(self.center_x, self.center_y, self.center_x, self.center_y, fill="blue")

    def update_time(self):
        current_time = time.localtime()
        hours = current_time.tm_hour % 12
        minutes = current_time.tm_min
        seconds = current_time.tm_sec

        hour_angle = math.radians(90 - (hours * 30 + (minutes / 60) * 30))
        minute_angle = math.radians(90 - (minutes * 6 + (seconds / 60) * 6))
        second_angle = math.radians(90 - (seconds * 6))

        self.canvas.coords(self.hour_hand, self.center_x, self.center_y,
                           self.center_x + self.radius * 0.4 * math.cos(hour_angle),
                           self.center_y - self.radius * 0.4 * math.sin(hour_angle))
        
        self.canvas.coords(self.minute_hand, self.center_x, self.center_y,
                           self.center_x + self.radius * 0.7 * math.cos(minute_angle),
                           self.center_y - self.radius * 0.7 * math.sin(minute_angle))
        
        self.canvas.coords(self.second_hand, self.center_x, self.center_y,
                           self.center_x + self.radius * 0.7 * math.cos(second_angle),
                           self.center_y - self.radius * 0.7 * math.sin(second_angle))
        
        self.root.after(1000, self.update_time)

root = tk.Tk()
analog_clock = AnalogClock(root)
root.mainloop()
