##!/usr/bin/python3

# pyKacoPowadorRS232 v0.1

# some code pieces borrowed from https://struband.net/
# thanks to the people from winhistory-forum

import serial, sys, time, json, csv
from influxdb import InfluxDBClient

# Configuration
serialPort='/dev/ttyUSB0'
db = InfluxDBClient(host='*', port=8086, username='*', password='*', database='*')

try:
    ser = serial.Serial(serialPort,baudrate=9600,timeout=15,rtscts=True)
except:
    print("cannot open the serialport")
    sys.exit(1)

while True:
    try:
        while True:
                   serData = ser.readline().decode("utf8").strip()
                   if serData and (not serData.isspace()):
                        rd = serData.split()
                        if len(rd) >5:
                         ener = int(rd[5])
                         json_body = [
                                         {
                                           "measurement": "defaultpowador",
                                                "fields": {"energy": ener}
                                         }
                                     ]
                         try:
                             print("Write points: {0}".format(json_body))
                             db.write_points(json_body)
                             print("send data ok.")
                         except:
                                pass
                                print("error send data")
    except serial.SerialException as e:
        try:
            ser.close()
            time.sleep(1)
            ser = serial.Serial(serialPort,baudrate=9600,timeout=15,rtscts=True)
        except:
            pass
