estoque =(
    ("mouse LG tech", 10),
    ("mic hyperx", 5),
    ("acer nitro 5", 3),
    ("webcam HD", 0)
)
#percorrendo a tupla
print ("produtos de menos de 5 unidades:")
for i in estoque :
    if i[1] < 5 :#verifica o numero de itens
        print (f'-{i[0]}')#tem que sair o produto
    if i[1] == 0 :
        print (f'produtos esgotados: -{i[0]}')
soma = 0
for q in estoque:
    soma += q[1]
print (f'a soma de tudo é {soma}')