#!/usr/bin/python

luke=[1,25,35,40,"soquete","perro", "ortencia"]

cage=[20, 40, 60, "sotreta", "ahijuna"]

def superposicion(luke,cage):

    for j in luke:

        for o in cage:

            if j==o:

                return True

            else:

                return False

superposicion(luke,cage)

print (superposicion(luke,cage))