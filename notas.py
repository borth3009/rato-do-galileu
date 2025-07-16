def calcular_media(lista_notas):
    if len(lista_notas) == 0:
        return 0
    return sum(lista_notas) / len(lista_notas)
def avaliar_aluno(nome, lista_notas):
    media = calcular_media(lista_notas)

    if 9 <= media <= 10:
        print(f"Parabéns, {nome}! Excelente desempenho.")
    elif 7 <= media <= 8.9:
        print(f"Muito bem, {nome}! Você está indo bem.")
    elif 5 <= media <= 6.9:
        print(f"Atenção, {nome}. Você precisa se dedicar mais.")
    else:  # Abaixo de 5
        print(f"Força, {nome}!faz o L kk")
notas = [7.5, 8.0, 9.0]
avaliar_aluno("Rato", notas)