string = "Marcela"

def inverter_string(s):
    invertida = ""
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    return invertida

resultado = inverter_string(string)
print("String original:", string)
print("String invertida:", resultado)
