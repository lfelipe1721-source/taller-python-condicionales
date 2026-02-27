#Ejercicio2
#Pedir ujn número enetero
#Mostrar si es par o impar
#Pedir edad
#Mostrar si es mayor o menor de edad

numero = int(input("Ingresa cualquier número entero: "))

if numero % 2 == 0:
	print("El número es par")
else:
	print("El número es impar")


edad = int(input("Escribe tu edad:"))

if edad >= 18:
	print("Eres mayor de edad")
else:
	print("Eres menor de edad")
