# CAN Frame Decoder

This script is a simple tool for decoding CAN (Controller Area Network) frames using
the `can-decoder` library. It takes a CAN frame as input and outputs the decoded frame
as a Python dictionary with the following structure:
```
{
    "ID": <frame_id>,
    "Data": <data_bytes>,
    "Flags": {
        "RTR": <is_remote_transmission_request>,
        "IDE": <is_extended_frame>
    }
}
```
Here's a brief description of each field in the output dictionary:

* `ID`: The CAN frame ID, which is a unique identifier for the message.
* `Data`: The data bytes that make up the message.
* `Flags`: A dictionary containing flags related to the frame. These include:
        + `RTR`: Whether the frame is a remote transmission request (i.e., whether it's a re

request to send a message from another node).
        + `IDE`: Whether the frame is an extended frame (i.e., whether it has an ID greater

than 11 bits).

This script assumes that the CAN frames being decoded are using the J1939 protocol,
which is used for vehicle networking in North America. If your CAN frames are using a
different protocol, you may need to modify this script accordingly.

To use this script, simply provide it with a CAN frame as input and it will output the
decoded frame. For example:
```
python can_decoder.py -i <can_frame>
```
This script is based on the `can-decoder` library, which provides a simple way to
decode CAN frames using the CAN format. If you need more advanced features or support
for different protocols, you may want to consider using a more comprehensive CAN
decoding library instead.
