loja_games = {
    'minecraft':{'preço': 59.90,'estoque': 5},
    'fifa':{'preço':199.90,'estoque': 4},
    'god of war' :{'preço': 149.90,'estoque':4},
}
print('-'*50)
carrinho = {}
while True:
    escolha_jogo = input('que jogo deseja comprar, caso deseje sair digite sair: ' )
    if escolha_jogo == 'sair':
        break
    if escolha_jogo.strip().lower() in loja_games :
        quantidade_compra = int(input ('quantos voce deseja comprar: '))
        infos_game = loja_games[escolha_jogo]
        if quantidade_compra <= infos_game['estoque']:
            loja_games[escolha_jogo]['estoque'] -= quantidade_compra
            print (f'jogo adicionado no carrinho')
            if escolha_jogo not in carrinho:
                carrinho[escolha_jogo] = quantidade_compra
            else: 
                carrinho[escolha_jogo] += quantidade_compra
            print('-'*50)
        else:
            print ('não a estoque suficiente')
    else :
        print (f'não temos o jogo {escolha_jogo}. tente semana que vem ')


    print (carrinho)
print('resumo da compra'.center('-'*40))
total = 0 
for jogo, qnt in carrinho.items():
    preço = loja_games[jogo]['preço']
    total += preço * qnt
    print (f'{jogo} x{qnt}'.center(40))
print('-'*40)
print (f'total R${total}'.center(40))