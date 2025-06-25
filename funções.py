import random
#sem parametro e sem retorno
def boas_vindas ():
    print ("seja bem vindo!")
boas_vindas()

#sem parametro mas com retorno
def numero_aleatorio_1433():
    return random.randint(14,33)
print (numero_aleatorio_1433())

#com parametro e com retorno 
def multiplicação (a,b):
    return a*b
print (multiplicação(2,8))

#com parametro mas sem retorno
def ola_personalisado(nome):
    print (f'ola {nome} seja bem vindo!')
ola_personalisado('rato')

#exercicios
def desconto(valor,porcentagem):
    return valor*(porcentagem/100)
print (desconto(200,35))

senha = tuple('rato123')
senha_verificação = tuple(input('qual a sua senha:'))
def verificação (senha_verificada):
    if senha_verificada == senha :
        return print ('acesso sussedido:')
    else :
       return print ('acesso negado:')
verificação(senha_verificação)