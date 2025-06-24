
import re


# [: coincide con cualquier caracter dentro de los corchetes]

username = "rub.ius_69+"
pattern = r"^[\w._%+-]+$"

match = re.search(pattern, username)

if match:
    print("El nombre de usuario es valido")
else:
    print("El nombre de usuario no es valido")


# Buscar todas las vocales en una cadena
text = "Hola mundo"
pattern = r"[aeiou]"
matches = re.findall(pattern, text)
print(matches)


# una regex para encontrar las palabras man, fan y ban
# pero ignoradno el resto 

text = "man ran fan ñan ban"
pattern = r"[mfb]an"

matches = re.findall(pattern, text)
print(matches)
