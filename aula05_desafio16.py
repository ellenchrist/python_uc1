idade=int(input("Digite a sua idade : "))
renda=float(input("Digite a sua renda : "))
serasa=input("Você já recebeu uma carta do SPC/Serasa? <s/n> : ").lower()

if (idade>=21) and (renda>=2000) and (serasa=="n"):
    print ("Empréstimo aprovado!")
else:
    print ("Emprétimo não aprovado.")