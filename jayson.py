#importação da biblioteca
import json

def abrir(arquivo):
    file = open(arquivo,'r')
    arquivo = json.load(file)
    file.close()
    return arquivo

def salvar(dicionario, arquivo):
    file = open(arquivo,'w')
    json.dump(dicionario,file)
    file.close()

#Função de salvamento à cada modificação
def autSave():
    try:
        save = input("\nO SysColege por Default salva as alterações sempre que se volta ao Menu Principal.\nDeseja salvar as alterações a cada modificação (S/N)? ").upper()
        while not(save == "S" or save == "N"):
            save = input("\nEscolha inválida!\nDigite novamente (S/N):").upper()

    except:
        print("Escolha inválida! O valor deve ser 'S' ou 'N'\nDigite novamente!")
        save = autSave()
    
    return save