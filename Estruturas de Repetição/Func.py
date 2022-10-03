def fazer_big_mac(nome):
    print(f"Fazer BiraMac do {nome}")
    
def fazer_batata(tamanho):
    print(f"Fazer batata{tamanho}")
    
def Refri(tipo, tamanho):
    print(f"Fazer Refri {tipo}, {tamanho}")
    
def fazer_combo(nome, tam_batata, tipo_refri, tam_refri):
    nome = str(input("Entre com o nome do cliente: "))
    tam_batata = str(input("Entre com o tamanho da batata: "))
    tipo_refri = str(input("Entre com o tipo de refri: "))
    tam_refri = str(input("Entre com o tamanho do refri: "))
    
    print("Seu pedido está a caminho.")
    print(f"{nome} pediu uma batata {tam_batata}, um refrigerante {tipo_refri} de tamanho {tam_refri}")
    
def frist_while():
    i = int(input("Contar de: ")) 
    x = int(input("Até: "))      
    while i <= x:
        print(i)
        i = i + 1
    
    print("Game Over")  