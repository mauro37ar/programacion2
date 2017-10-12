#!/usr/bin/python

teemo=range(0,100)

def bus_lin_while(a, teemo):

    pos=-1

    salir=False

    j=0

    while j<len(teemo) and not salir:

        if a==teemo[j]:

            pos=j

            salir=True

        j+=1

    return pos

print bus_lin_while(30,teemo)

