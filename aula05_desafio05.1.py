idade=18
Senha="5555"
idade=int(input("Digite sua idade : "))
Senha_correta=input("Digite sua senha : ").lower()
if idade>=18 :
    if Senha==Senha_correta :
        print("Acesso liberado!")
    else:
        print("Acesso bloqueado!")
else:
        print("Idade inválida")


