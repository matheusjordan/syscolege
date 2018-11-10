def buscarAluno(alunosDic): 
    ler = input("\nDigite o nome do Aluno: ").upper()
           
    if(ler in alunosDic):
        print("\nAluno:",ler,"\nNotas:",alunosDic[ler],"\nMédia: %.1f" %(sum(alunosDic[ler]) / 3),"\nStatus: ")
    else:
        print("\nAluno não cadastrado!")

#Função que exibe o melhor ou os melhores alunos
def bestAluno(alunosDic):
    alunosM = {}
    alunoBest = {}
    mediaANT = 0

    #Algoritmo para verificar os alunos
    for i in alunosDic.keys():
        media = sum(alunosDic[i]) / 3
        alunosM[i] = media

        if(media > mediaANT):
            alunoBest = {}
            alunoBest[i] = media
        
        elif(media == mediaANT):
            alunoBest[i] = media
        
        mediaANT = media
    
    #Mostrar o melhor ou os melhores alunos
    for i in alunoBest:
        print("\nAluno:",i,"\nMédia: %.1f" %alunoBest[i])

#Função para separar alunos aprovados dos reprovados
def resultAlunos(opc, alunosDic):
    alunos_aprovados = []
    alunos_reprovados = []
    alunos_final = []

    for i in alunosDic:
        media = sum(alunosDic[i]) / 3

        if(media >= 7):
            alunos_aprovados.append(i)
        
        elif(5 <= media < 7):
            alunos_final.append(i)
        
        elif(media < 5):
            alunos_reprovados.append(i)
    
    if(opc == 3):
        for i in alunos_aprovados:
            print(i)

    elif(opc == 4):
        for i in alunos_final:
            print(i)
            
    elif(opc == 5):
        for i in alunos_reprovados:
            print(i)
