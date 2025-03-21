numero = int(input("Digite um número: "))
fatorial = 0
i=0
soma = []
while i+1 <= numero:
    fatorial = numero -i
    soma.append(fatorial)
    i += 1
    print("fatorial",fatorial)
print(sum(soma))