alunosDic = {}
notas = []
alunosLista = []
loop = True

while(loop):

#Menu Inicial
    esc = int(input("\n-- Menu --\n01- Alunos\n02- Notas\n03- Informações sobre alunos\n00- Sair\nEscolha uma opção: "))
    while(esc < 0 or esc > 3):
        esc = int(input("\nEscolha inválida!\nDigite novamente: "))
    
    else:
        #Menu de Alunos
        while(esc == 1):
            opc = int(input("\n-- Alunos --\n01- Cadastrar Aluno\n02- Remover Aluno\n03- Listagem de Alunos\n00- Menu anterior\nEscolha uma opção: "))

            while(opc < 0 or opc > 3):
                opc = int(input("\nEscolha inválida\nDigite novamente: "))
            
            #Cadastrar aluno
            if(opc == 1):
                ler = input("\nDigite o nome do Aluno: ").upper()
                ver = input("Digite novamente o nome do Aluno: ").upper()

                #Verificação do nome de alunos
                while(ler != ver):
                    ler = input("\nNomes diferentes!\nDigite o nome do aluno corretamente: ").upper()
                    ver = input("Digite novamente o nome do aluno: ").upper()

                
                notas = list(map(float, input("\nDigite as notas do Aluno: ").split()))
                
                #Vertificação da lista de notas
                c = len(notas)
                while(c < 1 or c > 3):
                    notas = list(map(float, input("\nNotas inválidas\nDigite notas válidas ou 0: ")))
                    c = len(notas)

                #verificação individual das notas
                for i in range(c):
                    while(notas[i] < 0 or notas[i] > 10):
                        notas[i] = float(input("\n" + str(i+1) + "º Nota inválida\nDigite novamente: "))
                
                print("\nAluno", ler,"foi cadastrado com sucesso!")
                alunosDic[ler] = notas

            #Deletar aluno
            elif(opc == 2):
                ler = input("\nDigite o nome do Aluno: ").upper()

                #Confirmar antes de apagar
                if(ler in alunosDic):
                    ok = input("\nRealmente deseja deletar o aluno (S/N)? ").upper()
                    if(ok == "S"):
                        del alunosDic[ler]
                        print("Aluno "+ ler +" excluido com Sucesso!")

                else:
                    print("\nAluno  digitado não se encontra na lista!")
                    
            #Listagem de Alunos
            elif(opc == 3):
                if(len(alunosDic) > 0):
                    ler = int(input("\n01- Por Nome\n02- Por Nota\nEscolha uma opção: "))

                    while(ler < 1 or  ler > 2):
                        ler = int(input("\nEscolha inválida\nDigite novamente: "))

                    if(ler == 1):
                        for i in alunosDic:
                            alunosLista.append(i)
                        alunosLista.sort()
                        for i in alunosLista:
                            print("\nNome:", i,"\nNotas:", alunosDic[i],"\nMédia: %.1f" %(sum(alunosDic[i])/3),"\n++_______++")
                        
                    elif(ler == 2):
                        print("\nEm breve")
                
                else:
                    print("\nNão há Alunos cadastrados no sistema!")
            
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
            opc = int(input("\n-- Menu de Informações --\n01- Consultar Aluno por nome\n02- Exbir melhor Aluno\n03- Alunos aprovados \n04- Alunos na final\n05- Alunos reprovados\nEscolha uma opção: "))

            while(opc < 0 or opc > 5):
                opc = int(input("\nEscolha inválida\nDigite novamente: "))

            if(opc == 1):
                ler = input("\nDigite o nome do Aluno: ").upper()
                
                if(ler in alunosDic):
                    print("\nAluno:",ler,"\nNotas:",alunosDic[ler],"\nMédia: %.1f" %(sum(alunosDic[ler]) / 3),"\nStatus: ")
                else:
                    print("\nAluno não cadastrado!")
        
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
