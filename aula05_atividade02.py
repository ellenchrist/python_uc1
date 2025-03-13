idade=20
tem_carteira = True
if (idade>=18) and (tem_carteira):
    print("Você pode dirigir!")
else:
    print("Desculpe, sem carteira não dá!")

idade=int(input("Digite sua idade : "))
tem_carteira = True
if (idade>=18) and (tem_carteira):
    print("Você pode dirigir!")
else:
    print("Desculpe, sem carteira não dá!")

idade=int(input("Digite sua idade : "))
tem_carteira=input("Você possui carteira de motorista? <s/n> : ")
tem_carteira=tem_carteira.lower()
if(idade>=18) and (tem_carteira=="s"):
    print("Você pode dirigir!")
else:
    print("Desculpe, sem carteira não dá!")