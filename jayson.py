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