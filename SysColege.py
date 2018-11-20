import Menu
import jayson

esc, opc, save = 0, 0, 0
loop = True

#tratativa de erro ao carregar arquivo JSON 
try:
    alunosDic = jayson.abrir('alunos.json')
    save = jayson.autSave()
except:
    print("Arquivo Json vazio ou não encontrado\nCarregando biblioteca default!")
    alunosDic = {"TESTE":[10.0,10.0,10.0]}

print("\n--- SysColege ---\n----- v14.0 -----")

#Menu Inicial
while(loop):
    
    #Lista de opções
    esc = Menu.menuInit()

    if(esc in range(5)):
        #Menu de Alunos
        while(esc == 1):
            import Alunos

            #Menu de escolha
            opc = Menu.menuAluno()
            
            #Adicionar aluno
            if(opc == 1):
                Alunos.addAluno(alunosDic)
                if(save == "S"):
                    jayson.salvar(alunosDic,'alunos.json')
                          
            #Deletar aluno
            elif(opc == 2):
                Alunos.delAluno(alunosDic)
                if(save == "S"):
                    jayson.salvar(alunosDic,'alunos.json')

            #Listagem de Alunos
            elif(opc == 3):
                Alunos.listAlunos(alunosDic)
            
            else:
                esc = 10
        
        #Menu Notas
        while(esc == 2):
            import Notas

            #Menu de escolha
            opc = Menu.menuNota()

            #Adicionar Nota
            if(opc == 1):
                Notas.addNota(alunosDic)
                if(save == "S"):
                    jayson.salvar(alunosDic,'alunos.json')
            
            #Editar Nota
            elif(opc == 2):
                Notas.editNota(alunosDic)
                if(save == "S"):
                    jayson.salvar(alunosDic,'alunos.json')

            #Deletar Nota
            elif(opc == 3):
                Notas.delNota(alunosDic)
                if(save == "S"):
                    jayson.salvar(alunosDic,'alunos.json')

            #Média da Turma
            elif(opc == 4):
                Notas.mediaTurma(alunosDic)
                
            else:
                esc = 10

        #Menu de Informações
        while(esc == 3):
            import Infos
            
            #Menu de escolha
            opc = Menu.menuInfo()

            #Consultar aluno
            if(opc == 1):
                Infos.buscarAluno(alunosDic)

            #Consultar melhor aluno
            elif(opc == 2):
                Infos.bestAluno(alunosDic)

            #Consultar alunos aprovados, na final e reprovados
            elif(opc == 3 or opc == 4 or opc == 5):
                Infos.resultAlunos(opc, alunosDic)

            else:
                esc = 10
        
        if(esc == 4):
            print("\n---Desenvolvedores---\n   Matheus Jordan\n   Lucas Emanuel\n\nProjeto iniciado em: 21/10/2018\nProjeto finalizado em: 20/11/2018")

        #Finalizar Syscolege
        else:
            loop = True if esc == 10 else False
            jayson.salvar(alunosDic,'alunos.json')