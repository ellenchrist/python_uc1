def somar_elemento ():
    numeros=[]
    for i in range(5):
        numero=int(input("Digite um número: "))
        numeros.append(numero)

    soma=sum(numeros)
    print(f"A soma dos valores lidos é {soma}")

def somar_elemento_v2 (vezes):
    numeros=[]
    for i in range(vezes):
        numero=int(input("Digite um número: "))
        numeros.append(numero)

    soma=sum(numeros)
    print(f"A soma dos valores lidos é a {soma}")

if __name__=="__main__" :
    somar_elemento_v2 (5)

