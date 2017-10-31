#!/usr/bin/python

import math
num = input("Ingrese un numero entero ")
if(num > 0):
    cad = ""
    while(num > 0):
        if(num%2 == 0):
            cad = "0" + cad
        else:
            cad = "1" + cad
        num = math.floor(num/2)
    print cad      
else:
    if(num == 0):
        print("0")
    else:
        print("Solo numeros mayores a cero")