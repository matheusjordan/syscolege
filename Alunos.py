#Função para adicionar alunos em uma lista
def addAluno(alunosDic):
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

    alunosDic[ler] = notas
    print("\nAluno", ler,"foi cadastrado com sucesso!")

#Função deletar aluno
def delAluno(alunosDic):
    ler = input("\nDigite o nome do Aluno: ").upper()
    #Confirmar antes de apagar
    if(ler in alunosDic):
        ok = input("\nRealmente deseja deletar o aluno (S/N)? ").upper()
        if(ok == "S"):
            del alunosDic[ler]
            print("Aluno "+ ler +" excluido com Sucesso!")

    else:
        print("\nAluno  digitado não se encontra na lista!")

#Função listar alunos 
def listAlunos(alunosDic):
    alunosLista = []
    ler = int(input("\n01- Por Nome\n02- Por Nota\nEscolha uma opção: "))

    while(ler < 1 or  ler > 2):
        ler = int(input("\nEscolha inválida\nDigite novamente: "))

    #Pela ordem alfabética
    if(ler == 1):
        for i in alunosDic:
            alunosLista.append(i)
        alunosLista.sort()

        for i in alunosLista:
            print("\nNome:", i,"\nNotas:", alunosDic[i],"\nMédia: %.1f" %(sum(alunosDic[i])/3),"\n")
    
    #Por nota
    elif(ler == 2):
        alunosM = {}

        #Criação de dicionario por media
        for aluno in alunosDic:
            media = sum(alunosDic[aluno]) / 3
            
            while(media in alunosM):
                media += 0.1
            
            alunosM[media] = aluno
        
        #Adicionado todas as chaves do dicionario a uma lista ordenada
        mediaLis = list(alunosM.keys())
        mediaLis.sort(reverse=True)

        #Algoritmo para mostrar em ordem decrescente os alunos a partir da maior nota
        for media in mediaLis:
            aluno = alunosM[media]
            
            if(media >= 7):
                status = "Aprovado"

            elif(media < 7 and media > 4.9):
                status = "Final" 

            elif(media < 5):
                status = "Reprovado"

            md = sum(alunosDic[aluno]) / 3
            print(f"Nome: {aluno}\nNotas: {alunosDic[aluno]}\nMédia: {round(md, 1)}\nStatus: {status}\n")
