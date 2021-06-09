n = int(input())
c = 0
n2 = 0

notasOriginais = []
notasAtividades = []
notasFinais = []
aux = 0
while c < n:
    x = float(input())
    c += 1
    if c <= n:
        notasOriginais.append(x)

    elif c > n:
        notasAtividades.append(x)

for c in range(n):
    novaNota = 0
    if notasAtividades[c] == 10:
        if notasOriginais[c] <= 8:
            novaNota = notasOriginais[c] + 2
            notasFinais.append(novaNota)
        elif 8 < notasOriginais[c] <= 10:
            novaNota = 10
            notasFinais.append(novaNota)
    elif notasAtividades[c] != 10:
        notasFinais.append(notasOriginais[c])

for c in range(n):
    if notasOriginais[c] != notasFinais[c]:
        aux += 1

print(f'NOTAS ALTERADAS: {aux}')

for c in range(n):
    if notasOriginais[c] != notasFinais[c]:
        if c < 9:
            print(f'({c+1:03}) original: {notasOriginais[c]:.2f} | final: {notasFinais[c]:.2f} ')
        if c >= 9:
            print(f'({c+1:03}) original: {notasOriginais[c]:.2f} | final: {notasFinais[c]:.2f} ')
        if c >= 99:
            print(f'({c+1:03}) original: {notasOriginais[c]:.2f} | final: {notasFinais[c]:.2f} ')
    elif notasOriginais[c] == notasFinais[c]:
        if c < 9:
            print(f'-({c+1:03}) original: {notasOriginais[c]:.2f} | final: {notasFinais[c]:.2f} ')
        if c >= 9:
            print(f'-({c+1:03}) original: {notasOriginais[c]:.2f} | final: {notasFinais[c]:.2f} ')
        if c >= 99:
            print(f'-({c+1:03}) original: {notasOriginais[c]:.2f} | final: {notasFinais[c]:.2f} ')