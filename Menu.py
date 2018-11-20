#Opções do Menu Principal
def menuInit():

    #Tratativa de erro para entrada de valores inesperados
    try:
        esc = int(input("\n-- Menu --\n01- Alunos\n02- Notas\n03- Informações sobre alunos\n00- Sair\nEscolha uma opção: "))
    except:
        print("Escolha inválida! O valor digitado é vazio ou não é um número!\nDigite novamente!")
        esc = menuInit()
    
    return esc

#opções do menu aluno
def menuAluno():

    #Tratativa de erro para entrada de valores inesperados
    try:
        opc = int(input("\n-- Alunos --\n01- Cadastrar Aluno\n02- Remover Aluno\n03- Listagem de Alunos\n00- Menu anterior\nEscolha uma opção: "))
    
        #Verificação da opção escolhida
        while(opc < 0 or opc > 3):
            opc = int(input("\nEscolha inválida\nDigite novamente: "))
    except:
        print("\nEscolha inválida! O valor digitado é vazio ou não é um número!\nDigite novamente!")
        opc = menuAluno()
    
    return opc

#opções do Menu Notas
def menuNota():

    #Tratativa de erro para entrada de valores inesperados
    try:
        opc = int(input("\n-- Notas --\n01- Adicionar Nota(s)\n02- Editar Nota(s)\n03- Remover Nota(s)\n04- Exibir média da Turma\n00- Menu anterior\nEscolha uma opção: "))

        #Verificação da opção escolhida
        while(opc < 0 or opc > 4):
            opc = int(input("\nEscolha inválida\nDigite novamente: "))
    except:
        opc = menuNota()
        
    return opc

def menuInfo():
    #opções
    try:
        opc = int(input("\n-- Menu de Informações --\n01- Consultar Aluno por nome\n02- Exbir melhor Aluno\n03- Alunos aprovados \n04- Alunos na final\n05- Alunos reprovados\n00- Sair\nEscolha uma opção: "))

        #Verificação da opção escolhida
        while(opc < 0 or opc > 5):
            opc = int(input("\nEscolha inválida\nDigite novamente: "))
    except:
        opc = menuInfo()
        
    return opc