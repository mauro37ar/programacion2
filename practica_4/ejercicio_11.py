#!/usr/bin/python

leia=raw_input("ingrese palabra: ")

def palindromo(leia):

    if leia == leia[::-1]:

        han = 1
        
        luke ="La palabra %s es palindromo" % leia

        
    
        return luke + str(han) 
        
    else:
         solo = 0
         
         cage="La palabra %s no es palindromo" % leia

                 
         return cage + str(solo)         


print palindromo(leia)
