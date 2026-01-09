from utils.funções import menu,leiaInt
from utils.arquivos import arcExiste, criarArc, lerArc,cadastro, deleta

arq = 'arquivo.txt'

if(arcExiste(arq)):
    print("Arquivo encontrado com sucesso")
else:
    print("Não achei o arquivo")
    criarArc(arq)
menu()
while True:
    option = leiaInt("Escolha uma opção: ")
    if(option == 4):
        break
    elif(option == 1):
        lerArc(arq)
    elif(option == 2):
        nome = input("Qual é o nome dessa pessoa? ")
        idade = int(input("Quantos anos ela tem? "))
        cadastro(arq,nome,idade)
    elif(option == 3):
        nome = input("Qual é o nome dessa pessoa? ")
        idade = int(input("Quantos anos ela tem? "))
        deleta(arq,nome,idade)
    menu()
print("Tchau! Volte sempre")

    