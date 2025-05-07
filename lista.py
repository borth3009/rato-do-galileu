#lista de notas
lnt = [10,10,8]

#lista de str
lnm = ["alvaro","arthur","joaquim"]


media = sum(lnt) / len(lnt)
print (media)

#filtrandpo informacões
lnm2 = ["joaquim","arthur","carlos","joana"]
filtro = []
for n in lnm2:
    if n.startswith("j"):
        filtro.append(n)
        print(filtro)
##############################################################
listas_clientes = [
    ['alvaro','alvaro.sampaio@galileunegocios.com.br',32],
    ['felipe','nacibem@galileunegocios.com.br',41],
    ['matheus','matheus.biasotto@galileunegocios', 25]
]
#acessando o numero 41
print (listas_clientes[1][2])
#acessando o email matheus biasotto
print (listas_clientes[2][1])
############################################################
#elemento a ser adicionado -- usando .append que adiciona como ultimo elemento da lista
frutas = ['banana','uva','maçã']
salada = ['alface','tomate','cebola']
frutas.append(salada)
print (frutas)
#metodo .insert(posição,elemento)add item a uma posição expecifica
frutas.insert(2,'coringa')
print (frutas)
#metodo.remove(elemento) vai remover a primeira vez que elemento expecificado aparece
frutas.remove("banana")
print (frutas)
#metodo . sort() ele ordena em ordem alfabetica ou numerica -- mas se tiver reverse=true ele faz ao contrario
numeroaleatorio = [22,47,47,14,3,10]
numeroaleatorio.sort()
print (numeroaleatorio)
numeroaleatorio.sort(reverse=True)
print (numeroaleatorio)
#metodo .count(elemento) ele conta quantos vezes o elemento aparece na lista
print(numeroaleatorio.count(47))
#metodo len(lista) retona quantos elementos tem na lista
print(len(numeroaleatorio))
#metodo .index(elemento) retorna a posição do elemento expecificado
print (numeroaleatorio.index(10))