reta1=float(input("Digite o tamanho da primeira reta : "))
reta2=float(input("Digite o tamanho da segunda reta : "))
reta3=float(input("Digite o tamanho da terceira reta : "))
if (reta1==reta2) and (reta2==reta3) :
    print ("É um triângulo equilátero.")
elif (reta1==reta2) or (reta2==reta3) :
    print ("É um triângulo isósceles.")
else:
    print ("É um triângulo escaleno.")
    