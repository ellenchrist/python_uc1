'''class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        print("Au Au!")

class Gato(Animal):
    def fazer_som(self):
        print("Miau!")

def fazer_barulho(animal):
    animal.fazer_som()

meu_cachorro = Cachorro()
meu_gato = Gato()

fazer_barulho(meu_cachorro)  
fazer_barulho(meu_gato)  '''


class Conta:
    def __init__(self, numero, titular, saldo=0.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado na conta {self.numero}.")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente para saque!")
        else:
            self.saldo -= valor
            print (f"Saque de R${valor:.2f} realizado na conta {self.numero}")

    def exibir_dados(self):
        return f"Conta {self.numero} | Titular: {self.titular} | Saldo: R${self.saldo:.2f}"

    def __str__(self):
        return self.exibir_dados()


class Banco:
    def __init__(self):
        # Usamos um dicionário para armazenar as contas: chave é o número da conta
        self.contas = {}

    def adicionar_conta(self, conta):
        if conta.numero in self.contas:
            print("Conta já cadastrada!")
        else:
            self.contas[conta.numero] = conta
            print(f"Conta {conta.numero} adicionada com sucesso!")

    def depositar(self, numero, valor):
        conta = self.contas.get(numero)
        if conta:
            conta.depositar(valor)
        else:
            print("Conta não encontrada!")

    def sacar(self, numero, valor):
        conta = self.contas.get(numero)
        if conta:
            conta.sacar(valor)
        else:
            print("Conta não encontrada!")

    def transferir(self, origem, destino, valor):
        conta_origem = self.contas.get(origem)
        conta_destino = self.contas.get(destino)
        if not conta_origem or not conta_destino:
            print("Conta(s) não encontrada(s)!")
            return
        if conta_origem.saldo >= valor:
            conta_origem.sacar(valor)
            conta_destino.depositar(valor)
            print(f"Transferência de R${valor:.2f} de {origem} para {destino} realizada com sucesso!")
        else:
            print("Saldo insuficiente para transferência!")

    def listar_contas(self):
        print("\n--- Lista de Contas ---")
        for conta in self.contas.values():
            print(conta)
        print("-----------------------\n")


# Exemplo de uso:
banco = Banco()
conta1 = Conta("001", "Alice", 1000.0)
conta2 = Conta("002", "Bruno", 1500.0)

banco.adicionar_conta(conta1)
banco.adicionar_conta(conta2)

banco.depositar("001", 500.0)
banco.sacar("002", 200.0)
banco.transferir("001", "002", 300.0)

banco.listar_contas()