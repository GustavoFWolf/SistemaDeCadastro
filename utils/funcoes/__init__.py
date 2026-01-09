def menu():
    print(40*"-")
    print("MENU PRINCIPAL".center(30))
    print(40*"-")
    print("1 - Ver pessoas cadastradas")
    print("2 - Cadastrar nova Pessoa")
    print("3 - Remover uma Pessoa")
    print("4 - Sair do sistema")
    print(40*"-")

def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
            if(num<1 or num>4):
                print("\033[0;31mDigite um número inteiro válido\033[m")
                continue
        except:
            print("\033[0;31mERRO! Digite um numero inteiro\033[m")
            continue
        else:
            return num




