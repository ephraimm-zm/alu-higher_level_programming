#!/usr/bin/python3
for i in range(0, 100):
    if i < 10:
        print("0{i}".format(i=i), end=', ')
    else:
        print("{i}".format(i=i), end=', ' if i != 99 else '\n')
