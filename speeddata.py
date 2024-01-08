import serial
import time
import pandas as pd

ser = serial.Serial('/dev/tty.usbserial-10', 9600)

time.sleep(3)

new_speeds = []

for i in range(100):
    if ser.in_waiting:
        line = ser.readline().decode('utf-8').strip()
        speed = line.split(': ')[1]
        new_speeds.append(float(speed))


    while len(new_speeds) < i + 1:
        new_speeds.append(None)

df = pd.read_csv('speeds.csv')

df['21摄氏度'] = new_speeds

df.to_csv('speeds.csv', index=False)

ser.close()
