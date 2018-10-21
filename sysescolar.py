alunosDic = {}
alunosLista = []
loop = True

while(loop):

#Menu Inicial
    esc = int(input("\n-- Menu --\n01- Alunos\n02- Notas\n00- Sair\nEscolha uma opção: "))
    while(esc > 2 or esc < 0):
        esc = int(input("\nEscolha inválida!\nDigite novamente: "))
    
    else:
        
        while(esc == 1):
            opc = int(input("\n-- Alunos --\n01- Cadastrar Aluno\n02- Remover Aluno\n03- Listagem de Alunos\n04- Buscas\n00- Menu anterior\nEscolha uma opção: "))

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

        #Mata Loop
        else:
            loop = True if esc == 10 else False