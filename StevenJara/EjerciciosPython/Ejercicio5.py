"""
	@autor: stevejr23
 	nombre: ejercicio5.py
  	descripción: ...
""" 
# System.ou.println("Ingrese su nombre")
# nombre = entrada.nextLine()

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: \n")
nota1 = input("Ingrese el valor de nota 1: ")
nota2 = input("Ingrese el valor de nota 2: ")

suma = int(nota1) + int(nota2);
print("%s -- %s\nSu suma de notas es %s" %
	(nombre, edad, suma))
