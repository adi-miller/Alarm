from time import sleep
import serial
import datetime 

channel = serial.Serial(port="/dev/serial0",
                              stopbits=serial.STOPBITS_ONE,
                              baudrate=2400,
                              bytesize=serial.EIGHTBITS,
                              parity=serial.PARITY_NONE)

print(channel.name)
while (True):
  avail = channel.in_waiting
  if (avail != 0):
    print("-- " + str(avail) + " - " + str(datetime.datetime.now()))
    while (channel.in_waiting > 0):
      data = channel.read(1)
      print("x" + data.hex() + "-" + str(ord(data)), end=' ')
    print()
    print()
  else:
    print(".", end='')

  sleep(0.01)
