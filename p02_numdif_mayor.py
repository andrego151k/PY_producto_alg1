num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 != num2 and num1 != num3 and num2 != num3:
    mayor = max(num1, num2, num3)
    print(f"El número mayor es: {mayor}")
else:
    print("Por favor, asegúrese de ingresar tres valores distintos.")
