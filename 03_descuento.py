#Ejercicio3
#Descuento tienda

#Pedir:
#subtotal (float)  
#tipo_cliente (vip o regular)
#Si es vip:
#15% de descuento.

#Si es regular:
#5% solo si subtotal >= 100  
#si no, no hay descuento.

#Mostrar:
#subtotal  
#descuento aplicado  
#total final

subtotal = float(input("¿Cuál es tu subtotal?:"))
tipo_de_cliente = input("¿Qué tipo de cliente eres?(vip o regular):")

descuento = 0

if tipo_de_cliente == "vip":
	descuento = subtotal * 0.15
elif tipo_de_cliente == "regular":
	if subtotal >= 100:
		descuento = subtotal * 0.05

total = subtotal - descuento
print (f"subtotal: ${subtotal}")
print (f"Descuento aplicado: ${descuento}")
print (f"Total final: ${total}")
  
