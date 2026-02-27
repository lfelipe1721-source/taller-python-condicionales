#Ejercicio5
#Clasificador de notas

n1 = float(input("nota 1:"))
n2 = float(input("nota 2:"))
n3 = float(input("nota 3:"))

if not (0 <= n1 <= 100 and 0 <= n2 <= 100 and 0 <= n3 <= 100):
	print ("Error: nota inválida")
else:
	promedio = (n1+n2+n3)/3
	if promedio >= 90:
		clasificación = "excelente"
	elif promedio >= 80:
		clasificación = "muy bueno"
	elif promedio >= 70:
		clasificación = "bueno"
	elif promedio >= 60
		clasificación = "supletorio"
	else:
		clasificación = "reprobado"
	
	print(f"Notas: {n1}, {n2}, {n3}")
	print(f"El promedio es: {promedio}")
	print(f"Clasificación final: {clasificación}")
