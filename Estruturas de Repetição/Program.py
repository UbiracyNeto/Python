

pessoas = ("João", "Maria", "José")

canal = "BiraOnTheCode"

for index in range(len(canal)):
    print(index)

for index in range(len(pessoas)):
    print(pessoas[index], index)

for index in range(5):
    if index == 0:
        print("primeira Linha")
    else:
        print(f"Outras linhas {index}")
        

matrix_number = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0]]

for linha in matrix_number:
    print("------")
    for coluna in matrix_number:
        print(coluna)