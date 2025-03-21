numero = int(input("Coloque o seu número: "))
i = 1 
lista = []
for i in range (1,numero):
   primo = numero%i
   if primo == 0:
      lista.append(primo)
      i+=1
   else:
      i+=1
if len(lista)>2:
   print(f"O número {numero} não é primo")
elif len(lista)<=2:
   print(f"O número {numero} é primo")