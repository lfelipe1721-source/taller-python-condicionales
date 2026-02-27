#Ejercicio 4 -tarifa de taxi

distancia = float(input("Distancia en km:"))
hora = int(input("Hora del viaje (0-23):"))

tarifa_base = 1

if 6 <= hora <= 19:
	costo_km = 0.50
	horario = "día"
else:
	costo_km = 0.65
	horario = "noche"
total = tarifa_base + (distancia * costo_km)

if distancia > 10:
	total += 2

print (f"Tu horario es de: {horario}")
print (f"La distancia es: {distancia} km")
print (f"Total a pagar: ${total}")


