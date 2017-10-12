#!/usr/bin/python

lee=[15, 25, 30, 45, 55, 54, 60, 78, 9,10]

def bus_lin_while(a,lee):

    pos=-1

    j=0

    salir=False

    while j<len(lee) and not salir:

        if a==lee[j]:

            pos=j

            salir=True

        j+=1

    return pos

print bus_lin_while(45,lee)