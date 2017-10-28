#!/usr/bin/python

teemo=range(0,100)

print teemo

def bus_lin_bin(a, teemo):

    menor=0

    mayor=len(teemo)-1

    salir=False

    pos=-1

    while (menor<=mayor) and not salir:

        mitad=(menor+mayor)/2

        print mitad
        
        if teemo[mitad]==a:

            pos=mitad

            salir=True
        
        elif teemo[mitad]<a:

            menor=mitad+1

        elif teemo[mitad]>a:

            mayor=mitad+1

            return pos

print bus_lin_bin(45,teemo)