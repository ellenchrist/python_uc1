x = 1
y = 1
fibo = x + y
i=0

for i in range(10):
    if i == 0:
       x = 1
       y = 1
       fibo = 1
       print(fibo)
       i+=1
    elif i == 1:
       x = 1
       y = 1
       fibo = 1
       print(fibo)
       i+=1
    else:
       fibo = x + y
       print(fibo)
       x = y
       y = fibo
       fibo = x + y
       i +=1

