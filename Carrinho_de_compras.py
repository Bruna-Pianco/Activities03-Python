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



#correção

def converte_inteiro(lista):
    for i in range(len(lista)):
        lista[i] = int(lista[i])

def exibe(carrinho):
    for i in range(len(carrinho)):
        if i < len(carrinho) -1:
            print(carrinho[i], end=' ')
        else:
            print(carrinho[i])


carrinho = input().split()
if carrinho != []:
    converte_inteiro(carrinho)
comando = input().split()

while comando[0] != 'encerrar':
    if comando[0] == 'adicionar':
        carrinho.append(int(comando[1]))
    elif comando [0] == 'remover':
        comando[1] = int(comando[1])
        if comando [1] in carrinho:
             carrinho.remove(comando[1])
        else:
             print(f'código {comando[1]} não encontrado')
    else:
        carrinho.sort()       
        exibe(carrinho)  
    comando = input().split() 
carrinho.sort()       
exibe(carrinho)          

