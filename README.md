Jogo do "Banco Imobiliário"


https://wiki.termux.com/wiki/Main_Page
Termux e Termux-API instalado por F-Droid




script:

Decidir a ordem dos joagadores nos dados
minimo 2 máximo 4 jogadores
    armazenar informações dos jogadores
        input primeiro nome; padrão: jogador 1, jogador 2... até 4
        ordem para jogar
        posição atual no tabuleiro; padrão: 0 para todos, inicio de jogo
        quantidade dinheiro; padrão: 805
        voltas completas no tabuleiro; padrão: 0



Jogador da vez joga o dado
valor do dado é somado à posição atual do jogador
Jogador se move para a posição do tabuleiro que corresponde à soma (dado+posição)
se Posição não tem proprietario
    comprar propriedade
    não comprar
se Posição tem proprietário
    se o dono da propriedade for o próprio jogador
        investir para aumentar os ganhos
        nada a fazer
    se não
        pagar taxa da propriedade ao respectivo dono
Vez do próximo jogador
