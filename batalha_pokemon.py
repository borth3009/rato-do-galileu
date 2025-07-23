

pokemons = {
    'charmander':{'ataque': 'bola de fogo','dano':35},
    'squirtle':{'ataque': 'jatada','dano': 32},
    'bulbaconha':{'ataque':'brisa torta','dano':30},
}

jogador1 = ''
jogador2 = ''

def selecionar_pokemon(jogador) :
    print ('escolha seu pokemon'.center(40,'-'))
    print ('(1) charmander\n(2)squirtle\n(3)bulbaconha')
    print ('-'*40)
    escolha = int(input('escolha um dos pokemons: '))
    if escolha == 1:
        escolha = 'charmander'
    elif escolha == 2:
        escolha = 'squirtale'
    elif escolha == 3:
        escolha = 'bubaconha'
    else :
        print ('olha a pergunta retardado')
    
    return escolha

escolha1 = selecionar_pokemon(jogador1)
escolha2 = selecionar_pokemon(jogador2)

print (f'o jogador1 escolhe {escolha1}')
print (f'o jogador2 escolhe {escolha2}')
