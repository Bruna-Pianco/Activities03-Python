def main():
    # valor inteiro que representa a quantidade N (1 <= N <= 200) de canais
    N = int(input('Quantidade de canais: '))
 
    dados_canais = []
 
    # Em cada uma das N linhas seguintes serão informados os registros que
    # compõem a tabela
    for i in range(1, N+1):
        linha = input(f'Dados do {i}º canal: ')
 
        # com os valores das colunas separados por um ponto e vírgula
        valores = linha.split(';')
 
        # string com o nome do canal que será bonificado
        nome = valores[0]
 
        # número natural que é a quantidade de inscritos no canal
        qtd_inscritos = int(valores[1])
 
        # valor real simbolizando a monetização do canal no mês anterior
        monetizacao_anterior = float(valores[2])
 
        # string 'sim' ou 'não' que indica se o canal produz conteúdo premium
        is_premium = valores[3] == 'sim'
 
        dados_canal = (nome, qtd_inscritos, monetizacao_anterior, is_premium)
 
        dados_canais.append(dados_canal)
 
    # O primeiro valor é referente aos canais que possuem conteúdo premium
    valor_com_premium = float(input('Valor fixo com premium: '))
 
    # o segundo para canais que não possuem
    valor_sem_premium = float(input('Valor fixo sem premium: '))
 
    # TODO: Saída do programa
    print(f"{nome} : R${valores:.2f} ")
 
if nome == 'main':
    main()