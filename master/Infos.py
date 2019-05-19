def buscarAluno(alunosDic = {}): 
    ler = input("\nDigite o nome do Aluno: ").upper()
           
    if(ler in alunosDic):
        print("\nAluno:",ler,"\nNotas:",alunosDic[ler],"\nMédia: %.1f" %(sum(alunosDic[ler]) / 3),"\nStatus: ")
    else:
        print("\nAluno não cadastrado!")

def  bestAluno(alunosDic = {}):
    alunosM = {}
    alunoBest = {}
    mediaANT = 0

    for i in alunosDic.keys():
        media = sum(alunosDic[i]) / 3
        alunosM[i] = media

        if(media > mediaANT):
            alunoBest = {}
            alunoBest[i] = media
        
        elif(media == mediaANT):
            alunoBest[i] = media
        
        mediaANT = media
    
    print(alunoBest.items())

