i = 1
notas = []
for i in range (5):
   numero = int(input("Digite a sua nota: "))
   notas.append(numero)
menor = min(notas)
print((sum(notas)-menor)/4)