###
# 02 - Metacharactes
# los metacaracteres son simbolos especiales con significado 
# especificos en las expresiones reguales 
###

import re

text = "Hola mundo, H0la python, H$la regex"
patter = "H.la"

found = re.findall(patter, text);

if found:
    print(found)
else:
    print("No se a encontrado el patron")

# prefijo

text = "Hola mundo, H0la python, H$la regex"
patter = r"H.la"

found = re.findall(patter, text);

if found:
    print(found)
else:
    print("No se a encontrado el patron")


text = "Mi casa es blanca. y el coche es negro."
pattern = r"\."

matches = re.findall(pattern, text)

print(matches)


# \d: coincide con cualquier digito (0-9)
text = "El numero de telefono es 123456789"
found = re.findall(r'\d{9}', text)

print(found)

# detectar si hay un numero de mexico  en el texto prefijo +52
text = "Mi numero de telefono es +52 123456789 apuntalo vale?"
pattern = r"\+52 \d{9}"

found = re.findall(pattern, text)

if found: print(f"Encontre el numero de telefono {found.group()}")


# \w: coincide con cualquier caracter alfanumerico (a-z, A-Z, 0-9, _)
text = "@El_rubius_69"
pattern = r"\w"

found = re.findall(pattern, text)

print(found)


# \s: coincide con cualquier espacio en blanco
text = "Hola mundo\n¿Como estas?\t"
pattern = r"\s"

found = re.findall(pattern, text)

print(found)


# ^: coincide con el inicio de una cadena
text = "@423_name"
pattern = r"^\w" # validar nombre de usuario

valid = re.findall(pattern, text)

if valid: print("El nombre de usuario es valido")
else: print("El nombre de usuario no es valido")

phone = "+52 123456789"
pattern = r"^\+\d{2} "

valid = re.findall(pattern, phone)
if valid: print("El numero de telefono es valido")
else: print("El numero de telefono no es valido")


# $: coincide con el final de una cadena
text = "Hola mundo"
pattern = r"mundo$"

valid = re.findall(pattern, text)

# EJERCICIO 
# validar que un correo sea gmail.com
email = "willy@gmail.com"
pattern = r"^\w+@gmail\.com$"  # cuantificador + que haya una o mas veces un caracter alfanumerico
valid = re.findall(pattern, email)

if valid: print("El correo es valido")
else: print("El correo no es valido")


# \b: coincide con un limite de palabra
text = "casa casada casado"
pattern = r"\bcasa\b"  # solo coincide con la palabra casa completa
found = re.findall(pattern, text)
if found: 
    print("Se encontro la palabra casa")
else: print("No se encontro la palabra casa")

# |: coincide con una de las opciones u otra
fruits = "manzana, naranja, pera, kiwi"
pattern = r"manzana|pera"

found = re.findall(pattern, fruits)
if found: 
    print("Se encontro una de las frutas")