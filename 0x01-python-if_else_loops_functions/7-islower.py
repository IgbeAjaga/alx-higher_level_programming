#!/usr/bin/python3
def islower(c):
    # Check if the ASCII code of c is between 97 and 122 (inclusive)
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
