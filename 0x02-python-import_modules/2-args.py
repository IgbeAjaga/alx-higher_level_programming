#!/usr/bin/python3
import sys

num_args = len(sys.argv) - 1
if num_args == 0:
    print("Number of arguments: 0.")
    print(".")
else:
    if num_args == 1:
        print("Number of argument: 1.")
    else:
        print(f"Number of arguments: {num_args}.")
    print(":")
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")
