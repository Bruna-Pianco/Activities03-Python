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