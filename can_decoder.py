import serial
from can import Decoder
import logging

# Set up logging
logging.basicConfig(filename='can_decoder.log', level=logging.DEBUG)

# Open the UART port and set up the decoder
interface = serial.Serial('/dev/ttyUSB0', 115200, timeout=None)
decoder = Decoder(interface)

# Read a CAN frame from the UART port
frame = interface.read_frame()

# Decode the frame using the decoder
decoded_frame = decoder.decode(frame)

# Log the decoded frame to the console and file
logging.info('Decoded frame: %s', decoded_frame)
