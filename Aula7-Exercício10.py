   # Função recursiva para calcular Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Exibir o 8º termo da sequência de Fibonacci
termo = 10
print(f"O {termo}º termo da sequência de Fibonacci é: {fibonacci(termo)}")
