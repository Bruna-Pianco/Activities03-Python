<img src="https://img.icons8.com/color/48/000000/python.png"/>

### Carrinho de Compras

Você está criando um site para uma loja virtual e precisa guardar os itens que os usuários adicionam em seu carrinho. Cada item é representado no sistema por um código numérico, isto é, um número inteiro que é capaz de identificá-lo unicamente. Como solução inicial, você decidiu guardar os itens adicionados ao carrinho em uma lista, e para testar o seu programa, implementou alguns comandos básicos para simular uma interação do usuário com o sistema:

adicionar: inclui o código de um novo produto à lista;remover: remove o código de um produto da lista;exibir: exibe os itens da lista em ordem crescente;encerrar: exibe os itens da lista, assim como no comando exibir, em ordem crescente, e encerra o programa.

A primeira linha poderá conter uma lista de inteiros separados por espaços, representando produtos que já estavam no carrinho, por exemplo, de uma sessão anterior que o usuário iniciou mas não finalizou a compra. Você deve receber essa lista e inicializar o carrinho de compras já com os códigos dessa lista, que devem ser números inteiros.

Caso não haja nenhum produto salvo de uma sessão anterior, essa primeira linha será uma linha em branco, sem nenhum texto ou caractere.

Entrada

A primeira linha poderá conter números inteiros separados por espaço ou ser uma linha em branco;

Cada linha seguinte conterá um dos comandos listados acima e, para os comandos "adicionar" e "remover", conterá também o código de um produto separado por um espaço;

A entrada termina sempre com o comando "encerrar".

Saída

A saída deve conter:

A exibição dos códigos na lista, separados por espaço, de acordo com a execução dos comandos "exibir" e "encerrar";A mensagem "código <código> não encontrado", quando o comando remover é executado com um código que não esteja presente na lista. Substitua <código> pelo número do código em questão (veja os exemplos para maiores detalhes).

<hr>

### Exibindo Tabuadas

Escreva um programa que receba como entrada dois números inteiros quaisquer A e B e exiba todas as tabuadas existentes no intervalo fechado crescente [ A..B ].

Entrada

Dois números inteiros, um em cada linha.

Saída

As tabuadas de todos os valores inteiros no intervalo fechado crescente [ A..B ]. Ao fim de cada tabuada, exibir uma linha com dez hifens ('-'). Caso A seja maior do que B, o intervalo será vazio e, neste caso, deve ser exibida somente a frase 'Nenhuma tabuada no intervalo!', sem apóstrofos. Obs.: Lembre-se de não exibir texto no input.

<hr>

### ImpacTube

A ImpacTube, uma famosa empresa de compartilhamento de vídeos, quer premiar alguns de seus mais notáveis criadores de conteúdo e, para isso, montará uma tabela com alguns canais que possuem grande quantidade de usuários inscritos. Os usuários inscritos em um canal são notificados quando um novo vídeo é postado.

No site da ImpacTube, os canais geram renda para seus criadores de conteúdo por meio de diversos mecanismos, a conhecida "monetização", o que geralmente é influenciado pela quantidade de usuários inscritos e que acessam aos vídeos postados.

A tabela terá a seguinte estrutura:

O nome do canal;A quantidade atual de inscritos; A monetização do último mês do canal e;Um valor indicando se o canal produz conteúdo premium, que são vídeos exclusivos para usuários que pagam uma mensalidade à ImpacTube.

Com esses dados será possível definir a bonificação de cada canal, que será composta pelo valor "monetização" da tabela acrescido de um valor fixo para cada mil inscritos.

Você foi escolhido para desenvolver um programa que receberá como entrada os dados de cada canal, gerando internamente a tabela modelo, e que mostrará os nomes dos canais, na ordem em que foram dados na entrada, acompanhados do valor que receberão como bonificação. Observe cuidadosamente o formato de entrada e o formato de saída especificados.

Na primeira linha será informado um valor inteiro que representa a quantidade N (1 <= N <= 200) de canais da tabela;Em cada uma das N linhas seguintes serão informados os registros que compõem a tabela, com os valores das colunas separados por um ponto e vírgula, nesta ordem: (1) uma string com o nome do canal que será bonificado; (2) um número natural que é a quantidade de inscritos no canal; (3) um valor real simbolizando a monetização do canal no mês anterior (dado em reais R$) e; (4) uma string 'sim' ou 'não', sem apóstrofos e completamente em minúsculo, que indica se o canal produz conteúdo premium;Por fim, serão informados dois valores reais, um em cada linha, que indicam o valor fixo que os canais receberão a mais para cada mil inscritos no canal. O primeiro valor é referente aos canais que possuem conteúdo premium e o segundo para canais que não possuem, ambos os valores estão em R$ (reais).

Saída

