"""
Ejercicio 3 — Agenda de contactos simple

Crea un programa que mantenga un “diccionario de contactos” donde:
La clave sea el nombre de la persona.
El valor sea su número de teléfono (cadena, para permitir +34... etc.).
El programa debería:

1. Empezar con un diccionario vacío.

2. Preguntar al usuario si quiere:

- Añadir contacto
- Buscar contacto
- Salir

3. Según la opción, actuar.
"""
nombre = "uwu"
numero= 0
contactos = {}

def nuevo_contacto():
    while True:
        nombre=input("\nIntroduzca el nombre de su contacto: ")
        if nombre in contactos:
            print("\n   El nombre que ha introducido ya está en la lista de contactos.")
        else:
            numero=input("\nEscriba el número del contacto: ")
            if numero in contactos:
                #Este if parece no funcionar por algún motivo
                print("\n   El número ya se encuentra en la lista")
            else:
                break

    contactos[nombre]=numero

def buscar():
    if len(contactos) == 0:
        print("\nLa lista se encuentra vacia.")
    else:
        while True:
            nombre=input("\nIntroduzca el nombre que quiere buscar: ")
            if nombre in contactos:
                print("\n   El número de " + str(nombre) + " es " + str(contactos[nombre]))
                break
            else:
                print("\n   El contacto que busca no se encuentra en la lista.")

while True:
    accion=input("""
Introduzca:

    '1' para añadir un contacto
    '2' para buscar un contacto en la lista
    '3' para salir del programa

""")
    if accion == "1":
        nuevo_contacto()
    elif accion == "2":
        buscar()
    else:
        break