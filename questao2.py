valor = int(input("Insira o número que deseja verificar: "))

def fibonacci(req):
    n1 = 0
    n2 = 1
    n3 = 0
    contem = False
    while(n3 <= req):
        if(req==n3):
            contem = True
            break
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    return contem

print("O número {} {}pertence a sequência.".format(valor,"não " if not fibonacci(valor) else ""))