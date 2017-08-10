#!/usr/bin/python


lista={1,2,3,4}

suma=0

def sumarlista(lista):

	for i in lista:

		if sorted(lista)==lista:

			return True
	
		else:	
			
			return  False
print sumarlista(lista)
