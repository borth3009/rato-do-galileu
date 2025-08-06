import random

pokemons = {
    'charmander':{'ataque': 'bola de fogo','Dano':35},
    'squirtle':{'ataque': 'jatada','Dano': 32},
    'bulbaconha':{'ataque':'brisa torta','Dano':30},
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
        escolha = 'squirtle'
    elif escolha == 3:
        escolha = 'bulbaconha'
    else :
        print ('olha a pergunta retardado')
    
    return escolha

escolha1 = selecionar_pokemon(jogador1)
escolha2 = selecionar_pokemon(jogador2)

print (f'o jogador1 escolhe {escolha1}')
print (f'o jogador2 escolhe {escolha2}')


def ficha_habilidades(jogador) :
    print("FICHA HABILIDADES".center(40,"*"))
    print(f'vida = 100|ataque = {pokemons[jogador]['ataque']}|dano = {pokemons[jogador]['Dano']}')
    
ficha_habilidades(escolha1)
ficha_habilidades(escolha2)

def ataque(escolha):
    return pokemons[escolha]['Dano']*random.uniform(1,2)

dano1 = ataque(escolha1)
dano2 = ataque(escolha2)

print(f'o dano de {jogador1} foi de {pokemons[escolha1]['Dano']*random.uniform(1,2):.2f}')
print(f'o dano de {jogador2} foi de {pokemons[escolha2]['Dano']*random.uniform(1,2):.2f}')

ataque(escolha1)
ataque(escolha2)

def batalha():
    vida1 = 100 - dano2
    vida2 = 100 - dano1
    if vida1 > vida2 :
        print(f'o vencedor foi {escolha1} pois {escolha2} ficou com menos vida')
    else:
        print(f'o vencedor foi {escolha2} pois {escolha1} ficou com menos vida')

batalha()