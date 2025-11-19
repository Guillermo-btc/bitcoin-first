"""
Crea una función contar_vocales(texto) que devuelva un diccionario con el número de veces que aparece cada vocal
(a, e, i, o, u) en la cadena dada, sin distinguir mayúsculas/minúsculas.
"""

contador = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0,
}

texto=input("Escriba el texto: ")

for w in texto.lower():
    if w == "a":
        contador["a"]=contador["a"]+1
    elif w == "e":
        contador["e"]=contador["e"]+1
    elif w == "i":
        contador["i"]=contador["i"]+1
    elif w == "o":
        contador["o"]=contador["o"]+1
    elif w == "u":
        contador["u"]=contador["u"]+1

print(contador)