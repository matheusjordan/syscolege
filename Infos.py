def buscarAluno(alunosDic): 
    ler = input("\nDigite o nome do Aluno: ").upper()
           
    if(ler in alunosDic):
        media = sum(alunosDic[ler]) / 3
        print("\nAluno:",ler,"\nNotas:",alunosDic[ler],"\nMédia: %.1f" %(media))

        if(media >= 7):
            print("Status: Aluno Aprovado")
        elif(media < 7 and media >= 5):
            print("Status: Aluno na Final")
        if(media < 5):
            print("Status: Aluno Reprovado")

    else:
        print("\nAluno não cadastrado!")

#Função que exibe o melhor ou os melhores alunos
def bestAluno(alunosDic):
    mediaANT = 0
    mediaMaior = 0

    #Algoritmo para verificar os alunos
    for i in alunosDic.keys():
        media = sum(alunosDic[i]) / 3
        
        if(media >= mediaANT):
            mediaMaior = media
            alunoBest = i
        mediaANT = mediaMaior
    
    #Mostrar o melhor aluno
    print("\nAluno:",alunoBest,"\nNotas:",alunosDic[alunoBest],"\nMédia: %.1f" %mediaMaior)

#Função para separar alunos aprovados dos reprovados
def resultAlunos(opc, alunosDic):
    alunos_aprovados = {}
    alunos_reprovados = {}
    alunos_final = {}

    #Adicionar alunos
    for i in alunosDic:
        media = sum(alunosDic[i]) / 3
        notas = alunosDic[i]

        if(media >= 7):
            alunos_aprovados[i] = notas
        
        elif(5 <= media < 7):
            alunos_final[i] = notas
        
        elif(media < 5):
            alunos_reprovados[i] = notas
    
    if(opc == 3):
        for i in alunos_aprovados:
            media = sum(alunosDic[i]) / 3
            print(f"\nNome: {i}\nNotas: {alunosDic[i]}\nMédia: %.1f" %(media))

    elif(opc == 4):
        for i in alunos_final:
            media = sum(alunosDic[i]) / 3
            print(f"\nNome: {i}\nNotas: {alunosDic[i]}\nMédia: %.1f" %(media))
            
    elif(opc == 5):
        for i in alunos_reprovados:
            media = sum(alunosDic[i]) / 3
            print(f"\nNome: {i}\nNotas: {alunosDic[i]}\nMédia: %.1f" %(media))
