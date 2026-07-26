#Script para convertir de pesos mexicanos a dolares // Diego Alejandro Salcido Pérez
#26/07/26
#Version mejorada, un poco mas acomodada para facil lectura del usuario, ademas de agregar un if, ya que en la version original parece tener un error de sintaxis 

cantidad = float(input("Ingresa la cantidad en pesos mexicanos: "))

print("Monedas:")
print("1. USD")
print("2. EUR")
print("3. THB")
print("4. JPY")
print("5. KRW")
print("6. AUD")
print("7. PEN")
print("8. CAD")
print("9. VES")
print("10. ARS")

opcion = int(input("Elige una opción del 1 al 10: "))

match opcion:
    case 1:
        resultado = cantidad / 16.5
        moneda = "USD"
    case 2:
        resultado = cantidad / 18.0
        moneda = "EUR"
    case 3:
        resultado = cantidad / 0.45
        moneda = "THB"
    case 4:
        resultado = cantidad / 0.12
        moneda = "JPY"
    case 5:
        resultado = cantidad / 0.012
        moneda = "KRW"
    case 6:
        resultado = cantidad / 11.5
        moneda = "AUD"
    case 7:
        resultado = cantidad / 2.8
        moneda = "PEN"
    case 8:
        resultado = cantidad / 8.2
        moneda = "CAD"
    case 9:
        resultado = cantidad / 0.0023
        moneda = "VES"
    case 10:
        resultado = cantidad / 0.046
        moneda = "ARS"
    case _:
        resultado = None
        print("Opción no válida")

if resultado is not None:
    print(f"Cantidad convertida: {resultado:.2f} {moneda}")
