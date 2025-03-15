nome=input("Iforme seu login com no mínimo três letras : ")
senha=input("Crie uma senha com seis ou mais caracteres : ")
if ( len(nome) < 3):
    print("Seu nome é inválido")
elif ( len(senha) > 6):
    print("Seu usuário foi criado")
elif (senha=="123456") or (senha==senha) :
    print("Sua senha é fraca.")
else:
    print("Seu cadastro foi criado com sucesso!")
