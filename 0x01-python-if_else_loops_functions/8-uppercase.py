#!/usr/bin/python3
def uppercase(str):
    for c in str:
        ascii_code = ord(c)
        if 97 <= ascii_code <= 122:  # Check if character is lowercase
            c = chr(ascii_code - 32)  # Convert to uppercase
        print("{}".format(c), end="")
    print("")
