"""
Ejercicio 2 — Estadísticas básicas de una lista

Crea una función resumen_numeros(lista) que reciba una lista de números y devuelva un diccionario con:

{
    "cantidad": ...,
    "suma": ...,
    "media": ...
}
"""
lista=[]

numero=0

while True:
    numero=(input('Escriba un número entero o "fin" para termianar: '))
    if numero == "fin":
        break
    lista.append(int(numero))

estadisticas={
    "cantidad": 0,
    "suma": 0,
    "media": 0
}

estadisticas["cantidad"] = len(lista)
estadisticas["suma"] = sum (lista)
estadisticas["media"] = round(estadisticas["suma"] / estadisticas["cantidad"] , 2)

print(estadisticas)