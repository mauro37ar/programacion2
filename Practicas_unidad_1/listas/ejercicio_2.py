#!/usr/bin/python

Personas  ={}
p1=raw_input ("ingrese su nombre: ")
p2=raw_input ("ingrese su apellido: ")
p3=input ("ingrese su dni: ")
p4=input("anio de nacimiento: ")
p5=raw_input ("ingrese su lugar de nacimiento: ")
clave_personal=(p3*p4)
personas=[p1, p2, p3, p4, p5, clave_personal]
 

print (personas)
