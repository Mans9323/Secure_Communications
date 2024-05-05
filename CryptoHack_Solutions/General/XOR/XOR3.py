hex_string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
hex_data = bytes.fromhex(hex_string)

for i in range(256):  # for every possible byte 0-255
    result = ''.join(chr(b ^ i) for b in hex_data)
    if all(32 <= ord(c) < 127 or c == '\n' for c in result):  # if all characters are printable
        print(f"Key: {i}, Result: {result}")