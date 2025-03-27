import tkinter as tk
from pyfirmata import Arduino, util

class ArduinoGUI:
    def __init__(self, master):
        self.master = master
        master.title("Arduino LED Control")

        # 連接 Arduino，請修改對應的 COM 埠
        self.board = Arduino('/dev/ttyUSB0')  # Linux: /dev/ttyUSB0 或 /dev/ttyACM0
        # self.board = Arduino('COM3')  # Windows 用戶請改成對應的 COM3, COM4, ...

        self.led_pin = self.board.get_pin('d:13:o')  # d: digital, 13: pin number, o: output

        # 建立按鈕來控制 LED
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

    def close(self):
        self.board.exit()
        self.master.destroy()

# 啟動 GUI
root = tk.Tk()
app = ArduinoGUI(root)

# 關閉時確保 Arduino 連線正常退出
root.protocol("WM_DELETE_WINDOW", app.close)

# 運行 GUI
root.mainloop()

