#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    argc = len(argv)

    print(argc, "argument" if argc == 1 else "arguments" + (":" if argc > 0 else "."))
    for i, arg in enumerate(argv, start=1):
        print(i, ":", arg)
