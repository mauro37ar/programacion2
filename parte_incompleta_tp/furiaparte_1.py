#!/usr/bin/python
nombre_1=raw_input("ingrese nombre: ")
apellido_1=raw_input("ingrese apellido: ")
dni_1=int(input("ingrese documento: "))
fecha_ingreso_1=int(input("anio de ingreso: "))
nombre_2=raw_input("ingrese nombre: ")
apellido_2=raw_input("ingrese apellido: ")
dni_2=int(input("ingrese documento: "))
fecha_ingreso_2=int(input("anio de ingreso: "))
nombre_3=raw_input("ingrese nombre: ")
apellido_3=raw_input("ingrese apellido: ")
dni_3=int(input("ingrese documento: "))
fecha_ingreso_3=int(input("anio de ingreso: "))
ju = {"nombre":nombre_1, "apellido": apellido_1, "dni": dni_1, "anio de egreso": fecha_ingreso_1, "materias": "ma"} 
pa = {"nombre": nombre_2, "apellido": apellido_2, "dni": dni_2, "anio de egreso": fecha_ingreso_2, "materias": "ma"}
el = {"nombre": nombre_3, "apellido": apellido_3, "dni": dni_3, "anio de egreso": fecha_ingreso_3, "materias": "ma"}
alumno =[ju, pa, el]
print alumno
