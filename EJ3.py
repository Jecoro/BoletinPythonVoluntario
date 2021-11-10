cadena = [x for x in input("Introduce expresion") if x in "{}[]()"]
if len(cadena) % 2 != 0 or len(cadena) == 0:
        respuesta = "No estan balanceados"
else:
        respuesta = "Estan balanceados"
        i = 0
        while 0 < len(cadena) and respuesta == "Estan balanceados":
            if cadena[i] in "{[(":
                i += 1
            else:
                if cadena[i - 1] + cadena[i] in '{}' or \
                        cadena[i - 1] + cadena[i] in '[]' or \
                        cadena[i - 1] + cadena[i] in '()':
                    cadena = cadena[:i - 1] + cadena[i + 1:]
                    i -= 1
                else:
                    respuesta = "No estan balanceados"
print(respuesta)
