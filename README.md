# CAN Frame Decoder for UART

This script is a simple tool for decoding CAN (Controller Area Network) frames using
the `can-decoder` library, specifically designed to work with CAN frames captured via
a UART port. It takes a CAN frame as input and outputs the decoded frame as a Python
dictionary with the following structure:
```
{
  "id": <frame ID>,
  "data": <data bytes>,
  "flags": {
    "rtr": <is remote transmission request>,
    "ide": <is extended frame>
  }
}
```
Here's a brief description of each field in the output dictionary:

* `id`: The CAN frame ID, which is a unique identifier for the message.
* `data`: The data bytes that make up the message.
* `flags`: A dictionary containing flags related to the frame. These include:
        + `rtr`: Whether the frame is a remote transmission request.
        + `ide`: Whether the frame is an extended frame.

To use this script, simply copy and paste the CAN frame data into the script as input,
and it will output the decoded frame in the format described above. For example:
```
# Example usage

# Connect to the UART port
uart = serial.Serial('/dev/ttyUSB0', 115200)

# Read a CAN frame from the UART port
frame_data = uart.read(8)

# Decode the CAN frame using the script
decoded_frame = decode_can_frame(frame_data)

print(decoded_frame)
```
This code will connect to a UART port at `/dev/ttyUSB0` (replace with the appropriate
path for your system), read an 8-byte CAN frame from the port, and then decode it
using the `decode_can_frame()` function. The decoded frame will be printed to the
console in the format described above.

The script also logs the decoded frame to a file called `can_decoder.log` in the
current working directory, with the log level set to `DEBUG`. This allows you to
review the decoded frames and verify that they are being properly decoded by the
script.
