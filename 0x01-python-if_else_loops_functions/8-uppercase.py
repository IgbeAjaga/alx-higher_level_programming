#!/usr/bin/python3
def uppercase(s):
    for c in s:
        ascii_code = ord(c)
        if 97 <= ascii_code <= 122:  # Check if character is lowercase
            ascii_code -= 32  # Convert to uppercase
        print(chr(ascii_code), end="")
    print()
