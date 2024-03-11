Horast = int(input("ingrese total de horas trabajadas: "))
Horasext = int(input("ingrese horas extras trabajadas si tiene: "))
Valor_hora = 10
bono_hextra = 5

if Horast <= 40:
    pagohoras = Valor_hora * Horast
    print(pagohoras)
elif Horast > 40:
    pagoextras = (Valor_hora * Horast) + (Horasext * bono_hextra)
    print(f'  salario total {pagoextras}')