# Script para calcular el porcentaje de descuento de un producto
# Diego Alejandro Salcido Pérez
# 26/07/26
#Version propia del programa con algunas mejoras, como el saldo descontado y agradecimiento porl la compra.
precio_original = float(input("Ingresa el precio original del producto: "))

if precio_original < 100:
    descuento = 0

elif precio_original < 200:
    descuento = 0.10

elif precio_original < 500:
    descuento = 0.20

else:
    descuento = 0.25

precio_final = precio_original - (precio_original * descuento)

print(f"Descuento aplicado: {descuento * 100:.0f}%")
print(f"El precio final del producto es: ${precio_final:.2f}")
print(f"El descuento aplicado es: ${precio_original * descuento:.2f}")
print("Gracias por tu compra.")
