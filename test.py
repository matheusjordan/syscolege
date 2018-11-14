#ad
import jayson

alunosDic = jayson.abrir('alunos.json')

#Tipo de operação
loop = True
while(loop):

    #Menu
    opc = int(input("01- Criar\n02- Ver\nEscolha: "))

    if(opc == 1):
        arquivo =  open('alunos.json','w',encoding = 'utf-8')
        
        nome = input("Digite o nome: ").upper()

        while(nome in alunosDic):
            nome = input("Nome já cadastrado!\nDigite novamente: ").upper()

        else:
            nota = list(map(int, input("Digite as notas: ").split()))
            
            qt = len(nota)
            if(qt > 3):
                nota = nota[0:3]
                qt = 3

            for i in range(qt):
                while(nota[i] < 0 or nota[i] > 10):
                    nota[i] = int(input(str(i +1) + "ª nota inválida!\nDigite novamente a nota: "))

            alunosDic[nome] = nota

    elif(opc == 2):
        #Printar elementos do dicionario
        for i in alunosDic:
            print(i,alunosDic[i])
    
    elif(opc == 0):
        loop = False
        jayson.salvar(alunosDic,'alunos.json')