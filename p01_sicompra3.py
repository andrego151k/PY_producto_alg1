print("producto alg1 1.-Compra de artículos")

Compras_Pagar = int(input(" ? cuantos articulos compraste ?: "))
if Compras_Pagar < 3:
    print("debes pagar en efectivo")   # Si los artículos comprados son menores a 3 Pagar en efectivo
else:
    print("debes pagar con tarjeta")   # caso contrario pagar con tarjeta.
