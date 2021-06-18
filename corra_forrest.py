lista = []
segundos = int(input())

while segundos >= 0:
        lista.append(segundos)
        segundos = int(input())

media = sum(lista) / len(lista)
print(f'MEDIA: {media:.2f}')
for x in lista:
    if x < media:
       print(x)


#correção1

tempos = []
soma = 0
qtd = 0

tempo = int(input())

while tempo >= 0:
    tempos.append(tempo)
    soma += tempo
    qtd += 1
    tempo = int(input())
media = soma / qtd
print(f'MÉDIA: {media:.2f}')    

for i in range (len(tempos)):
        if tempos[i] < media:
                print(tempos[i])


#correção2

tempos = []
tempo = int(input())

while tempo >= 0:
    tempos.append(tempo)
    tempo = int(input())
media = sum(tempos) / len(tempos)
print(f'MEDIA: {media:.2f}')    

for tempo in tempos:
        if tempo < media:
                print(tempo)

