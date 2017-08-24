#!/usr/bin/python

leia=raw_input("ingrese palabra: ")

def inversa(leia):
    nue = " "

    if len(leia)> 1:

        for l in leia:
            nue+=l
            return nue

    else:
         return leia

print inversa(leia)
