print("Bienvenido a su calculadora de propinas!")

subtotal = float(input("Ingrese valor de la cuenta:$"))
Porcent = float(input("ingrese valor de porcentaje:%"))
valorporcentaje = (subtotal * Porcent) / 100
print("calculo del porcentaje:$" , valorporcentaje)
total1 = subtotal + valorporcentaje
print("valor total:$" , total1)
propina = float(input("Ingrese el valor de la propina:$"))
total2 = float((total1 + propina))
print("Valor total final:$" , total2)
Personas = int(input("Ingrese cantidad de comensales:"))
Valorporpersona = float((total2/Personas))
print("Valor a cancelar por persona:$" , round(Valorporpersona,2))

print("Gracias por preferirnos. !Vuelva pronto!")



