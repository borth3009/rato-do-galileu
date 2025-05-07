#criando listas alinhadas de alunos e suas notas 
lista_alunos = [ 
    ["arthur",[9,7,7]],
    ["alvaro",[1,5,10]]
]

#fazendo a media das notas 
for i in lista_alunos:
    media = sum(i[1])/len(i[1])
    print (f"a media do aluno {i[0]} é de {media:.1f}")