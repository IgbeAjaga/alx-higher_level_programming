#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        output = fct(*args)
        return output
    except Exception as err:
        print("Exception:", err, file=sys.stderr)
        return (None)
