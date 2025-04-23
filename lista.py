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