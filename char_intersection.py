palavra1=input("Escreva uma palavra: ")
palavra2=input("Escreva outra palavra: ")

intersection=set(palavra1) and set(palavra2)



resultado=""

for car in palavra1:
    if car in intersection and car not in resultado:
        resultado+=car

print(resultado)