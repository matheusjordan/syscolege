alunosDic = {"MATHEUS":[10,9,8]}
notas = []
alunosLista = []

loop = True

#Menu Inicial
while(loop):

    #Lista de opções
    esc = int(input("\n-- Menu --\n01- Alunos\n02- Notas\n03- Informações sobre alunos\n00- Sair\nEscolha uma opção: "))

    #Verificação da opção escolhida
    while(esc < 0 or esc > 3):
        esc = int(input("\nEscolha inválida!\nDigite novamente: "))
    
    else:
        
        #Menu de Alunos
        while(esc == 1):
            import Alunos

            #Lista de opções
            opc = int(input("\n-- Alunos --\n01- Cadastrar Aluno\n02- Remover Aluno\n03- Listagem de Alunos\n00- Menu anterior\nEscolha uma opção: "))

            #Verificação da opção escolhida
            while(opc < 0 or opc > 3):
                opc = int(input("\nEscolha inválida\nDigite novamente: "))

            #Adicionar aluno
            if(opc == 1):
                Alunos.addAluno(alunosDic)
                          
            #Deletar aluno
            elif(opc == 2):
                Alunos.delAluno(alunosDic)
           
            #Listagem de Alunos
            elif(opc == 3):
                Alunos.listAlunos(alunosDic, alunosLista)
            
            else:
                esc = 10
        
        #Menu Notas
        while(esc == 2):
            opc = int(input("\n-- Notas --\n01- Adicionar Nota(s)\n02- Editar Nota(s)\n03- Remover Nota(s)\n04- Exibir média da Turma\n00- Menu anterior\nEscolha uma opção: "))

            while(opc < 0 or opc > 4):
                opc = int(input("\nEscolha inválida\nDigite novamente: "))

            if(opc == 1):
                print("opc 1")
            
            elif(opc == 2):
                print("opc 2")

            elif(opc == 3):
                print("opc 3")

            elif(opc == 4):
                print("opc 4")

            else:
                esc = 10

        #Menu de Informações
        while(esc == 3):
            import Infos
            opc = int(input("\n-- Menu de Informações --\n01- Consultar Aluno por nome\n02- Exbir melhor Aluno\n03- Alunos aprovados \n04- Alunos na final\n05- Alunos reprovados\n00- Sair\nEscolha uma opção: "))

            while(opc < 0 or opc > 5):
                opc = int(input("\nEscolha inválida\nDigite novamente: "))

            if(opc == 1):
                Infos.buscarAluno(alunosDic)
        
            elif(opc == 2):
                print("opc 2")

            elif(opc == 3):
                print("opc 3")

            elif(opc == 4):
                print("opc 4")
        
            elif(opc == 5):
                print("opc 5")

            else:
                esc = 10

        #Mata Loop
        else:
            loop = True if esc == 10 else False
