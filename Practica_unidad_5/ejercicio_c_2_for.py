#!/usr/bin/python

teemo=range(0,100)

a= 25

def bus_lin_for(a, teemo):

    pos = -1

    for j in range(0,len(teemo)):
 
        if a==teemo[j]:

            pos=j

    return pos

print bus_lin_for(a, teemo)