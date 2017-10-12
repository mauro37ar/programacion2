#!/usr/bin/python

tsukino=[10, 20, 30, 40, 50, 60,  70, 80, 90, 100]

def bus_binaria(a,tsukino):

    menor=0

    mayor=len(tsukino)-1

    salir=False

    pos=-1

    while (menor<=mayor) and not salir:

        mitad=(menor+mayor)/2

        if tsukino[mitad]==a:

            pos=mitad

            salir=True
        
        elif tsukino[mitad]<a:

            menor=mitad+1

        elif tsukino[mitad]>a:

            mayor=mitad+1

        return pos

print bus_binaria(50, tsukino)