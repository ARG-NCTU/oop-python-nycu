import serial
import serial.tools.list_ports
import time

def find_arduino():
    """自動尋找 Arduino 兼容設備"""
    ports = serial.tools.list_ports.comports()
    for port in ports:
        # 檢查 CH340 晶片或常見 Arduino 標識
        if ('1A86:7523' in port.hwid) or ('Arduino' in port.description):
            return port.device
    return None

def main():
    try:
        # 自動檢測或手動指定
        arduino_port = find_arduino() or '/dev/ttyUSB0'
        print(f"嘗試連接 {arduino_port}...")
        
        # 初始化串口連接
        arduino = serial.Serial(port=arduino_port, 
                              baudrate=9600,
                              timeout=1)
        time.sleep(2)  # 等待 Arduino 初始化
        
        print("連接成功！輸入指令控制 LED (ON/OFF/TOGGLE/EXIT):")
        
        while True:
            command = input("> ").upper().strip()
            
            if command == "EXIT":
                break
                
            if command in ["ON", "OFF", "TOGGLE"]:
                arduino.write(f"{command}\n".encode())
                response = arduino.readline().decode().strip()
                print(response)
            else:
                print("無效指令，請輸入 ON/OFF/TOGGLE/EXIT")
                
    except Exception as e:
        print(f"錯誤發生: {str(e)}")
    finally:
        if 'arduino' in locals() and arduino.is_open:
            arduino.close()
        print("程式結束")

if __name__ == "__main__":
    # 顯示所有檢測到的設備
    print("檢測到的串口設備:")
    for port in serial.tools.list_ports.comports():
        print(f"- {port.device}: {port.description} (HWID: {port.hwid})")
    
    main()