#!/usr/bin/python3
import sys

args = sys.argv[1:] # get all arguments, excluding the first one (the script name)
total = sum(int(arg) for arg in args) # sum all arguments, casting each one to int

print(total) # print the result
