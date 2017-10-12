#!/usr/bin/python

lee=[15, 25, 30, 45, 55, 54, 60, 78, 9,10]

def bus_linLfor(a, lee):

    pos=-1

    for j in range (0, len(lee)):

        if a==lee[j]:

            pos=j

        return pos

print bus_linLfor(43,lee)   