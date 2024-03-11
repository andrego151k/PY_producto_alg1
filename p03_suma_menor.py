print("poner 3 numeros diferentes "
      "\nimprimir el menor y la suma de los 3.")

Numero1 = int(input("ingrese primer numero: "))
Numero2 = int(input("ingrese el segundo: "))
Numero3 = int(input("ingrese el tercero: "))

if Numero1 < Numero2 and Numero1 < Numero3:  # el menor
    print(f"El {Numero1} es el menor")
elif Numero2 < Numero1 and Numero2 < Numero3:
    print(f"El {Numero2} es el menor")
elif Numero3 < Numero1 and Numero3 < Numero2:
    print(f"El {Numero3} es el menor")
elif Numero1 == Numero2 or Numero1 == Numero3 or Numero2 == Numero3:
    print("\n hay numeros iguales")

print(f' la suma de los numeros es {Numero1 + Numero2 + Numero3}')  # la suma
