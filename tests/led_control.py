import serial
import time

# 設定 Serial 連接
arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1)
time.sleep(2)

def send_command(command):
    """ 傳送 ON / OFF 指令給 Arduino """
    arduino.write(f"{command}\n".encode())
    print(f"發送: {command}")

def read_data():
    """ 讀取 Arduino 回傳的 LED 狀態與按鈕狀態 """
    while arduino.in_waiting:
        response = arduino.readline().decode().strip()
        if response:
            print(f"Arduino 回應: {response}")

try:
    while True:
        user_input = input("請輸入 ON / OFF（或 Q 結束）: ").strip().upper()
        if user_input == "Q":
            break
        elif user_input in ("ON", "OFF"):
            send_command(user_input)
            read_data()
        time.sleep(1)

except KeyboardInterrupt:
    print("\n程式結束")
finally:
    arduino.close()
