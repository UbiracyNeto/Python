#Vamos trabalhar com colections de dados LISTAS E TUPPLES

familia = ["Karlenia", "Hanna", "Rebeca", "Kira", "Pai"]

print(familia)

familia[4] = "Ubiracy"

print(familia)

#Agregados

familia.extend(["Daniel", "Rafaela"]) #Cria uma nova lista e concatena com a já existente.
familia.append("Vera") #Adiciona o valor espacífico a lista
familia.insert(8, "rafael") #Insere o valor no índice "8" da lista
familia.pop(2) #Remove o valor do último índice
familia.remove("Ubiracy") #Remove um valor específico da lista
familia.insert(0, "Rebeca")

print(familia.count("Vera")) #Conta quantos itens tem na lista.

numeros = [1, 5, 3, 6, 7, 9, 4, 5]
numeros.sort() #Ordena em ordem crescente.
print(numeros)
numeros.reverse()#Ordena em ordem decrescente.
print(numeros)

numeros2 = numeros

#Cria uma nova lista e copia por referência os dados da outra. Sendo assim tudo que for alterado na
# lista "numeros" também será alterado na lista "numeros2".

numeros2 = numeros.copy()

# Cria uma nova lista e copia de fato todos os dados da outra lista. Sendo assim se for feita uma
# alteração na lista "numeros" não terão efeito na lista "numeros2".

#Vamos agora criar um TUPPLE, que basicamente é uma lista, mas um tupple não pode ter os seus valores alterados.

numbers = (1, 2, 3, 4, 5)

#O TUPPLE é declarado com perênteses e não com parênteses retos com as lista normal.
#O TUPPLE terá sempre o valor inicial e nunca poderá ser alterado. Criando assim uma
#restrição de segurança.


