import tkinter as tk
from tkinter import Scale
from pyfirmata import Arduino, util
import time

class ArduinoGUI:
    def __init__(self, master):
        self.master = master
        master.title("Arduino LED PWM Control")

        # Connect to Arduino
        # Adjust your Arduino connection port accordingly
        self.board = Arduino('/dev/ttyACM0')

        # Use pin 9 for PWM (adjust pin number as needed)
        self.led_pin = self.board.get_pin('d:9:p')  # d for digital, 9 for pin, p for PWM

        # Create a slider for PWM control
        self.slider = Scale(master, from_=0, to=100, orient=tk.HORIZONTAL, command=self.update_pwm)
        self.slider.pack()

        # Set initial slider value
        self.slider.set(0)

        # Initialize flashing variables
        self.flashing = False
        self.flash_interval = 500  # milliseconds
        self.flash_timer = None

    def update_pwm(self, duty_cycle):
        # Convert duty cycle from slider (0-100) to PWM (0-1)
        pwm_value = float(duty_cycle) / 100.0
        self.led_pin.write(pwm_value)
        
        # If duty cycle is 100%, set the LED fully on
        if pwm_value == 1.0:
            self.led_pin.write(1.0)

        # Update flashing interval based on duty cycle
        # Range from 100 ms (fastest) to 1000 ms (slowest)
        self.flash_interval = int(1000 - (int(duty_cycle) * 9))

    def start_flash(self):
        if not self.flashing:
            self.flashing = True
            self.flash_timer = self.master.after(self.flash_interval, self.toggle_flash)

    def stop_flash(self):
        if self.flashing:
            self.flashing = False
            if self.flash_timer is not None:
                self.master.after_cancel(self.flash_timer)
                self.flash_timer = None

    def toggle_flash(self):
        if self.flashing:
            # Toggle LED state
            self.led_pin.write(1 if self.led_pin.read() == 0 else 0)
            # Schedule next flash
            self.flash_timer = self.master.after(self.flash_interval, self.toggle_flash)

    def close(self):
        self.stop_flash()  # Stop flashing before closing
        self.board.exit()
        self.master.destroy()

# Create the GUI window
root = tk.Tk()
root.title("Arduino LED PWM Control")
root.geometry("400x200")  # Set window size to 400x200

app = ArduinoGUI(root)

# Button to start/stop flashing
flash_button = tk.Button(root, text="Start Flash", command=app.start_flash)
flash_button.pack()

# Ensure the application cleans up properly upon exit
root.protocol("WM_DELETE_WINDOW", app.close)

# Run the application
root.mainloop()
