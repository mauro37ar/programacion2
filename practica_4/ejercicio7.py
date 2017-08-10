#!/usr/bin/python

leia=raw_input("ingrese palabra: ")

def inversa(leia):
    if len(leia)==1:
        return leia

    else:
        return leia[-1]+inversa(leia[:-1])

print inversa(leia)
