#Exibir cabeçalho da tabela
print("A|B|A AND B ")
print("---|---|--------")

#Gerar todas as combinações de A e B
for A in [0, 1]:
    for B in [0, 1]:
        resultado = A and B #Operação AND
        print(f" {A} | {B} |   {resultado} ")
         