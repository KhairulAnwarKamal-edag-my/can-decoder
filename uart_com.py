import serial
import time

class UartCommunication:
  def __init__(self, com_port):
    self.com_port = com_port # Set the COM port
    self.serial = None       # Create a variable to store the Serial object
    self.baud_rate = 9600    # default baudrate

def open(self):
  """Open the com port and set up the com port parameters"""
  self.serial = serial.Serial(self.com_port, self.baud_rate)
  time.sleep(1) # Delay before trying to communicate over the serial port

def close(self):
  """Close the serial port and clean up any resources"""
  if self.serial:
    self.serial.close()
    self.serial = None

def send(self, data):
  """Send data over the UART connection"""
  self.serial.write(data.endcode())

def receive(self, num_bytes=1024):
  """Receive data from the UART connection"""
  return self.serial.read(num_bytes)
  
