import tkinter as tk
from pyfirmata import Arduino, util
import time


class ArduinoGUI:
   def __init__(self, master):
       self.master = master
       master.title("Arduino LED Control")


       # Connect to Arduino
       # Adjust your Arduino connection port accordingly
       #self.board = Arduino('/dev/ttyUSB0') 
       # self.board = Arduino('/dev/ttyUSB1')
       self.board = Arduino('/dev/ttyACM0')
       # self.board = Arduino('/dev/ttyACM1')


       self.led_pin = self.board.get_pin('d:13:o')  # d for digital, 13 for pin, o for output


       # Create a GUI button for toggling the LED
       self.led_state = False
       self.toggle_button = tk.Button(master, text="Turn LED on", command=self.toggle_led)
       self.toggle_button.pack()


   def toggle_led(self):
       self.led_state = not self.led_state
       self.led_pin.write(self.led_state)
       if self.led_state:
           self.toggle_button.config(text="Turn LED off")
       else:
           self.toggle_button.config(text="Turn LED on")

   def brightness_scale(self):  # Add missing "self" parameter
       self.brightness_scale = tk.Scale(self.master, from_=0, to=255, orient=tk.HORIZONTAL, command=self.update_brightness)
       self.brightness_scale.pack()

   def update_brightness(self, brightness):
       self.led_pin.write(int(brightness))

   def close(self):
       self.board.exit()
       self.master.destroy()


# Create the GUI window
root = tk.Tk()
app = ArduinoGUI(root)


# Ensure the application cleans up properly upon exit
root.protocol("WM_DELETE_WINDOW", app.close)


# Run the application
root.mainloop()
