#criaremos uma função que somara 2 fatores e trara o resultado
def somar (a,b):
    soma = a + b
    return soma

pn = int(input("digite o primeiro numero: "))
sn = int(input("digite o segundo numero: "))

result = somar(pn , sn)
print (f"o resultado da soma é {result}")

