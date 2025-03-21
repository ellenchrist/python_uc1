i = 0
lista = []
while i <= 4:
    resposta = int(input("Fale um número para adicionar na lista: "))
    i+=1
    lista.append(resposta)
print(f"O maior número é o: {max(lista)}")