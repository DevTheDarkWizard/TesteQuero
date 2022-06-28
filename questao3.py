import json

f = open("dados.json")

data = json.load(f)

menor = 0
menor_dia = 0
maior = 0
maior_dia = 0

total = 0
total_dias = 0
media = 0
dias = []


for i in data:
    faturamento = i
    total += faturamento["valor"]
    if(faturamento["valor"]!=0):
        total_dias+=1
        if(faturamento["valor"]>maior):
            maior = faturamento["valor"]
            maior_dia = faturamento["dia"]
        if(faturamento["valor"]<menor or menor==0):
            menor = faturamento["valor"]
            menor_dia = faturamento["dia"]

media = (total/total_dias)

for i in data:
    faturamento = i
    if(faturamento["valor"]>media):
        dias.append(faturamento["dia"])

print("Menor valor {} dia {}".format(menor,menor_dia))
print("Maior valor {} dia {}".format(maior,maior_dia))
print("Número de dias que o valor foi superior que a média mensal: {} dias: {}".format(len(dias),",".join(map(str,dias))))