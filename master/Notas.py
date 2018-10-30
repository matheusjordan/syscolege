def addNota(alunosDic={}):
    alunosLista = []

    ler = input("\nDigite o nome do Aluno: ").upper()
    
    for ler in alunosDic:
        alunosLista.append(ler)
        break

    if(ler in alunosLista):
        nota = len(alunosDic[ler])

        if(nota == 3):
            return "\nAluno já possui três Notas"

        elif(nota < 3):
            ler = float(input("\nDigite a nota do Aluno: "))
            alunosDic[alunosLista[0]].append(ler)
            return "\nNota",ler,"adicionada com Sucesso!"

def editNota(alunosDic={}):
    notas = []

    ler = input("\nDigite o nome do Aluno: ").upper()

    if(ler in alunosDic):
        print("\nNotas:", alunosDic[ler])
        notas = alunosDic[ler]

    ler = float(input("\nEscolha uma das Notas: "))
    print(notas)

    for i in notas:
        if(i == ler):
            pos = notas.index(ler)
            ler = float(input("Digite a nova Nota: "))
            notas[pos] = ler
            break

def delNota(alunosDic={}):
    notas = []

    ler = input("\nDigite o nome do Aluno: ").upper()

    if ler in alunosDic:

        notas.append(alunosDic[ler])
        print("\nNotas:",notas)

        ler = float(input("\nDigite uma das Notas: "))
           
    else:
        return "\nAluno não cadastrado!"