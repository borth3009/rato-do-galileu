#metodo .replase substitui uma palavra por outra
nic = "Rato Opressor"
nicnv = nic.replace (" Opressor","beso")
print (nicnv)

frs = "A loud É o melhOR time SO pERde pra TOdos"
#metodo .captalise coloca so a 1 letra maiusculo e as restantes em minusculas 
print (frs.capitalize())

#metodo .title() coloca todas as 1 letras em maiuscolo 
print (frs.title())

#metodo .center (quantidade,caracter) centraliza a palavra colocando os caracteres em volta
print ("laud".center(40,"-"))

#metodo .len() retorna o numero de caracteres da palavra/frase
nm = "Arthur Nunes Martins"
print (len(nm))

#metodo .lower deixa tudo minusculo
print (nm.lower())

#metodo .upper retorna o texto todo em maiusculo
print (nm.upper())

#metodo .find retorna a posição da 1 letar de uma palavra buscada 
frs2 = "o givem tem a melhor irelia do pbe"
print (frs2.find("irelia"))

#metodo .index() mesmo que o find so que da erro caso não ache a palavra
#print (frs2.index("fiddle do markin"))

#metodo .startwith() identifica se a str possui uma palavra expecifica e retorna false ou true
arqv = "ramister.pdf"
print (arqv.startswith("ramister"))

#metodo .endwith()
print (arqv.endswith(".pdf"))

#metodo .isalnum() verifica se na frase possui numeros ou letras
frs2 = "balãozinh0 RatoOpressor"
print (frs2.isalnum())#retorna buleano "true ou false"

#metodo .isalpha() retorna se tem apenas letras
frs3 = "14708350"
print (frs3.isalpha())

#metodo .isdigit() retorna se tem apenas numeros
print (frs3.isdigit())

#metodo .strip() deleta os espaços do começo e do fim 
senha = " asda  adsasda                        "
print (senha.strip())

#encadeamento de metodos = voce pode usar varios metodos em ordem para corrigir um frase
frs4 = "  AD PRo raTo NÂo fuNcIONA Des de semPRE   "
print (frs4.strip().lower().capitalize())