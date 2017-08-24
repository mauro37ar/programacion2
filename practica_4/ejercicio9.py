#!/usr/bin/python

n = input("ingrese numero(de 0 a 9): ")
anakin = raw_input("ingrese caracter: ")
def generar_n_caracteres (n, anakin):
       
    if anakin !=0 and n<10:

       luke = anakin*n

       return luke

    else:

      return "jodido"

print generar_n_caracteres(n,anakin)

