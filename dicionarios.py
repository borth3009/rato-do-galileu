#estrutura de dados que organiza as infus em pares (chaves ou valor)
skins_raras = {
    'ratobeso': 'motoquero azul',
    'liquidi guzzi': 'capetão',
    'ricardão do clube pinguin' : 'homi roxo',
    'cashwx' : 'cavaleiro negro',
    'docinho' : 'homi vermelho',
}
# indexsação 
print(skins_raras['ratobeso'])
# retorna o valor da chave
print(skins_raras.get('ratobeso'))
# retorna todas as chaves de um dicionario
print(skins_raras.keys())
# retorna todos os valores de cahves de um dicionario
print(skins_raras.values())
# retorna todas as chaves e valores do dicionario
print(skins_raras.items())
# recebendo (chave,valor) ele procura e se n encontra ele add no dicionario
print (skins_raras.setdefault('mugica','marchmelow'))
# apaga o dicionario inteiro
print(skins_raras.clear())