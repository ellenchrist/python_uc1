"""
frutas=["maçã", "banana", "cereja"]
for fruta in frutas:
    input(f"\t {fruta.upper()}")
    print("\n PRESSIONE ENTER !!!\n") 




contagem = (9,8,7,6,5,4,3,2,1,0,)
for fruta in contagem:
    print(f"{fruta}...")

for i in range(3):
    print(f"{i}-{frutas[i]}")


contador=0
while contador<5:
    print(contador)
    contador +=1
"""

matriz=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()

for i in range(10):
    if i==5:
        break
    if i%2==0:
        continue
    print(i)

for i in range(51):
    if i%2==0:
        continue
    print(i)

for i in range(52):
    if i%2==1:
        continue
    print(i)    

for i in range(3):
    print(i)
else:
    print("Loop concluído!")
            