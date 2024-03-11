marca = input("Ingrese la marca de la motocicleta: ")
precio_moto = float(input("Ingrese el precio de la moto: "))

if marca == "Honda":
    descuento = 0.05 * precio_moto
elif marca == "Yamaha":
    descuento = 0.08 * precio_moto
elif marca == "Suzuki":
    descuento = 0.10 * precio_moto
else:
    descuento = 0.02 * precio_moto

precio_a_pagar = precio_moto - descuento

print(f"Precio de la moto: {precio_moto}")
print(f"Descuento: {descuento}")
print(f"Precio a pagar: {precio_a_pagar}")
