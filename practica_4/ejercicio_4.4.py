#!/usr/bin/python

P= raw_input("ingrese caracter: ")

def caracter(P):

	if ((P=="a") or (P=="e") or (P=="i") or (P=="o") or (P=="u")):

		return True

	else:
		return "false"

caracter (P)
print (caracter(P))
