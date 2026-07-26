#Script para revisar la edad de una persona, para verificar si puede efectuar un voto // Diego Alejandro Salcido Pérez
#26/07/26
#El ejercicio es copiar los scripts realizados en el examen anterior, pero decidi hacer mi propia versin de estos ejercicios
print("-_-VERIFICADOR DE EDAD PARA VOTAR-_-")

edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Puedes votar.")
else:
    print("No puedes votar.")
