#!/usr/bin/python

tsukino=[10, 20, 30, 40, 50, 60,  70, 80, 90, 100]

def bus_lin_bin_recursiva(a, tsukino):

    menor=0

    mayor=len(tsukino)-1

    mitad=(menor+mayor)/2

    if tsukino==[]:
        
        return -1
    
    elif tsukino[mitad]==a:

        return mitad

    elif tsukino[mitad]>a:

        soraka= bus_lin_bin_recursiva(a,tsukino[0:mitad])

        return soraka

    elif tsukino[mitad]<a:

        soraka=bus_lin_bin_recursiva(a, tsukino[mitad+1:mayor+1])

        if (soraka==-1):

            return -1

        return soraka + mitad + 1

    return -1

print bus_lin_bin_recursiva(70, tsukino)  

            



