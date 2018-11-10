import Menu

alunosDic = {"MATHEUS":[9.0,7.0,7.0],"LUCAS":[9.0,7.0]}
esc, opc = 0, 0
loop = True

#Menu Inicial
while(loop):
    
    #Lista de opções
    esc = Menu.menuInit()

    for i in range(3):
        if(esc < 0 or esc > 3):
            esc = int(input("\nEscolha inválida!\nDigite novamente: "))

    else:
        #Menu de Alunos
        while(esc == 1):
            import Alunos

            #Menu de escolha
            opc = Menu.menuAluno()
            
            #Adicionar aluno
            if(opc == 1):
                Alunos.addAluno(alunosDic)
                          
            #Deletar aluno
            elif(opc == 2):
                Alunos.delAluno(alunosDic)
           
            #Listagem de Alunos
            elif(opc == 3):
                Alunos.listAlunos(alunosDic)
            
            else:
                esc = 10
        
        #Menu Notas
        while(esc == 2):
            import Notas

            #Menu de escolha
            opc = Menu.menuNota()

            #Adicionar Nota
            if(opc == 1):
                Notas.addNota(alunosDic)
            
            #Editar Nota
            elif(opc == 2):
                Notas.editNota(alunosDic)

            #Deletar Nota
            elif(opc == 3):
                Notas.delNota(alunosDic)

            #Média da Turma
            elif(opc == 4):
                Notas.mediaTurma(alunosDic)
                
            else:
                esc = 10

        #Menu de Informações
        while(esc == 3):
            import Infos
            
            #Menu de escolha
            opc = Menu.menuInfo()

            #Consultar aluno
            if(opc == 1):
                Infos.buscarAluno(alunosDic)

            #Consultar melhor aluno
            elif(opc == 2):
                Infos.bestAluno(alunosDic)

            #Consultar alunos aprovados, na final e reprovados
            elif(opc == 3 or opc == 4 or opc == 5):
                Infos.resultAlunos(opc, alunosDic)

            else:
                esc = 10

        #Mata Loop
        else:
            loop = True if esc == 10 else False
