enunciado = "sistema de cadastro"
print (enunciado.center(40,"."))
quantidadedecadastros = int(input("quantos jogadores vão entrar: "))
for j in range (quantidadedecadastros):
    nc = str(input("qual o seu nome: "))
    nk = input("qual o seu nick: ")
    jg = input("qual o jogo que vai jogar: ")
    idd = int(input("qual é a sua idade: "))
    strm = str(input("voce é um streamer (sim ou não): "))
    print ("-_-"*40)
    ncv = nc.title()
    nkv = nk.strip().lower().capitalize()
    jgv = jg.capitalize()

    
    print (f"nome: {ncv}")
    print (f"nick: {nkv}")
    print (f"jogo: {jgv}")
    if strm == "sim":
        print ("criador de cinteudo")
    else:
        print ("somente jogador")

    print ("-"*40)