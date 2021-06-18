n = int(input())

originais = []
for _ in range(n):
    originais.append(float(input()))

novas = [] 
for _ in range(n):
    novas.append(float(input()))

finais = []
qtd_alteradas = 0

for i in range(n):
    if novas[i] == 10 and originais[i] < 10:
        final = originais[i] + 2
        if final > 10:
            final = 10
        finais.append(final)
        qtd_alteradas += 1
    else:
        finais.append(originais[i])
print(f'NOTAS ALTERADAS: {qtd_alteradas}')

for i in range(n):
    if originais[i] != finais[i]:
        print(f'*({i+1:03}) original: {originais[i]:05.2f} | final: {finais[i]:05.2f}')
    else:
         print(f'-({i+1:03}) original: {originais[i]:05.2f} | final: {finais[i]:05.2f}')   



#correção

def coleta_notas(qtd):
    lista = []
    for _ in range(qtd):  
        lista.append(float(input()))
    return lista    

def notas_finais(originais,novas):
    qtd_alteradas = 0
    for i in range(len(originais)):
        if novas[i] == 10 and originais[i] < 10:
            novas[i] = min(originais[i] + 2, 10)
            qtd_alteradas += 1
        else:
            novas[i] = originais[i]
    return qtd_alteradas

def exibe(originais, finais, qtd_alteradas):
    print(f'NOTAS ALTERADAS: {qtd_alteradas}')
    for i in range(n):
        alterou = ('*' if originais[i] != finais[i] else '-')
        print(f'{alterou}({i+1:03}) original: {originais[i]:05.2f} | final: {finais[i]:05.2f}')
  

n = int(input())

originais = coleta_notas(n)
novas = coleta_notas(n)
qtd_alteradas = notas_finais(originais,novas)
exibe(originais, novas, qtd_alteradas)



         