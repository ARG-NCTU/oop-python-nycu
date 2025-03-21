import tkinter as tk
from pyfirmata import Arduino, util

# 初始化 Arduino 板和 LED 引腳
board = Arduino('/dev/ttyUSB0')
led_pin = board.get_pin('d:13:o')

# 啟動板的迭代器
it = util.Iterator(board)
it.start()

# 初始化 Tkinter 根窗口
root = tk.Tk()
root.title("LED Control")

# 狀態標籤
status_label = tk.Label(root, text="LED OFF", font=('Helvetica', 16))
status_label.pack(pady=20)

# 當前 LED 狀態標籤
current_status_label = tk.Label(root, text="Current LED Status: OFF", font=('Helvetica', 16))
current_status_label.pack(pady=20)

# LED 狀態變量
ledstatus = 0

# 打開 LED 的函數
def turn_on_led():
    led_pin.write(1)
    status_label.config(text="LED ON")
    print("LED ON")

# 關閉 LED 的函數
def turn_off_led():
    led_pin.write(0)
    status_label.config(text="LED OFF")
    print("LED OFF")

# 更新當前 LED 狀態標籤的函數
def update_status_label():
    if ledstatus == 0:
        current_status_label.config(text="Current LED Status: OFF")
    else:
        current_status_label.config(text="Current LED Status: ON")

# 切換 LED 狀態的函數
def switch():
    global ledstatus
    if ledstatus == 0:
        turn_on_led()
        ledstatus = 1
        mybutton.config(text='turn off')
    else:
        turn_off_led()
        ledstatus = 0
        mybutton.config(text='turn on')
    update_status_label()

# 按鈕
mybutton = tk.Button(root, text='turn on', font=('Arial', 30, 'bold'), command=switch)
mybutton.pack()

# 啟動 Tkinter 主循環
root.mainloop()