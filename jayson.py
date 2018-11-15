#importação da biblioteca
import json

def abrir(arq):
    file = open(arq,'r')
    arq = json.load(file)
    file.close()
    return arq

def salvar(dic, arq):
    file = open(arq,'w')
    json.dump(dic,file)
    file.close()