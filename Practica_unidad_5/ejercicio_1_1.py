#!/usr/bin/python

SAkura=[25, 10, 45, 35, 55, 5]

def busq_lineal(a, SAkura):

    pos=-1

    for j in range(0,len(SAkura)):

        if a==SAkura[j]:

            pos=j

            return pos

print busq_lineal(5,SAkura)