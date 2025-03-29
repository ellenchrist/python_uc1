matriz= [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

soma=0
for i in range(4):
    soma=soma + sum(matriz[i])

print(f"Soma dos elementos acima da diagonal principal: {soma}")


for i, linha in enumerate(matriz):
    print(f"Maior valor da linha {i}: {max(linha)}")

for i in range(4):
    maior=matriz[i][0]
    for j in range(4):
        if matriz[i][j]>maior:
            maior=matriz[i][j]
    print(f"Maior valor da linha {i}: {maior}")

vet_pares=[]
vet_impares=[]
impares=0
pares = 0
for i in range(4):
    for j in range(4):
        if matriz[i][j] % 2 == 0:
            pares = pares + 1
            vet_pares.append(matriz[i][j])
        else:
            impares = impares + 1
            vet_impares.append(matriz[i][j])

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")

print(f"Os números pares são: {vet_pares}")
print(f"Os números pares são: {vet_impares}")

num = int(input("Digite o número para multiplicação: "))
linha_escolhida = int(input("Digite a linha a ser multiplicada (0-3): "))

for j in range(4):
    matriz[linha_escolhida][j] *= num

for linha in matriz:
    print(linha)