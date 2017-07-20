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

nom_mate_1=raw_input("ingrese materia: ")

nota_1=int(input("ingrese nota: "))

nota_2=int(input("ingrese nota: "))

nota_3=int(input("ingrese nota: "))

nom_mate_2=raw_input("ingrese materia: ")

nota_4=int(input("ingrese nota: "))

nota_5=int(input("ingrese nota: "))

nota_6=int(input("ingrese nota: "))

nom_mate_3=raw_input("ingrese materia: ")

nota_7=int(input("ingrese nota: "))

nota_8=int(input("ingrese nota: "))

nota_9=int(input("ingrese nota: "))

nom_mate_4=raw_input("ingrese materia: ")

nota_10=int(input("ingrese nota: "))

nota_11=int(input("ingrese nota: "))

nota_12=int(input("ingrese nota: "))

nom_mate_5=raw_input("ingrese materia: ")

nota_13=int(input("ingrese nota: "))

nota_14=int(input("ingrese nota: "))

nota_15=int(input("ingrese nota: "))

mate_1 = {"nombre" : nom_mate_1, "aprobado" : "aprobado", "nota" : nota_1, "nombre1" : nom_mate_1, "aprobado1" : "aprobado" , "nota1" : nota_2, "nombre2" : nom_mate_1, "aprobado2" :"aprobado" , "nota2" : nota_3}

mate_2 = {"nombre" : nom_mate_2, "aprobado" : "aprobado", "nota" : nota_4, "nombre1" : nom_mate_2, "aprobado1" : "aprobado" , "nota1" : nota_5, "nombre2" : nom_mate_2, "aprobado2" :"aprobado" ,"nota2" : nota_6}

mate_3 = {"nombre" : nom_mate_3, "aprobado" : "aprobado", "nota" : nota_7, "nombre1" : nom_mate_3, "aprobado1" : "aprobado" , "nota1" : nota_8, "nombre2" : nom_mate_3, "aprobado2" : "aprobado" ,"nota2" : nota_9}

mate_4 = {"nombre" : nom_mate_4, "aprobado" : "aprobado", "nota" : nota_10, "nombre1" : nom_mate_4, "aprobado1" : "aprobado" , "nota1" : nota_11, "nombre2" : nom_mate_4, "aprobado2" :"aprobado" ,"nota2" : nota_12}

mate_5 = {"nombre" : nom_mate_5, "aprobado" : "aprobado", "nota" : nota_13, "nombre1" : nom_mate_5, "aprobado1" : "aprobado" , "nota1" : nota_14, "nombre2" : nom_mate_5, "aprobado2" :"aprobado" ,"nota2" : nota_15}

materia_aprobada=[mate_1, mate_2, mate_3, mate_4, mate_5]

print materia_aprobada

print alumno

