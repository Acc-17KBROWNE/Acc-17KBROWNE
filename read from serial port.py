import serial

serialport = serial.Serial(port = "COM7" , baudrate=115200,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)


serialString = ""

while(1):
    if (serialport.in_waiting > 0):
        serialString = serialPort.readline()
        print(serialString.decode("Ascii"))