nota1=float(input("Digite a nota da primeira prova : "))
nota2=float(input("Digite a nota da segunda prova : "))
media=(nota1+nota2)/2

trabalho_extra=input("Executou o trabalho extra? <s/n>").lower()

#Trabalho_extra = True
if (media>=7) or (trabalho_extra=="s"):
    print("Você está aprovado")
else:
    print("Você está reprovado")
