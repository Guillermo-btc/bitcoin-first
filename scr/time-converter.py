"""Ejercicio 1 — Conversor de tiempo simple
Escribe un programa que:
Pida al usuario (por input) un número de minutos.
Calcule cuántas horas y minutos son (por ejemplo, 130 min → 2 horas y 10 minutos).
Imprima una frase tipo: "130 minutos son 2 horas y 10 minutos"."""

minutos=int(input("Minutos a convertir: "))

horas = minutos // 60
minutos_restantes = minutos % 60

print(str(minutos) + " minutos equivalen a: " + str(horas) + " horas y " + str(int(round(minutos_restantes,0))) + " minutos.")