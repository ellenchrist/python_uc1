idade=int(input("Digite a sua idade : "))
if (idade>=18) or (pais=="s") and (banidos=="n"):
    print("Autorizada a entrada")
else:
    print("Infelizmente, você não pode entrar na festa.")
pais=input("Está acompanhada dos pais? <s/n> : ").lower()
banidos=input("Está na lista dos banidos? <s/n> : ").lower()
print("Infelizmente, você não pode entrar na festa.")


