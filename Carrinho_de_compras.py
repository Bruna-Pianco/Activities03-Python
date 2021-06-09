lista_produtos = []

def adicionar (lista_produtos,item=True):
    lista_produtos.append(item)
    lista_produtos.sort()
    return

def remover (lista_produtos,item=True):
    if item in lista_produtos:
        lista_produtos.remove(item)
    else:
        print(f"Código {item} não encontrado")
    return

def exibir(lista_produtos, item=True):
    for i in range(item):
        print(lista_produtos[i], end=' ')


carrinho = list(map(int,input().split()))
carrinho.sort()

comando = input().split()
item = input().split()

while True:
    comando = input().split(' ')
    if comando[0] =='adicionar':
        lista_produtos = adicionar(int(comando[1]),lista_produtos)
    elif comando[0] =='remover':
        remover = int(comando[1],lista_produtos)
    elif comando[0] =='exibir':
        exibir(lista_produtos[item])
    elif comando[0] == 'encerrar':
        exibir(lista_produtos[item])
        break    