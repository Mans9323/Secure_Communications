import binascii
import base64

hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
bytes_from_hex = binascii.unhexlify(hex_string)
base64_string = base64.b64encode(bytes_from_hex)
print(base64_string)