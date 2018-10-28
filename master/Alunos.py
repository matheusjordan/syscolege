#função para validar notas
def validNota(c = 0):
    while(c < 1 or c > 3):
        notas = list(map(float, input("\nNotas inválidas\nDigite notas válidas ou 0: ")))
        c = len(notas)

#Função para adicionar alunos em uma lista
def addAluno(alunosDic = {}):
    ler = input("\nDigite o nome do Aluno: ").upper()
    ver = input("Digite novamente o nome do Aluno: ").upper()

    #Verificação do nome de alunos
    while(ler != ver):
        ler = input("\nNomes diferentes!\nDigite o nome do aluno corretamente: ").upper()
        ver = input("Digite novamente o nome do aluno: ").upper()

    
    notas = list(map(float, input("\nDigite as notas do Aluno: ").split()))
    
    #Vertificação da lista de notas
    c = len(notas)

    #verificação individual das notas
    for i in range(c):
        while(notas[i] < 0 or notas[i] > 10):
            notas[i] = float(input("\n" + str(i+1) + "º Nota inválida\nDigite novamente: "))

    alunosDic[ler] = notas
    print("\nAluno", ler,"foi cadastrado com sucesso!")


def delAluno(alunosDic = {}):
    ler = input("\nDigite o nome do Aluno: ").upper()
    #Confirmar antes de apagar
    if(ler in alunosDic):
        ok = input("\nRealmente deseja deletar o aluno (S/N)? ").upper()
        if(ok == "S"):
            del alunosDic[ler]
            print("Aluno "+ ler +" excluido com Sucesso!")

    else:
        print("\nAluno  digitado não se encontra na lista!")

def listAlunos(alunosDic = {}, alunosLista = []):
    ler = int(input("\n01- Por Nome\n02- Por Nota\nEscolha uma opção: "))

    while(ler < 1 or  ler > 2):
        ler = int(input("\nEscolha inválida\nDigite novamente: "))

    if(ler == 1):
        for i in alunosDic:
            alunosLista.append(i)
        alunosLista.sort()
        
        for i in alunosLista:
            print("\nNome:", i,"\nNotas:", alunosDic[i],"\nMédia: %.1f" %(sum(alunosDic[i])/3),"\n___________")
        
    elif(ler == 2):
        print("\nEm breve")

    else:
        print("\nNão há Alunos cadastrados no sistema!")
