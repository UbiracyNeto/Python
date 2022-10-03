def tenho_sede(op):
    op = input("Você está com sede:")
    if op == "SIM":
        print("Beba água")
    else:
        print("Até logo")


def fome_sede():
    op1 = input("Está com fome?")
    op2 = input("Está com sede")

    if op1 == "SIM" and op2 == "SIM":
        print("Vá a cozinha e faça um Sanduíche e beba uma Coca")
    elif op1 == "NÃO" and op2 == "SIM":
        print("Vá a cozinha e beba água")
    elif op1 == "SIM" and op2 == "NÃO":
        print("Vá a cozinha e coma um ovo")
    else:
        print("Continue a estudar")


def maior_num():
    num1 = input("Entre com o Primeiro Número:")
    num2 = input("Entre com o Segundo Número:")

    if num1 > num2:
        print("O Primeiro é o maior")
    else:
        print("O Segundo é o maior")

def swap():
    x = input("Entre com o valor de X:")
    y = input("Entre com o valor de Y:")

    aux = x
    x = y
    y = aux

    print(f"O valor de X agora é {x} e o de Y agora é {y}")