#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i+1, 10):
        if i == 0:
            print("{:02d}".format(j), end=", ")
        else:
            print("{:d}{:d}".format(i, j), end=", ")