O cabeçalho com a palavra 'BÔNUS', sem apóstrofos e completamente em maiúsculo e, nas próximas N linhas, os nomes dos canais, na mesma ordem em que foram dados na entrada, acompanhados à direita pelo valor que receberão como bonificação, em reais e com duas casas decimais, exatamente como consta nos exemplos. Tome cuidado com a quantidade de hifens no cabeçalho.

<hr>

### Corra Forrest!

Forrest é um garoto que adora correr e contar histórias, as vezes até conta histórias sobre correr... vai entender. Como costuma correr diariamente pela cidade, Forrest sempre procura fazer o menor tempo possível, porém não é muito organizado e anota os tempos de suas corridas em papeis que são jogados em sua gaveta sem nenhum tipo de ordenação.

Como Forrest está muito ocupado ultimamente, planejando como cumprir uma promessa a um antigo amigo que adorava restaurantes e camarão, pediu a você que crie um programa que receba como entrada os tempos das corridas que estão nos papeis e calcule a média aritmética dos tempos gastos por Forrest para completar o seu percurso de corrida diário. Ao final, seu programa deve também exibir todos os tempos que ficaram abaixo dessa média, na mesma ordem em que foram recebidos na entrada.

Entrada

Diversos valores inteiros, um por linha, que representam os tempos gastos em cada corrida (em segundos);A entrada é finalizada com a inserção de um valor negativo, que não deve ser contabilizado.

Saída

Na primeira linha a palavra 'MEDIA', sem apóstrofos, sem acentuação e completamente em maiúsculo, seguida por dois pontos (':'), um caractere de espaço e um valor real com duas casas decimais, indicando a média dos tempos dados na entrada, em segundos;Nas linhas seguintes, os tempos que ficaram abaixo dessa média, em segundos, um por linha.

<hr>

### Segunda Chance

Em uma faculdade de um mundo muito distante, dois jovens professores buscam ajudar seus alunos a estudarem e melhorarem seus conhecimentos sobre a disciplina de programação, fazendo com que notas mais altas sejam conquistadas. Para isso, desenvolveram a estratégia da "Segunda Chance".

A estratégia da "Segunda Chance" consiste em criar uma nova atividade com os mesmos problemas da atividade original, porém com um prazo estendido e com a disponibilização de vídeos detalhados com a resolução de cada problema da atividade, de modo a incentivar que os alunos revisitem e comparem suas próprias propostas de solução.

Para aumentar ainda mais o incentivo para a turma, os professores concedem um bônus de dois pontos sobre a nota original para aqueles que resolverem TODOS os problemas dentro do prazo estendido, isto é, que obtiverem dez na nova atividade, o que é uma "moleza", considerando que basta assistir as resoluções e aplicá-las. Mas é claro, o bônus é concedido até o limite de dez pontos, ou seja, caso a soma do bônus com a nota original resulte em um valor superior a dez, a nota final será dez.

Como esperado, os alunos ficaram contentes e empolgados com a oportunidade. De tão agradecidos, ofereceram um software aos dois professores, de modo a reduzir um pouco da carga extra de trabalho que eles terão para recalcular as notas.

Você se voluntariou para implementar esse software, que precisa receber um valor inicial indicando a quantidade de alunos da turma, seguido pelas notas originais de cada aluno e pelas notas obtidas na nova atividade. O programa deverá exibir a quantidade de alunos que tiveram suas notas alteradas, assim como as notas originais e finais de cada aluno, destacando aqueles que aumentaram as notas.

Entrada

Na primeira linha haverá um número natural N (1 <= N <= 999) indicando a quantidade de alunos da turma;Nas próximas N linhas, haverá a nota original de cada aluno, que são valores reais no intervalo fechado [ 0,10 ];E, por fim, nas N linhas seguintes, haverá a nota obtida na nova atividade, também situadas no intervalo fechado [ 0,10 ].

Saída

A primeira linha será a frase 'NOTAS ALTERADAS: <quantidade>', sem apóstrofos e completamente em maiúsculo, em que <quantidade> deve ser substituído pela quantidade de alunos que tiveram suas notas originais alteradas em decorrência da aplicação do bônus;As próximas N linhas serão as notas de todos os alunos, na mesma ordem dada na entrada, iniciando com asterisco ('\*') para indicar as notas que foram alteradas e hífen ('-') para indicar aquelas que não foram, seguido pela posição da referida nota entre parênteses. O formato de cada linha pode ser observada nos exemplos, onde se destacam três características: (a) a posição tem sempre três dígitos, completada com zeros à esquerda quando necessário; (b) todas as notas são exibidas com duas casas decimais e; (c) todas as notas ocupam cinco colunas (o que inclui o caractere de ponto), completadas com zeros à esquerda quando necessário.

<hr>
