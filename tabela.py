def exibe_tabela(tabela):
    for linha in tabela:
        print(linha)
    print()

def bonificacao(tabela):
    for linha in tabela:
        bonus = linha[1] + (linha[1] * linha[2] * 0.05)
        if linha[3] == 'sim':
            bonus += bonus * 0.10
        print(f'{linha[0]}: R$ {bonus:.2f}')

def preenche_tabela(qtd_funcionarios):
    tabela = []
    for i in range(qtd_funcionarios):
        linha = input(f'Linha {i}: ').split(';')
        linha[1] = float(linha[1])
        linha[2] = int(linha[2])
        # linha[3] = linha[3] == 'sim' # para transformar em boolean
        tabela.append(linha)
    return tabela

n = int(input('Quantidade de funcionários: '))
tabela = preenche_tabela(n)
exibe_tabela(tabela)
bonificacao(tabela)
