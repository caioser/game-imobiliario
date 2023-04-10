def clear():
    print('\033c', en='')

class Screen:
    map = '''Game Imobiliário
    novo jogo
        jogadores
    continuar jogo salvo
        listar jogos salvos
    configs
    sair
    '''
    new_game = '''Novo jogo
    jogadores: 4
        Vermelho
        Verde
        Azul
        Amarelo

1 - definir quantidade de jogadores
2 - mudar nomes dos jogadores
        
        '''