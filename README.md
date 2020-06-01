# pyKacoPowadorRS232 0.1

# Dependencies
- Python3.4 or higher
- pySerial
- python-InfluxDB
- a serial connection!

only tested under Linux/armv6

# Configuration
Set host, port, username, password, database, serialPort, measurement and fields to your system configuration.

# Kaco Powador Inverter

the RS232 port of the Kaco Powador from 2000xi to 3600xi, use a csv-style output every 10 seconds.
Other Kaco inverter like the bigger ones are not supported because they use the RS485 Protocol which is slightly different.
