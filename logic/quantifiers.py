###
# 03 - Quantifiers
# los cuantificadores se utilizarn para especificar cuantas ocurrencias
# de un caracter o grupo de caracteres se deb encontrar en una cadena
###


import re

# *: puede coincidir con 0 o mas ocurrencias
text = "aaaba"
pattern = "a*"
matches = re.findall(pattern, text)
print(matches)


# +: puede coincidir con 1 o mas ocurrencias
text = "ddddd aaaa cccc bb"
pattern = "a+"
matches = re.findall(pattern, text)
print(matches)


# ?: cero o una vez
text = "aaabacb"
pettern = "a?b"
matches = re.findall(pettern, text)
print(matches)


# ejercicio: haz opcional que aparezca un +34 en el siguiente texto 



# {n}: exactamente n veces
text = "aaaaaa"
pattern = "a{3}"
matches = re.findall(pattern, text)
print(matches)