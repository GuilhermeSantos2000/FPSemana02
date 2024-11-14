frase=str(input("Escreva qualquer frase: "))

palavras=frase.split(" ")

resultado={}

for palavra in palavras:
    resultado[palavra]=len(palavra)

print (resultado)