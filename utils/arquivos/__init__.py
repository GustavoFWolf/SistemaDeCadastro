import os

def arcExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArc(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("Houve um erro na criação do arquivo")
    else:
        print("Arquivo criado com sucesso")

def lerArc(nome):
    try:
        a = open(nome, 'rt')
    except:
        print("erro")
    else:
        print(40*"-")
        print("PESSOA CADATRADAS".center(30))
        print(40*"-")
        for linha in a:
            dado = linha.split(';')
            dado[1] =dado[1].replace("\n","")
            print(f"{dado[0]:<30}{dado[1]} anos")
    finally:
        a.close()

def cadastro(arq, nome="desconhecido", idade=0):
    try:
        a = open(arq, 'at')
    except:
        print("erro")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("Erro")
        else:
            print(f"Novo registo de {nome} adicionado")
            a.close()

import os

def deleta(arq, nome, idade):
    linhaDeletar = f"{nome};{idade}\n"
    
    try:
        with open(arq, 'r') as original, open("tmp.txt", 'w') as tmp:
            encontrado = False
            for linha in original:
                if linha != linhaDeletar:
                    tmp.write(linha)
                else:
                    encontrado = True

        if encontrado:
            os.replace("tmp.txt", arq)
            print(f"Registro de {nome} deletado")
        else:
            os.remove("tmp.txt")
            print("Registro não encontrado")

    except:
        print("Erro")
