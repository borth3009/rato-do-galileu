jogos = {
    'lol': {'preço':'sua alma','estoque':5},
    'minecraft':{'preço': 59.90,'estoque': 5},
    'fifa':{'preço':199.90,'estoque': 4},
    'god of war' :{'preço': 149.90,'estoque':4},
}
for k, v in jogos.items():
    print (f'a chave é {k} e o valor é {v['preço']}')