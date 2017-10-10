#!/usr/bin/python

cage=[31, 55, 46, 67, 14, 9, 3, 10]

def busq_linea_while(a, cage):

    pos=-1

    j=0

    salir=False

    while j<len(cage) and not salir:

        if a==cage[j]:

            pos=j

            salir=True

        j+=1

    return pos

print busq_linea_while(3, cage)        