"""
pessoa={"nome":"Ana","idade":30, "cidade": "São Paulo"}
print(f"Dados da pessoa: {pessoa}")
pessoa["email"]="ana@email.com"
print(f"Dados da pessoa: {pessoa}")
pessoa["idade"]=31
print(f"Dados da pessoa: {pessoa}")
del pessoa["cidade"]
print(pessoa)
pessoa["sexo"]="m"
print(f"Dados atualizado: {pessoa}")


d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

# Método 1: update()
d1.update(d2)

# Método 2: operador ** (Python 3.9+)
d3 = {**d1, **d2}

print("Resultado:", d1)

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

print (f"Dicionários originais")
print (f"D1:     {d1}")
print (f"D2:     {d2}")

d1.update(d2)
d2.update(d3)

print(f"Dicionários atualizados:  ")
print (f"D1:     {d1}")
print (f"D2:     {d2}")

frase = "o rato roeu a roupa do rei de roma"
palavras = frase.split()
contagem = {}

for palavra in palavras:
    contagem[palavra] = contagem.get(palavra, 0) + 1

print(contagem)

alunos = {}

# Adicionar alunos
alunos[1] = {"nome": "Maria", "notas": [7.5, 8.0, 9.2]}
alunos[2] = {"nome": "João", "notas": [6.0, 7.8, 8.5]}
alunos[3] = {"nome": "Carlos", "notas": [5.5, 6.5, 7.0]}

# Calcular médias
for id_aluno, info in alunos.items():
    notas = info["notas"]
    media = sum(notas) / len(notas)
    info["média"] = round(media, 2)

print(alunos)
"""

class Carro:
    # Método construtor (__init__) para inicializar os atributos
    def __init__(self, marca, modelo, ano):
        self.marca = marca  # Atributo
        self.modelo = modelo  # Atributo
        self.ano = ano  # Atributo
        self.ligado = False  # Atributo com valor padrão

    # Método para ligar o carro
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"{self.marca} {self.modelo} está ligado.")
        else:
            print(f"{self.marca} {self.modelo} já está ligado.")

    # Método para desligar o carro
    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f"{self.marca} {self.modelo} está desligado.")
        else:
            print(f"{self.marca} {self.modelo} já está desligado.")

    # Método para exibir informações do carro
    def exibir_info(self):
        status = "ligado" if self.ligado else "desligado"
        print(f"{self.marca} {self.modelo} ({self.ano}) está {status}.")

# Criando um objeto da classe Carro
meu_carro = Carro("Toyota", "Corolla", 2020)

# Usando métodos do objeto
meu_carro.exibir_info()  # Exibe as informações do carro
meu_carro.ligar()  # Liga o carro
meu_carro.exibir_info()  # Exibe as informações do carro novamente
meu_carro.desligar()  # Desliga o carro
meu_carro.exibir_info()  # Exibe as informações do carro novamente