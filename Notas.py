def addNota(alunosDic={}):
    alunosLista = []

    nome = input("\nDigite o nome do Aluno: ").upper()
    
    for nome in alunosDic:
        alunosLista.append(nome)

    if(nome in alunosLista):
        nota = len(alunosDic[nome])

        if(nota == 3):
            return "\nAluno já possui três Notas"

        elif(nota < 3):
            ler = float(input("\nDigite a nota do Aluno: "))
            lista = alunosDic[nome]
            lista.append(ler)
            alunosDic[nome] = lista
            print("\nNota",ler,"adicionada com Sucesso!")

def editNota(alunosDic={}):
    notas = []

    ler = input("\nDigite o nome do Aluno: ").upper()

    if(ler in alunosDic):
        print("\nNotas:", alunosDic[ler])
        notas = alunosDic[ler]

    ler = float(input("\nEscolha uma das Notas: "))

    for i in notas:
        if(i == ler):
            pos = notas.index(ler)
            ler = float(input("Digite a nova Nota: "))
            notas[pos] = ler
            break

def delNota(alunosDic={}):
    alunosLista = []
    ler = input("Digite o nome do aluno: ").upper()
    for i in alunosDic:
        alunosLista.append(i)
    if ler in alunosLista:
        print("Notas:",alunosDic[ler])
        notas = alunosDic[ler]
    remover = float(input("Digite a nota à remover: "))
    for i in notas:
        if i == remover:
            notas.remove(remover)
            print("Nota removida com sucesso")
    alunosLista = []
