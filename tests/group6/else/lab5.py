import serial
import time
# 設定 Serial 連接
arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=1)
time.sleep(2)
def send_command(command):
    # """ 傳送 ON / OFF 指令給 Arduino """
    arduino.write(f"{command}\n".encode()) # 傳送指令
    print(f"發送: {command}")
def read_data():
# """ 讀取 Arduino 回傳的 LED 狀態與按鈕狀態 """
    while arduino.in_waiting:
        response = arduino.readline().decode().strip()
        if response:
            print(f"Arduino 回應: {response}")
# 主循環
try:
    while True:
        command = input("輸入 '1' 或 '0': ")
        send_command(command)
        time.sleep(1.5)
        read_data()
except KeyboardInterrupt:
        print("\n 程式結束")
finally:
        arduino.close()