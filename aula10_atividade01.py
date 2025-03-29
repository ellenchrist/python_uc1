# Criando uma matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Elemento (0,0):", matriz[0][0])  # Saída: 1
print("Elemento (2,1):", matriz[2][1])  # Saída: 8

for linha in matriz:
    print(f"|", end=" ")
    for elemento in linha:
        print(elemento, end='|')
    print()

matriz= []
for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input(f"Digite o valor para [{i}][{j}]: ")) 
        linha.append(valor)
    matriz.append(linha)

for linha in matriz:
    print(linha)



matriz_4_4 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
soma=0
for i in range(4):
    for j in range(i+1,4):
        soma += matriz_4_4[i][j]

print(f"Soma dos elementos acima da diagonal principal: {soma}")


matriz= [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
soma=0
for i in range(4):
    soma=soma + sum(matriz(i))
print(f"Soma dos elementos acima da diagonal principal: {soma}")
