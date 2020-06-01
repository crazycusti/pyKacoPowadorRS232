# pyKacoPowadorRS232 0.1

## Dependencies
- Python3.4 or higher
- pySerial
- python-InfluxDB
- a serial connection!

## Debian/Ubuntu
```shell
apt-get install python3 python3-influxdb python3-serial
```



## Configuration
Set host, port, username, password, database, serialPort, measurement and fields to your system configuration.

## systemd unit file
install the .service file in your [preferred] (https://www.freedesktop.org/software/systemd/man/systemd.unit.html#User%20Unit%20Search%20Path) systemd unit folder.

copy the main.py to /usr/local/pykacopowadorrs232/ 


## Kaco Powador Inverter

the RS232 port of the Kaco Powador from 2000xi to 3600xi, use a csv-style output every 10 seconds.
Other Kaco inverter like the bigger ones are not supported because they use the RS485 Protocol which is slightly different.
