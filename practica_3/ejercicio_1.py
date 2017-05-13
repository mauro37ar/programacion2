#!/usr/bin/python

p1= raw_input("ingrese palabra:  ")

p2= raw_input ("ingrese palabra: ")

if (p1[-3: ] == p2[-3: ]):

	print "las palabras riman" 

elif (p1 [-2:] == p2[-2:]):

	print "las palabras riman poco"

else:
	print "las palabras no riman"

print "fin del ejercicio 1"
