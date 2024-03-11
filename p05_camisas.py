camisas = int(input("Ingrese la cantidad de camisas compradas: "))
precio_unitario = float(input("Ingrese el precio unitario de cada camisa: "))

factura = camisas * precio_unitario    # Total sin descuento

if camisas >= 3:
    descuento = 0.2 * factura  # Descuento del 20%
else:
    descuento = 0.1 * factura

total_a_pagar = factura - descuento

print(f"El total a pagar es: {total_a_pagar}")