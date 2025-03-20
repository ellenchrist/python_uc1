numero = int(input("Digite um número (digite um número negativo para sair): "))
adicao = 0
while numero >= 0:
    adicao+=numero
    numero = int(input("Digite um número (digite um número negativo para sair): "))
    
print(f"A soma dos números positivos digitados é: {adicao}")