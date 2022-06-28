valor = input("Insira um texto: ")

def inverter(texto):
    result = ""
    for i in range(len(texto)-1,-1,-1):
        result = result + texto[i]
    return result

print(inverter(valor))