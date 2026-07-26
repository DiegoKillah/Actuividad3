#Script evaluacion de calificacion con letras (A, B C, D, F) // Diego Alejandro Salcido Pérez
#26/07/26
""" Version propia del ejercicio realizado en el examen anterior, pero decidi hacer mi propia versin de estos ejercicios, en este caso no hat tanto que cambiar 
    
"""
calificacion = float(input("Ingresa la calificación numérica: "))

if calificacion >= 90:
    print("La calificación es: A")
elif calificacion >= 80:
    print("La calificación es: B")
elif calificacion >= 70:
    print("La calificación es: C")
elif calificacion >= 60:
    print("La calificación es: D")
else:
    print("La calificación es: F")
