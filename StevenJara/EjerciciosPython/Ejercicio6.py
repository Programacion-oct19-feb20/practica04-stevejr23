"""
	@autor: stevejr23
 	nombre: ejercicio6.py
  	descripción: ...

  	Steven Jara -- 18
  	Su suma de notas es: 30
  	Su promedio es: 15

""" 
 
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: \n")
nota1 = input("Ingrese el valor de nota 1: ")
nota2 = input("Ingrese el valor de nota 2: ")

suma = int(nota1) + int(nota2);
promedio = int(suma)/2

print("%s -- %s\nSu suma es %s\nSu promedio es%s" %
	(nombre, edad, suma, promedio))
