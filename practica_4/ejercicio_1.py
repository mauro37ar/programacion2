#!/usr/bin/python

p=int(input("ingrese numero: "))

l=int(input("ingrese numero: "))


def maxima(p,l):

		if p>l:

			return (p)
		
		elif p<l:

			return (l)
		
		else:

			return (p,l)

maxima(p,l)

print (maxima(p,l))
