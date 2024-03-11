sueldo = float(input("Ingrese el sueldo del trabajador: "))

#  condicional Calculo del descuento
if sueldo <= 1000:
    descuento = 0.1 * sueldo  # Descuento del 10% en sueldo menor a 1000.
elif sueldo <= 2000:
    descuento = (0.1 * 1000) + (0.05 * (sueldo - 1000))  # 5% adicional hasta 2000.
else:
    descuento = (0.1 * 1000) + (0.05 * 1000) + (0.03 * (sueldo - 2000))
    #  3% del adicional.

# resta sueldo neto descuento en el sueldo original.
sueldo_neto = sueldo - descuento

print(f"Descuento: {descuento}")   # Imprimir el descuento y el sueldo neto
print(f"Sueldo neto: {sueldo_neto}")
