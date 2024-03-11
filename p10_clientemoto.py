dia_semana = input("Ingrese el día de la semana (en minúsculas): ")
es_feriado = input("¿Es feriado? (True/False): ").lower() == "true"

if dia_semana == "martes":
    descuento = 0.12
elif dia_semana == "sábado":
    descuento = 0.18
elif es_feriado:
    descuento = 0.25
else:
    descuento = 0

precio_original = float(input("Ingrese el precio original de la moto: "))
precio_a_pagar = precio_original * (1 - descuento)

print(f"Si compra la moto el {dia_semana} pagará: {precio_a_pagar:.2f}")
