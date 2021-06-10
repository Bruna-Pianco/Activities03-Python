def adicionar(item,lista):
   lista.append(item)
   return lista

def remover(item,lista):
    try:
        lista.remove(item)
    except ValueError:
        print(f'código {item} não encontrado')

def exibir(lista):
    lista.sort()
    print(*lista, sep = " ")

string_produtos = input('')
list_pro = string_produtos.split(' ')
list_pro = [int(i) for i in list_pro]

while True:
    comando = input().split(' ')
    if comando[0] == 'adicionar':
        list_pro = adicionar(int(comando[1]), list_pro)
    elif comando[0] == 'remover':
        remover(int(comando[1]), list_pro)
    elif comando[0] == 'exibir':
        exibir(list_pro)
    elif comando[0] == 'encerrar':
        exibir(list_pro)
        break