
lista = {
    "SP": 67836.43,
    "RJ":36678.66,
    "MG":29229.88,
    "ES":27165.48,
    "Outros":19849.53
}

total = 0
for i in lista:
    total+=lista[i]
    
for i in lista:
    percent = (lista[i] * 100 / total)
    print("{} total em {:.2f}%".format(i,percent))