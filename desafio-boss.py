smprodintreg = []
pedidos = [
    ("Camisa", "Vestuário", 59.90, "Entregue"),
    ("Tênis", "Calçados", 199.90, "Cancelado"),
    ("Calça", "Vestuário", 89.90, "Entregue"),
    ("Fone de Ouvido", "Eletrônicos", 129.90, "Pendente"),
    ("Meia", "Vestuário", 19.90, "Entregue"),
    ("Notebook", "Eletrônicos", 3299.90, "Entregue"),
    ("Jaqueta", "Vestuário", 139.90, "Cancelado"),
]
print ('Produtos entregues'.center(40,"-"))
for p in pedidos :
    if p[3] == 'Entregue' :
        print (f'-{p[0]}')

for p in pedidos :
    if p[3] == 'Entregue' :
        smprodintreg.append(p[2])
        sm = sum(smprodintreg)
print (f'soma total dos valores entregues'.center(40,'-'))
print (sm)
print (f"ultimos 3 pedidos".center(40,'-'))
for p in pedidos[-3:]:
    print (p[0])
print (f'cancelados da categoria vestuarios'.center(40,'-'))
smvcc = 0
for p in pedidos :
    if p[1] == 'Vestuário' and p[3] == 'Cancelado':
        smvcc =+ 1
print(smvcc)

pergunta = input('qual categoria voce deseja ver: ')
for p in pedidos:
    if pergunta == p[1]:
        print (p[0])
        break
    elif pergunta != p[1] :
        print ("nâo temos essa categoria")
        break