import serial
import serial.tools.list_ports
import time

ser = serial.Serial(port ="COM6", baudrate = 9600)
ports = serial.tools.list_ports.comports()

#serial func returns entries to call line
def serialfunc():
    while True:
        value = ser.readline()
        try:
            yield float(value.decode('utf-8').strip())
        except:
            pass
