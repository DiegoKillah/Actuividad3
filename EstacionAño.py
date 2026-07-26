#Script para calcular la estacion del año match case con estaciones // Diego Alejandro Salcido Pérez
#26/07/26
"""En este caso resolvi el examen de manera erronea, ya que al pedir usar switch entendi que se tenia que colocarn la parte de abajo, despues pasandolo a codigo note que switch ya se usa 
desde que se coloca match case, ya que switch no es valido en python
"""
mes = int(input("Ingresa el número del mes (1-12): "))

match mes:
    case 12 | 1 | 2:
        estacion = "Invierno"
    case 3 | 4 | 5:
        estacion = "Primavera"
    case 6 | 7 | 8:
        estacion = "Verano"
    case 9 | 10 | 11:
        estacion = "Otoño"
    case _:
        print("Número de mes inválido")

print(f"La estación es: {estacion}")
print("Gracias por usar el programa.")
