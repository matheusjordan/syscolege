def addNota(alunosDic={}, alunosLista=[], notas=[]):
    ler = input("\nDigite o nome do Aluno: ").upper()
    
    for ler in alunosDic:
        alunosLista.append(ler)
        break

    if(ler in alunosLista):
        chec_nota = len(alunosDic[ler])

        if(chec_nota == 3):
            print("\nAluno já possui três Notas")

        elif(chec_nota < 3):
            ler = float(input("\nDigite a nota do Aluno: "))
            print("\nNota",ler,"adicionada com Sucesso!")
            alunosDic[alunosLista[0]].append(ler)

    alunosLista = []

def editNota(alunosDic={}, alunosLista=[], notas=[]):
    ler = input("\nDigite o nome do Aluno: ").upper()

    if(ler in alunosDic):
        alunosLista.append(ler)
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

    alunosLista = []

def delNota(alunosDic={}, alunosLista=[], notas=[]):
    ler = input("\nDigite o nome do Aluno: ").upper()

    if ler in alunosDic:

        notas.append(alunosDic[ler])
        print("\nNotas:",notas)

        ler = float(input("\nDigite uma das Notas: "))
        
        
    else:
        return "\nAluno não cadastrado!"
    
    notas = []