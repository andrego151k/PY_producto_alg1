calificacion1 = float(input("Ingrese la calificación 1: "))
calificacion2 = float(input("Ingrese la calificación 2: "))
calificacion3 = float(input("Ingrese la calificación 3: "))
calificacion4 = float(input("Ingrese la calificación 4: "))
calificacion5 = float(input("Ingrese la calificación 5: "))

promedio = (calificacion1 + calificacion2 + calificacion3 + calificacion4 + calificacion5) / 5

if promedio >= 5:
    estado = "APRUEBA"
else:
    estado = "REPRUEBA"

print(f"El alumno {estado} el curso con un promedio de {promedio:.1f}")
