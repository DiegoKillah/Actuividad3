#Script calcular calificaciones finales // Diego Alejandro Salcido Pérez 
#26/07/26
#Ejemplo realizado con 3 parciales, 3 examenes por parcial y 1 proyecto final, con un porcentaje de 40% parciales, 30% proyecto y 30% examenes finales


print("-_-CALCULADORA DE CALIFICACIONES-_-")

parcial1 = float(input("Ingresa la calificación del primer parcial: "))
parcial2 = float(input("Ingresa la calificación del segundo parcial: "))
parcial3 = float(input("Ingresa la calificación del tercer parcial: "))

proyectof = float(input("Ingresa la calificación del proyecto: "))

examen1 = float(input("Ingresa la calificación del examen 1: "))
examen2 = float(input("Ingresa la calificación del examen 2: "))
examen3 = float(input("Ingresa la calificación del examen 3: "))

promedio_parciales = (parcial1 + parcial2 + parcial3) / 3
promedio_examenes = (examen1 + examen2 + examen3) / 3

calificacion_final = (promedio_parciales * 0.40) + (proyectof * 0.30) + (promedio_examenes * 0.30)

print(f"La calificación final es: {calificacion_final:.2f}"
