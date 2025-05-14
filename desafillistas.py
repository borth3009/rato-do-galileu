arena = [
    [1200,1500,1100,1800,1700],#arena1
    [1000,950,1100,1050,900],#arena2
    [2000,1900,1950,2100,2200]#arena3
]
medias = []
contador = 0
for p in arena:
    contador += 1
    media = sum(p) / len(p)
    medias.append(media)
    print (f"a media da arena {contador} foi {media}")
print (f"e a maior pontuação de arena foi de {max(medias)}")