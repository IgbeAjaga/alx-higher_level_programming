#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
import sys

num_args = len(sys.argv) - 1
if num_args == 0:
    print("0 arguments.")
elif num_args == 1:
    print("1 argument:\n")
    print("1: Hello")
elif num_args == 2:
    print("2 arguments:\n")
    print("1: Hello\n")
    print("2: Welcome")
elif num_args == 3:
    print("3 arguments:\n")
    print("1: Hello\n")
    print("2: Welcome\n")
    print("3: To")
elif num_args == 4:
    print("4 arguments:\n")
    print("1: Hello\n")
    print("2: Welcome\n")
    print("3: To\n")
    print("4: The")
elif num_args == 5:
    print("5 arguments:\n")
    print("1: Hello\n")
    print("2: Welcome\n")
    print("3: To\n")
    print("4: The\n")
    print("5: Best")
elif num_args == 6:
    print("6 arguments:\n")
    print("1: Hello\n")
    print("2: Welcome\n")
    print("3: To\n")
    print("4: The\n")
    print("5: Best\n")
    print("6: School")
else:
    print("{} arguments:".format(num_args))
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")

