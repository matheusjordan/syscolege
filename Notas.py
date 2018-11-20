def addNotas(alunosDic):
    try:
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
        
        return notas
    except:
        print("\nNota(s) inválida(s)! O valor digitado é vazio ou não é um número!\nDigite novamente!")
        notas = addNotas(alunosDic)
        
    return notas

#Função para adicionar uma nota aos alunos
def addNota(alunosDic):
    alunosLista = []
    nome = input("\nDigite o nome do Aluno: ").upper()
    
    #Verificação do nome do aluno
    if(nome in alunosDic):
        alunosLista.append(nome)
    else:
        print("\nAluno não cadastrado")

    #Adicionar nota do aluno caso ele passe pela verificação
    if(nome in alunosLista):
        nota = len(alunosDic[nome])

        if(nota == 3):
            print("\nAluno já possui três Notas")

        #Leitura da nota
        elif(nota < 3):
            ler = float(input("\nDigite a nota do Aluno: "))

            while(ler < 0 or ler > 10):
                ler = float(input("\nNota inválida! Digite novamente: "))

            lista = alunosDic[nome]
            lista.append(ler)
            alunosDic[nome] = lista
            print("\nNota",ler,"adicionada com Sucesso!")

#Função para editar notas dos alunos
def editNota(alunosDic):
    notas = []

    ler = input("\nDigite o nome do Aluno: ").upper()

    #Verificação do nome do aluno
    if(ler in alunosDic):
        print("\nNotas:", alunosDic[ler])
        notas = alunosDic[ler]
        ler = float(input("\nEscolha uma das Notas: "))

        #Editar nota do aluno
        for i in notas:
            if(i == ler):
                pos = notas.index(ler)
                ler = float(input("\nDigite a nova Nota: "))

                while(ler < 0 or ler > 10):
                    ler = float(input("\nNota inválida! Digite novamente: "))

                notas[pos] = ler
                break
        
        print("\nNota modificada com sucesso!")
    else:
        print("\nAluno não cadastrado!")

#Função para deletar nota do aluno
def delNota(alunosDic):
    alunosLista = []

    ler = input("\nDigite o nome do aluno: ").upper()
    for i in alunosDic:
        alunosLista.append(i)

    #Verificação do nome do aluno
    if(ler in alunosLista):
        print("\nNotas:",alunosDic[ler])
        notas = alunosDic[ler]

        remover = float(input("\nDigite a nota à remover: "))

        while not(remover in notas):
            remover = float(input("\nNota inválida! Digite novamente: "))

        #Deletar nota
        for i in notas:
            if(i == remover):
                rnota = notas.index(remover)
                rnota = notas.pop(rnota)
                print(f"\nNota {rnota} removida com sucesso")
                break

        alunosDic[ler] = notas
    else:
        print("\nAluno não cadastrado!")
    alunosLista = []

#Função para calcular média da turma
def mediaTurma(alunosDic):
    notas = []

    for i in alunosDic:
        notas.append(sum(alunosDic[i]))
    
    #Calculo da média
    numero_alunos = len(notas)
    media_turma = (sum(notas) / (numero_alunos *3))
    
    print("\nMédia da turma: %.1f" %media_turma)
    
    #Verificação do desempenho da turma
    if(media_turma > 7):
        print("O desempenho da turma está ótimo!")
    elif(media_turma < 7 and media_turma >= 5):
        print("O desempenho da turma está ruim!")
    elif(media_turma < 5):
        print("O desempenho da turma está péssimo!")

    