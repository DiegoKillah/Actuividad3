#sCRIPT PARA CONVERTIR GRADOS FAHRENHEIT A GRADOS CELSIUS Y VICEVERSA // Diego Alejandro Salcido Pérez
#26/07/26
# El codigo tiene la mejora de contar con un "menu" para elegir si se requiere farenheit  o kelvin , mostrado de una mejor manera ya que, es mas facil para el usuario se se le comenta si usar 1 o 2, como un menu de voz tradicional

print("-_-CONVERSOR DE TEMPERATURA-_-")
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
print("Fahrenheit \n. Kelvin")
opcion = int(input("Elige la opción 1 para Fahrenheit o 2 para Kelvin: "))

match opcion:
    case 1:
        resultado = (celsius * 9/5) + 32
        unidad = "°F"
    case 2:
        resultado = celsius + 273.15
        unidad = "K"
    case _:
        resultado = None
        print("Opción inválida")

if resultado is not None:
    print(f"La temperatura convertida es: {resultado:.2f} {unidad}")
