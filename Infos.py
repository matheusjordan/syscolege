def buscarAluno(alunosDic = {}): 
    ler = input("\nDigite o nome do Aluno: ").upper()
           
    if(ler in alunosDic):
        print("\nAluno:",ler,"\nNotas:",alunosDic[ler],"\nMédia: %.1f" %(sum(alunosDic[ler]) / 3),"\nStatus: ")
    else:
        print("\nAluno não cadastrado!")
