nome = "bira neto"
idade = 20
altura = 1.80
gosta_de = "programar"

print(f"Meu nome é {nome.upper()}.")
print(f"E gosto de {gosta_de.upper()}.")
print(f"Eu tenho {idade} anos.")
print(f"{nome.lower()} gosta de {gosta_de.lower()} e tem {idade} anos.")

#A função .UPPER torna o texto inteiro de uma string MAIÚSCULO.
#A função .LOWER torna o texto inteiro de uma string minúculo.

texto1 = " A função .STRIP retira os espaços de um texto "
print(texto1)
print(texto1.strip())

texto2 = "A função .REPLACE substitui uma palavra, texto ou até apenas uma letra"
print(texto2)
print(texto2.replace("palavra", "coisa"))
print(texto2[0:8])
print(texto2.index("A"))

#Para saber se existe uma palavra ou letra dentro de uma string.

x = "Para" in texto2
y = "a" in texto2

print(x)
print(y)

#Para escrever o texto em linhas diferente se usa a "\".

texto3 = "Vou escrever isso na \"primeira\" linha,\nisso na \"segunda\" e\nisso na \"terceira\" com aspas"
print(texto3)


