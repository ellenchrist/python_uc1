vet_dados=[15,2,94,30,8,76,2024,3,3,3,3]
vetor=[15,2,94,30,8,76,2025,3,3,3,3]

def criar_imprimir_lista ():
    vetor=[15,2,94,30,8,76,2025]
    print (f"\n\t O conteúdo do vetor é {vetor}\n)")

def criar_imprimir_lista_v2 (vetor) :
    print (f"\n\t O conteúdo do vetor é {vetor}\n)")


def interar_sobre_a_lista (vetor):
    for elemento in vetor:
        print("Elemento:", elemento)
    
 
    interar_sobre_a_lista (vet_dados)

def soma_de_vetores (vetor):
    soma=sum(vetor)
    print(f"\n\t A soma dos vetores é {soma}\n)")


    soma_de_vetores (vetor)

        
def maior_e_menor_vetor (vetor):
    maior=max(vetor)
    menor=min(vetor)
    print(f"\n\t O maior vetor é {maior}\n)")
    print(f"\n\t O menor vetor é {menor}\n)")


    maior_e_menor_vetor (vetor)

def vetor_invertido (vetor):
    invertido=vetor[::-1]
    print(f"\n\t O vetor invertido é {invertido}\n)")


    vetor_invertido (vetor)

multiplicador = 2

def multiplicar_elemento_2 (vetor):
    for elemento in vetor: 
        mult=elemento*multiplicador
        print(f"\n\t O vetor multiplicado é {mult}\n)")   


    multiplicar_elemento_2 (vetor)

def contar_elementos (vetor):
    ocorrencias = vetor.count(3)
    print(f"\n\t O valor 3 aparece {ocorrencias} vezes.\n)")   


    contar_elementos (vetor)


def vetor_crescente (vetor):
    vetor_ordenado = sorted(vetor)
    print(f"\n\t O vetor em ordem crescente é {vetor_ordenado}\n)")

if __name__=="__main__" :
    vetor_crescente (vetor)

def remove_vetor_duplicado (vetor):
    vetor_sem_duplicatas = list(dict.fromkeys(vetor))
    print(f"\n\t O vetor sem duplicatas é {vetor_sem_duplicatas}\n)")


    remove_vetor_duplicado (vetor)


vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   
def pares_e_impares (vetor):
    pares = [num for num in vetor if num % 2 == 0]
    impares = [num for num in vetor if num % 2 != 0]
    print(f"\n\t Os vetores pares são {pares}\n)")
    print(f"\n\t Os vetores impares são {impares}\n)")


    pares_e_impares (vetor)

def calculo_media_mostrar_acima (vetor):
    media = sum(vetor) / len(vetor)
    acima_media = [num for num in vetor if num > media]
    print(f"\n\t A média é {media}\n)")
    print(f"\n\t Os acima da média são {acima_media}\n)")

if __name__=="__main__" :
   calculo_media_mostrar_acima (vetor)
    